import objc
import os
from objc import super  # noqa: A004
from .supercall import OCSuperCallHelper
from PyObjCTools.TestSupport import (
    TestCase,
    pyobjc_options,
    no_autorelease_pool,
    skipUnless,
    os_level_key,
    os_release,
)
import objc.simd

NSObject = objc.lookUpClass("NSObject")


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

        with self.assertRaisesRegex(TypeError, "missing required argument"):
            objc._updatingMetadata()

    def test_valid_usage(self):
        # The tests in this method have  permanent side effects,
        # make sure that mutating tests only use classes that
        # aren't used elsewhere in the test suite.

        # Use '_updatingMetadata' to force a rescan

        with self.subTest("setup"):
            objc._updatingMetadata(True)
            objc._updatingMetadata(False)
            objc._rescanClass(name="NSObject")

            objc._updatingMetadata(True)
            objc._updatingMetadata(False)
            objc._rescanClass("NSObject")

            objc._updatingMetadata(True)
            objc._updatingMetadata(False)
            objc._rescanClass("SomeNonexistingClass")

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)

        with self.subTest("dummy attribute"):

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

        with self.subTest("weird attributes"):

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

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)

        class NoCompare:
            def __eq__(self, other):
                raise TypeError("cannot compare")

        no_compare = NoCompare()

        with self.subTest("No compare  class extender"):

            def dummy_extender(klass, class_dict):
                class_dict["foo"] = no_compare

            cls.foo = objc.python_method(lambda self: 99)
            try:
                with pyobjc_options(_class_extender=dummy_extender):
                    objc._updatingMetadata(True)
                    objc._updatingMetadata(False)

                    with self.assertRaisesRegex(TypeError, "cannot compare"):
                        objc._rescanClass(cls.__name__)

                        print(cls.foo)

            finally:
                del cls.foo

        objc._updatingMetadata(True)
        objc._updatingMetadata(False)

        info1 = cls.downloadTaskWithURL_completionHandler_.__metadata__()
        objc._updatingMetadata(True)
        objc._updatingMetadata(False)
        info2 = cls.downloadTaskWithURL_completionHandler_.__metadata__()
        self.assertEqual(info1, info2)

        for attr in ("__dict__", "__bases__", "__slots__", "__mro__"):

            with self.subTest("tweak attr", key=attr):

                def dummy_extender(klass, class_dict, attr=attr):
                    if klass.__name__ == "NSURLSession":
                        class_dict[attr] = attr

                with pyobjc_options(_class_extender=dummy_extender):
                    objc._updatingMetadata(True)
                    objc._updatingMetadata(False)

                    objc._rescanClass("NSURLSession")
                    self.assertNotEqual(getattr(cls, attr), attr)

            objc._updatingMetadata(True)
            objc._updatingMetadata(False)

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
        if getattr(self, "_raise", False):
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


class TestRegisterVectorTypes(TestCase):
    # This only tests some non-standard cases, the regular code
    # path's are used already.
    def test_twice(self):
        v = objc.repythonify((1, 2), b"<2f>")
        self.assertIsInstance(v, objc.simd.vector_float2)

        try:
            # Create a new vector type with the same encoding and
            # check that this is used instead.
            cls = objc.simd.make_type("vector_float2", 0.0, float, 2, typestr=b"<2f>")
            self.assertIsNot(cls, objc.simd.vector_float2)

            v = objc.repythonify((1, 2), b"<2f>")
            self.assertIsInstance(v, cls)

        finally:
            # Finally restory the previous situation
            objc._registerVectorType(objc.simd.vector_float2)

        v = objc.repythonify((1, 2), b"<2f>")
        self.assertIsInstance(v, objc.simd.vector_float2)

    def test_unused_simd(self):
        with self.assertRaisesRegex(
            objc.internal_error, "Unsupported SIMD encoding: <7f>"
        ):
            objc.simd.make_type("vector_float7", 0.0, float, 7, typestr=b"<7f>")

    def test_invalid_type(self):
        class vector:
            pass

        with self.assertRaisesRegex(
            AttributeError, "type object 'vector' has no attribute '__typestr__'"
        ):
            objc._registerVectorType(vector)

        vector.__typestr__ = 42
        with self.assertRaisesRegex(TypeError, "__typstr__ must be bytes"):
            objc._registerVectorType(vector)


class TestMakeClosure(TestCase):
    # Most of the code is tested implicitly, only test some error cases here
    def test_api_misuse(self):
        with self.assertRaisesRegex(TypeError, "function missing required argument"):
            objc._makeClosure()


