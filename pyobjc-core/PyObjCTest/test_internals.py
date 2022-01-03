import objc
from PyObjCTools.TestSupport import TestCase, pyobjc_options


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
            TypeError, r"function takes at most 0 arguments \(1 given\)"
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
            TypeError, r"function missing required argument 'name' \(pos 1\)"
        ):
            objc._rescanClass()

        with self.assertRaisesRegex(
            TypeError, r"function missing required argument 'name' \(pos 1\)"
        ):
            objc._rescanClass(naam="NSObject")

    def test_valid_usage(self):
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
            if klass.__name__ == "NSObject":
                class_dict["_dummy_attribute_"] = 42

        cls = objc.lookUpClass("NSObject")
        self.assertNotHasAttr(cls, "_dummy_attribute_")
        with pyobjc_options(_class_extender=dummy_extender):
            objc._updatingMetadata(True)
            objc._updatingMetadata(False)
            objc._rescanClass("NSObject")
            self.assertHasAttr(cls, "_dummy_attribute_")

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
            r"objc._objc._nameForSignature\(\) takes exactly one argument \(0 given\)",
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
