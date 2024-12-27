import objc
import os
from objc import super  # noqa: A004
from PyObjCTools.TestSupport import (
    TestCase,
    pyobjc_options,
    no_autorelease_pool,
    skipUnless,
    os_level_key,
    os_release,
)


class TestMetadataRegistry(TestCase):
    def test_copyMetadataRegistry_valid(self):
        result = objc._copyMetadataRegistry()
        self.assertIsInstance(result, dict)

        for selector, info in result.items():
            self.assertIsInstance(selector, bytes)
            self.assertIsInstance(info, list)
            for item in info:
                self.assertIsInstance(item, tuple)
                self.assertEqual(len(item), 2)
                self.assertIsInstance(item[0], bytes)
                self.assertIsInstance(item[1], dict)

                meta = item[1]
                self.assertIn("arguments", meta)
                self.assertIn("retval", meta)
                self.assertIsInstance(meta["arguments"], tuple)
                self.assertIsInstance(meta["retval"], (dict, type(None)))

                # XXX: Maybe look for a particular set of metadata and
                #      verify that it is compatible with the ``__metadata__``
                #      method of the selector.

    def test_copyMetadataRegistry_deepcopies(self):
        # Make sure this results a copy of the registry, not the registry itself
        result = objc._copyMetadataRegistry()
        result["foo"] = "bar"
        extra = objc._copyMetadataRegistry()
        self.assertNotIn("foo", extra)

        del result["foo"]
        self.assertEqual(extra, result)

        result[next(iter(result.keys()))].append("hello")

        self.assertNotEqual(extra, result)

    def test_copyMetadataRegistry_invalid(self):
        with self.assertRaisesRegex(
            TypeError,
            r".*_copyMetadataRegistry\(\) takes no arguments \(1 given\)",
        ):
            objc._copyMetadataRegistry(1)

    def test_metadata_reolacement(self):
        sel = b"replacement:"
        sel2 = b"replacement2:"

        # Register some metadata and check that it can be found
        objc.registerMetaDataForSelector(
            b"NSObject", sel, {"retval": {"type": objc._C_INT}}
        )

        metadata = objc._copyMetadataRegistry()
        self.assertIn(sel, metadata)
        self.assertEqual(len(metadata[sel]), 1)

        self.assertEqual(metadata[sel][0][0], b"NSObject")
        self.assertEqual(metadata[sel][0][1]["retval"]["type"], objc._C_INT)

        # Replace the registration:
        objc.registerMetaDataForSelector(
            b"NSObject", sel, {"retval": {"type": objc._C_UINT}}
        )

        metadata = objc._copyMetadataRegistry()
        self.assertIn(sel, metadata)
        self.assertEqual(len(metadata[sel]), 1)

        self.assertEqual(metadata[sel][0][0], b"NSObject")
        self.assertEqual(metadata[sel][0][1]["retval"]["type"], objc._C_UINT)

        # Register for a different parent class
        objc.registerMetaDataForSelector(
            b"NSArray", sel, {"retval": {"type": objc._C_INT}}
        )
        objc.registerMetaDataForSelector(
            b"NSMutableArray", sel, {"retval": {"type": objc._C_FLT}}
        )

        # And register in a different order:
        objc.registerMetaDataForSelector(
            b"NSMutableArray", sel2, {"retval": {"type": objc._C_FLT}}
        )
        objc.registerMetaDataForSelector(
            b"NSArray", sel2, {"retval": {"type": objc._C_SHT}}
        )
        objc.registerMetaDataForSelector(
            b"NSObject", sel2, {"retval": {"type": objc._C_USHT}}
        )

        # Define a new subclass, check that the new, and most specific, metadata is used.
        class OC_InternalTest(objc.lookUpClass("NSArray")):
            def replacement_(self, arg):
                return 1

            def replacement2_(self, arg):
                return 1

            def replacement3_(self, arg):
                return 1

        self.assertResultHasType(OC_InternalTest.replacement_, objc._C_INT)
        self.assertResultHasType(OC_InternalTest.replacement2_, objc._C_SHT)
        self.assertResultHasType(OC_InternalTest.replacement3_, objc._C_ID)


