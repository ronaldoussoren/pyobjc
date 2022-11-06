import objc
from PyObjCTools.TestSupport import TestCase

objc.registerMetaDataForSelector(
    b"OC_CallbackTest",
    b"selWithSEL:SEL:andObject:",
    {"arguments": {2: {"sel_of_type": b"q@:q"}, 3: {"sel_of_type": b"v@:@@^v"}}},
)

objc.registerMetaDataForSelector(
    b"OC_CallbackTest",
    b"selWithCallback:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"q"},
                    "arguments": {"0": {"type": b"@"}, "1": {"type": b"i"}},
                }
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OC_CallbackTest",
    b"selWithCallback2:",
    {"arguments": {2: {"callable": {"retval": {"type": b"d"}, "arguments": {}}}}},
)

objc.registerMetaDataForSelector(
    b"OC_CallbackTest",
    b"selWithCallback:andCallback:",
    {
        "arguments": {
            2: {"callable": {"arguments": {"0": {"type": b"@"}}}},
            3: {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {"0": {"type": b"q"}, "1": {"type": b"^v"}},
                }
            },
        }
    },
)


class OC_CallbackTest(objc.lookUpClass("NSObject")):
    @objc.typedSelector(b"v@:" + objc._C_SEL + objc._C_SEL + b"@")
    def selWithSEL_SEL_andObject_(self, s1, s2, o):
        pass

    @objc.typedSelector(b"v@:" + objc._C_SEL)
    def selWithoutSEL_(self, o):
        pass

    @objc.typedSelector(b"v@:?")
    def selWithCallback_(self, cb):
        pass

    @objc.typedSelector(b"v@:?")
    def selWithCallback2_(self, cb):
        pass

    @objc.typedSelector(b"v@:??")
    def selWithCallback_andCallback_(self, cb1, cb2):
        pass


class TestClosure(TestCase):
    # tests for objc._makeClosure
    # (note: as the name indicates _makeClosure is not a public API)
    def testCallbackForUnsupported(self):
        def function(arg):
            pass

        with self.assertRaisesRegex(
            TypeError,
            "Don't know how to create closure for instance of builtin_function_or_method",
        ):
            objc._makeClosure(function, dir, -1)
        with self.assertRaisesRegex(
            TypeError, "Don't know how to create closure for instance of function"
        ):
            objc._makeClosure(function, function, -1)
        with self.assertRaisesRegex(
            TypeError, "Don't know how to create closure for instance of int"
        ):
            objc._makeClosure(function, 42, -1)
        with self.assertRaisesRegex(
            ValueError, "No callback argument in the specified object"
        ):
            objc._makeClosure(
                function,
                OC_CallbackTest.selWithSEL_SEL_andObject_,
                -1,
            )
        with self.assertRaisesRegex(
            ValueError, "No callback argument in the specified object"
        ):
            objc._makeClosure(function, OC_CallbackTest.selWithoutSEL_, -1)

    def testCreatingCallbacks(self):
        def function(*arg):
            pass

        cl = objc._makeClosure(function, OC_CallbackTest.selWithCallback_, -1)
        self.assertIn(' "objc.__imp__" ', repr(cl))
        cl = objc._makeClosure(function, OC_CallbackTest.selWithCallback2_, -1)
        self.assertIn(' "objc.__imp__" ', repr(cl))
        cl = objc._makeClosure(
            function, OC_CallbackTest.selWithCallback_andCallback_, -1
        )
        self.assertIn(' "objc.__imp__" ', repr(cl))
        cl = objc._makeClosure(
            function, OC_CallbackTest.selWithCallback_andCallback_, 2
        )
        self.assertIn(' "objc.__imp__" ', repr(cl))
        cl = objc._makeClosure(
            function, OC_CallbackTest.selWithCallback_andCallback_, 3
        )
        self.assertIn(' "objc.__imp__" ', repr(cl))

        with self.assertRaisesRegex(
            objc.BadPrototypeError,
            "Objective-C expects 2 arguments, .* has 1 positional arguments",
        ):
            objc._makeClosure(
                lambda a: None,
                OC_CallbackTest.selWithCallback_,
                -1,
            )
        objc._makeClosure(lambda a, b: None, OC_CallbackTest.selWithCallback_, -1)
        with self.assertRaisesRegex(
            objc.BadPrototypeError,
            "Objective-C expects 2 arguments, .* has 3 positional arguments",
        ):
            objc._makeClosure(
                lambda a, b, c: None,
                OC_CallbackTest.selWithCallback_,
                -1,
            )