class TestClosurePointer(TestCase):
    # Most of the code is tested implicitly, only test some error cases here
    def test_api_misuse(self):
        with self.assertRaisesRegex(TypeError, "function missing required argument"):
            objc._closurePointer()

        o = objc.lookUpClass("NSObject").alloc().init()

        capsule = o.__cobject__()
        with self.assertRaisesRegex(
            ValueError, "PyCapsule_GetPointer called with incorrect name"
        ):
            objc._closurePointer(capsule)


class TestLoadConstant(TestCase):
    # Most of the code is tested implicitly, only test some error cases here
    def test_api_misuse(self):
        with self.assertRaisesRegex(TypeError, "function missing required argument"):
            objc._loadConstant()


class TestRegisteredMetadata(TestCase):
    # Most of the code is tested implicitly, only test some error cases here
    def test_api_misuse(self):
        with self.assertRaisesRegex(TypeError, "function takes exactly"):
            objc._registeredMetadataForSelector()

        with self.assertRaisesRegex(TypeError, "Expecting a class"):
            objc._registeredMetadataForSelector(object, b"init")

        with self.assertRaisesRegex(TypeError, "a bytes-like object is required"):
            objc._registeredMetadataForSelector(objc.lookUpClass("NSObject"), "init")


class TestSizeOfType(TestCase):
    def test_sizeOfType(self):
        self.assertEqual(objc._sizeOfType(objc._C_LNG_LNG), 8)

        with self.assertRaisesRegex(
            objc.internal_error, "PyObjCRT_SizeOfType: Unhandled type"
        ):
            objc._sizeOfType(b"xyz")

        with self.assertRaisesRegex(TypeError, "a bytes-like object is required"):
            objc._sizeOfType(42)


class TestOverrideResolution(TestCase):
    # Tests checks validate the logic for resolving a custom method call function
    # when overrides are registered in different orders for base and sub classes.
    @classmethod
    def setUpClass(cls):
        cls.baseclass = NSObject.alloc().init()
        cls.subclass = OCSuperCallHelper.alloc().init()

    def test_register_nsobject_first(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerFirst(), "overriden-first-nsobject"
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerFirst(), "overriden-first-subclass"
        )

    def test_register_nsobject_last(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerLast(), "overriden-last-nsobject"
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerLast(), "overriden-last-subclass"
        )

    def test_register_nsobject_first_nil_before(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerFirstNone1(),
            "overriden-first-none1-nsobject",
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerFirstNone1(), "overriden-first-none1-subclass"
        )

    def test_register_nsobject_last_nil_before(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerLastNone1(), "overriden-last-none1-nsobject"
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerLastNone1(), "overriden-last-none1-subclass"
        )

    def test_register_nsobject_first_nil_after(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerFirstNone2(),
            "overriden-first-none2-nsobject",
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerFirstNone2(), "overriden-first-none2-subclass"
        )

    def test_register_nsobject_last_nil_after(self):
        self.assertEqual(
            self.baseclass.ocRegisterCallerLastNone2(), "overriden-last-none2-nsobject"
        )
        self.assertEqual(
            self.subclass.ocRegisterCallerLastNone2(), "overriden-last-none2-subclass"
        )

    def test_register_subclss_only(self):
        self.assertEqual(
            self.baseclass.ocRegisterSubClassOnly(), "native-subclass-only"
        )
        self.assertEqual(
            self.subclass.ocRegisterSubClassOnly(), "overriden-subclass-only-subclass"
        )

    def test_register_subclss_only_none_first(self):
        self.assertEqual(
            self.baseclass.ocRegisterSubClassOnlyNone1(),
            "overriden-subclass-only-none1-none",
        )
        self.assertEqual(
            self.subclass.ocRegisterSubClassOnlyNone1(),
            "overriden-subclass-only-none1-subclass",
        )

    def test_register_subclss_only_none_last(self):
        self.assertEqual(
            self.baseclass.ocRegisterSubClassOnlyNone2(),
            "overriden-subclass-only-none2-none",
        )
        self.assertEqual(
            self.subclass.ocRegisterSubClassOnlyNone2(),
            "overriden-subclass-only-none2-subclass",
        )


class TestSelectorEdgeCases(TestCase):
    def test_selector_invalid_name(self):
        def fn(self):
            pass

        fn.__name__ = "\udfff"
        with self.assertRaisesRegex(UnicodeError, "surrogate"):
            fn.__name__.encode()

        with self.assertRaisesRegex(UnicodeError, "surrogate"):
            objc.selector(fn)

        # Setting the name to non-string doesn't work:
        with self.assertRaises(TypeError):
            fn.__name__ = b"fn"