class TestRescanClass(TestCase):
    def test_invalid_usage(self):
        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'name' \(pos 1\))|(Required argument 'name' \(pos 1\) not found)",
        ):
            objc._rescanClass()

        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'name' \(pos 1\))|(Required argument 'name' \(pos 1\) not found)",
        ):
            objc._rescanClass(naam="NSObject")

    def test_valid_usage(self):
        # The tests in this method have  permanent side effects,
        # make sure that mutating tests only use classes that
        # aren't used elsewhere in the test suite.

        # Use '_updatingMetadata' to force a rescan
        objc._updatingMetadata(True)
        objc._updatingMetadata(False)
        objc._rescanClass(name="NSObject")

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)
        objc._rescanClass("NSObject")

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)
        objc._rescanClass("SomeNonexistingClass")

        def dummy_extender(klass, class_dict):
            if klass.__name__ == "NSURLSession":
                class_dict["_dummy_attribute_"] = 42

        cls = objc.lookUpClass("NSURLSession")
        self.assertNotHasAttr(cls, "_dummy_attribute_")
        with pyobjc_options(_class_extender=dummy_extender):
            objc._updatingMetadata(True)
            objc._updatingMetadata(False)
            objc._rescanClass("NSURLSession")
            self.assertHasAttr(cls, "_dummy_attribute_")

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)

        def dummy_extender(klass, class_dict):
            if klass.__name__ == "NSURLSession":
                class_dict[2001] = "spaces"
                class_dict["__has_python_implementation__"] = 0

        with pyobjc_options(_class_extender=dummy_extender):
            objc._updatingMetadata(True)
            objc._updatingMetadata(False)

            objc._rescanClass("NSURLSession")
            self.assertIn(2001, cls.__dict__)
            self.assertNotEqual(cls.init, 42)

        for attr in ("__dict__", "__bases__", "__slots__", "__mro__"):

            def dummy_extender(klass, class_dict, attr=attr):
                if klass.__name__ == "NSURLSession":
                    class_dict[attr] = attr

            with pyobjc_options(_class_extender=dummy_extender):
                objc._updatingMetadata(True)
                objc._updatingMetadata(False)

                objc._rescanClass("NSURLSession")
                self.assertNotEqual(getattr(cls, attr), attr)

    def test_rescan_raises(self):
        def raising_extender(*args, **kwds):
            raise RuntimeError("dont extend")

        with pyobjc_options(_class_extender=raising_extender):
            with self.assertRaisesRegex(RuntimeError, "dont extend"):
                # Use '_updatingMetadata' to force a rescan
                objc._updatingMetadata(True)
                objc._updatingMetadata(False)
                objc._rescanClass("NSObject")

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)
        objc._rescanClass("NSObject")


class TestNameForSignature(TestCase):
    def test_invalid_usage(self):
        with self.assertRaisesRegex(
            TypeError,
            r".*_nameForSignature\(\) takes exactly one argument \(0 given\)",
        ):
            objc._nameForSignature()

        with self.assertRaisesRegex(
            TypeError, "type encoding must be a bytes string, not a 'str' object"
        ):
            objc._nameForSignature("some struct")

    def test_valid_usage(self):
        self.assertIs(objc._nameForSignature(objc._C_INT), None)

        # XXX: The rest of the implementation is tested implicitly,
        #      add tests here as well.


class OC_ReleasePool_Recorder(objc.lookUpClass("NSObject")):
    def initWithCallback_(self, callback):
        self = super().init()
        self.callback = callback
        return self

    def dealloc(self):
        self.callback()
        super().dealloc()


class RaisingRelease(objc.lookUpClass("NSObject")):
    def init(self):
        self = super().init()
        self._raise = True
        return self

    def release(self):
        if self._raise:
            self._raise = False
            objc.lookUpClass("NSException").exceptionWithName_reason_userInfo_(
                "SomeException", "Reason", None
            ).raise__()