class TestCallbackFor(TestCase):
    # tests for objc.callbackFor
    def testCallbackForUnsupported(self):
        def function(arg):
            pass

        with self.assertRaisesRegex(
            TypeError,
            "Don't know how to create closure for instance of builtin_function_or_method",
        ):
            objc.callbackFor(dir)(function)
        with self.assertRaisesRegex(
            TypeError, "Don't know how to create closure for instance of function"
        ):
            objc.callbackFor(function)(function)
        with self.assertRaisesRegex(
            TypeError, "Don't know how to create closure for instance of int"
        ):
            objc.callbackFor(42)(function)
        with self.assertRaisesRegex(
            ValueError, "No callback argument in the specified object"
        ):
            objc.callbackFor(OC_CallbackTest.selWithSEL_SEL_andObject_)(
                function,
            )
        with self.assertRaisesRegex(
            ValueError, "No callback argument in the specified object"
        ):
            objc.callbackFor(OC_CallbackTest.selWithoutSEL_)(function)

    def testCreatingCallbacks(self):
        # XXX: Need variant using objc.function
        @objc.callbackFor(OC_CallbackTest.selWithCallback_)
        def function(arg1, arg2):
            pass

        self.assertIn(' "objc.__imp__" ', repr(function.pyobjc_closure))
        meta = function.__metadata__()
        self.assertIsInstance(meta, dict)
        self.assertEqual(len(meta["arguments"]), 2)

        self.assertIsInstance(objc.callbackPointer(function), int)
        with self.assertRaisesRegex(
            ValueError, "Object is not decorated with 'callbackFor'"
        ):
            objc.callbackPointer(None)

        @objc.callbackFor(OC_CallbackTest.selWithCallback2_)
        def function():
            pass

        self.assertIn(' "objc.__imp__" ', repr(function.pyobjc_closure))

        @objc.callbackFor(OC_CallbackTest.selWithCallback_andCallback_, -1)
        def function(a):
            pass

        self.assertIn(' "objc.__imp__" ', repr(function.pyobjc_closure))

        @objc.callbackFor(OC_CallbackTest.selWithCallback_andCallback_, 2)
        def function(a):
            pass

        self.assertIn(' "objc.__imp__" ', repr(function.pyobjc_closure))

        @objc.callbackFor(OC_CallbackTest.selWithCallback_andCallback_, 3)
        def function(a, b):
            pass

        self.assertIn(' "objc.__imp__" ', repr(function.pyobjc_closure))

        with self.assertRaisesRegex(
            objc.BadPrototypeError,
            "Objective-C expects 2 arguments, .* has 1 positional arguments",
        ):
            objc.callbackFor(OC_CallbackTest.selWithCallback_)(
                lambda a: None,
            )
        with self.assertRaisesRegex(
            objc.BadPrototypeError,
            "Objective-C expects 2 arguments, .* has 3 positional arguments",
        ):
            objc.callbackFor(OC_CallbackTest.selWithCallback_)(
                lambda a, b, c: None,
            )


class TestSelectorFor(TestCase):
    # tests for objc.selectorFor
    def test_consistency(self):
        self.assertEqual(OC_CallbackTest.selWithSEL_SEL_andObject_.signature, b"v@:::@")

    def testNotSelector(self):
        with self.assertRaisesRegex(
            ValueError, "Not a selector argument with type information"
        ):
            objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 4)
        with self.assertRaisesRegex(
            ValueError, "Not a selector argument with type information"
        ):
            objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 8)
        with self.assertRaisesRegex(
            ValueError, "Not a selector argument with type information"
        ):
            objc.selectorFor(OC_CallbackTest.selWithoutSEL_)

    def testDefault(self):
        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"q@:q")

    def testExplicit(self):
        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 2)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"q@:q")

        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 3)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"v@:@@^v")