class TestReleasePoolManagement(TestCase):
    # Tests that check various aspect of management of
    # the global fallback release pool managed by the
    # pyobjc extension.
    #
    # 1. recycle (check that pool gets drained)
    # 2. clear (check that pool is removed, and that recycle reinstates)
    # 3. check that draining an outer pool resets the pyobjc pool

    def test_machinery(self):
        record = []
        v = OC_ReleasePool_Recorder.alloc().initWithCallback_(
            lambda: record.append(True)
        )
        self.assertEqual(record, [])
        del v
        self.assertEqual(record, [True])

    @skipUnless(
        not (
            os_level_key("10.14") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "crashes on 10.14???",
    )
    @no_autorelease_pool
    def test_manual_recycle(self):
        objc.recycleAutoreleasePool()
        record = []
        v = OC_ReleasePool_Recorder.alloc().initWithCallback_(
            lambda: record.append(True)
        )
        self.assertEqual(record, [])
        v.retain()
        v.autorelease()
        del v
        self.assertEqual(record, [])
        objc.recycleAutoreleasePool()
        self.assertEqual(record, [True])
        self.assertTrue(objc._haveAutoreleasePool())

    @no_autorelease_pool
    def test_manual_recycle_exception(self):
        self.assertTrue(objc._haveAutoreleasePool())
        try:
            o = RaisingRelease.alloc().init()
            o.retain()
            o.autorelease()
            with self.assertRaisesRegex(objc.error, "SomeException - Reason"):
                objc.removeAutoreleasePool()
            self.assertFalse(objc._haveAutoreleasePool())
        finally:
            objc.recycleAutoreleasePool()
            self.assertTrue(objc._haveAutoreleasePool())

    @no_autorelease_pool
    def test_removing_pool(self):
        self.assertTrue(objc._haveAutoreleasePool())
        try:
            objc.removeAutoreleasePool()
            self.assertFalse(objc._haveAutoreleasePool())
        finally:
            objc.recycleAutoreleasePool()
            self.assertTrue(objc._haveAutoreleasePool())

    @no_autorelease_pool
    def test_removing_pool_exception(self):
        # There's not much we can assert about the state of objects
        # in the release pool when one of them raises in
        # -release, just test that we still have a pool.
        objc.recycleAutoreleasePool()
        o = RaisingRelease.alloc().init()
        o.retain()
        o.autorelease()
        with self.assertRaisesRegex(objc.error, "SomeException - Reason"):
            objc.recycleAutoreleasePool()
        self.assertTrue(objc._haveAutoreleasePool())

    @skipUnless(
        not (
            os_level_key("10.14") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "crashes on 10.14???",
    )
    @no_autorelease_pool
    def test_draining_outer_pool(self):
        objc.removeAutoreleasePool()

        pool = objc.lookUpClass("NSAutoreleasePool").alloc().init()

        objc.recycleAutoreleasePool()
        record = []
        v = OC_ReleasePool_Recorder.alloc().initWithCallback_(
            lambda: record.append(True)
        )
        self.assertEqual(record, [])
        v.retain()
        v.autorelease()
        del v
        self.assertEqual(record, [])
        del pool
        self.assertEqual(record, [True])

        # The automatic recycle pool is cleared when the
        # pool it is nested in gets drained. In this
        # scenario the pool managed by PyObjC isn't needed.
        self.assertFalse(objc._haveAutoreleasePool())

        # Restory the pool to get default behaviour back.
        objc.recycleAutoreleasePool()
        self.assertTrue(objc._haveAutoreleasePool())


NSBundle = objc.lookUpClass("NSBundle")


class TestCurrentBundle(TestCase):
    # Note: bugs in the test or the implementation will likely crash
    # the interpreter as the implementation trusts that the
    # value of an environment variable is a valid pointer...

    def test_default(self):
        self.assertIs(objc.currentBundle(), NSBundle.mainBundle())

    def test_invalid_pointer(self):
        os.putenv("PYOBJC_BUNDLE_ADDRESS", "rotzooi")
        try:
            self.assertIs(objc.currentBundle(), NSBundle.mainBundle())
        finally:
            os.unsetenv("PYOBJC_BUNDLE_ADDRESS")

        os.putenv("PYOBJC_BUNDLE_ADDRESS", "0x12monkeys")
        try:
            self.assertIs(objc.currentBundle(), NSBundle.mainBundle())
        finally:
            os.unsetenv("PYOBJC_BUNDLE_ADDRESS")

        os.putenv("PYOBJC_BUNDLE_ADDRESS", "")
        try:
            self.assertIs(objc.currentBundle(), NSBundle.mainBundle())
        finally:
            os.unsetenv("PYOBJC_BUNDLE_ADDRESS")

    def test_invalid_use(self):
        with self.assertRaisesRegex(
            TypeError, r".*currentBundle\(\) takes no arguments \(1 given\)"
        ):
            objc.currentBundle(None)

    def test_alternate(self):
        b = NSBundle.bundleWithPath_("/System/Library/Frameworks/Foundation.framework")
        self.assertIsInstance(b, NSBundle)

        os.putenv("PYOBJC_BUNDLE_ADDRESS", f"{hex(objc.pyobjc_id(b))}")
        try:
            self.assertIs(objc.currentBundle(), b)
        finally:
            os.unsetenv("PYOBJC_BUNDLE_ADDRESS")


class TestOCBundleHack(TestCase):
    def test_bundle_hack_not_used(self):
        # XXX: Temporary test to check if the code in OC_NSBunldeHack is needed on
        # one of the supported platforms.
        self.assertFalse(objc.options._bundle_hack_used)
