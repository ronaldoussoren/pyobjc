import os

import objc
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_object_proxy import NoObjectiveC
from PyObjCTest.metadatafunction import function_list


from . import fnd as Foundation

NSObject = objc.lookUpClass("NSObject")


def S(*args):
    return b"".join(args)


FUNCTIONS = [
    ("NSHomeDirectory", S(objc._C_ID)),
    ("NSIsFreedObject", S(objc._C_NSBOOL, objc._C_ID)),
    ("NSCountFrames", S(objc._C_UINT)),
    ("NSClassFromString", S(objc._C_CLASS, objc._C_ID)),
]


class TestBundleFunctions(TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testSimple(self):
        for bundle in (None, self.bundle):
            with self.subTest(bundle):
                d = {}
                objc.loadBundleFunctions(bundle, d, FUNCTIONS)

                self.assertIn("NSIsFreedObject", d)
                self.assertIn("NSCountFrames", d)
                self.assertIn("NSHomeDirectory", d)

                # Don't use this API, it is unsupported and causes warnings.
                # fn = d[u'NSIsFreedObject']
                # obj = NSObject.alloc().init()
                # value = fn(obj)
                # self.assertTrue(not value)

                fn = d["NSHomeDirectory"]
                value = fn()
                self.assertEqual(value, os.path.expanduser("~"))

                fn = d["NSClassFromString"]
                value = fn("NSObject")
                self.assertIs(value, NSObject)

                # Need to look for a different example, NSCountFrames crashes
                # (that is the actual function, not the dynamic wrapper)
                # fn = d[u'NSCountFrames']
                # import Foundation
                # fn = Foundation.NSCountFrames
                # value = fn()
                # self.assertIsInstance(value, int)

    def test_missing(self):
        functions = FUNCTIONS[:]
        functions.insert(1, ("NoSuchFunction", b"v"))
        for bundle in (None, self.bundle):
            with self.subTest(bundle=bundle, ignore=True):
                d = {}
                objc.loadBundleFunctions(bundle, d, functions)

                self.assertIn("NSIsFreedObject", d)
                self.assertIn("NSCountFrames", d)
                self.assertIn("NSHomeDirectory", d)

            with self.subTest(bundle=bundle, ignore=False):
                d = {}

                with self.assertRaisesRegex(
                    objc.error, r"cannot find a function: \('NoSuchFunction', b'v'\)"
                ):
                    objc.loadBundleFunctions(bundle, d, functions, False)

                self.assertEqual(len(d), 1)
                self.assertIn(functions[0][0], d)

    def test_parsing_arguments(self):
        with self.assertRaisesRegex(
            TypeError, r"function missing required argument 'bundle' \(pos 1\)"
        ):
            objc.loadBundleFunctions()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            objc.loadBundleFunctions(NoObjectiveC(), {}, [])

        with self.assertRaisesRegex(
            ValueError,
            r"NSInvalidArgumentException - -\[OC_BuiltinPythonUnicode bundlePath\]: unrecognized selector sent to instance",
        ):
            # This exception is suboptimal, but does show that the bridge doesn't crash when an incorrect value is passed.
            objc.loadBundleFunctions("", {}, [])

        with self.assertRaisesRegex(TypeError, "argument 2 must be dict, not int"):
            objc.loadBundleFunctions(self.bundle, 42, [])

        with self.assertRaisesRegex(TypeError, "functionInfo not a sequence"):
            objc.loadBundleFunctions(self.bundle, {}, 42)

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.loadBundleFunctions(self.bundle, {}, [], "hello")

        with self.assertRaisesRegex(TypeError, "item 0 has type int not tuple"):
            objc.loadBundleFunctions(self.bundle, {}, [42])

        with self.assertRaisesRegex(
            TypeError, r"functionInfo\(\) takes at least 2 arguments \(0 given\)"
        ):
            objc.loadBundleFunctions(self.bundle, {}, [()])

        with self.assertRaisesRegex(
            TypeError, r"functionInfo\(\) takes at least 2 arguments \(0 given\)"
        ):
            objc.loadBundleFunctions(None, {}, [()])

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            objc.loadBundleFunctions(self.bundle, {}, [(NoObjectiveC(), b"@")])


class TestFunctionList(TestCase):
    def test_parsing_arguments(self):
        with self.assertRaisesRegex(
            TypeError, r"function missing required argument 'function_list' \(pos 1\)"
        ):
            objc.loadFunctionList()

        with self.assertRaisesRegex(TypeError, "argument 1 must be PyCapsule, not str"):
            objc.loadFunctionList("foo", {}, [])

        with self.assertRaisesRegex(TypeError, "argument 2 must be dict, not int"):
            objc.loadFunctionList(function_list, 42, [])

        with self.assertRaisesRegex(TypeError, "functionInfo not a sequence"):
            objc.loadFunctionList(function_list, {}, 42)

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.loadFunctionList(function_list, {}, [], "hello")

        with self.assertRaisesRegex(TypeError, "item 0 has type int not tuple"):
            objc.loadFunctionList(function_list, {}, [42])

        with self.assertRaisesRegex(
            TypeError, r"functionInfo tuple\(\) takes at least 2 arguments \(0 given\)"
        ):
            objc.loadFunctionList(function_list, {}, [()])

        with self.assertRaisesRegex(
            TypeError, r"functionInfo tuple\(\) takes at least 2 arguments \(0 given\)"
        ):
            objc.loadFunctionList(function_list, {}, [()])

        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.loadFunctionList(function_list, {}, [("foo", "@")])

    def test_invalid_function_signature(self):
        d = {}

        with self.assertRaisesRegex(
            objc.internal_error, "PyObjCRT_SkipTypeSpec: Unhandled type '0x21' !"
        ):
            objc.loadFunctionList(function_list, d, [("makeArrayWithFormat_", b"!")])
        self.assertEqual(d, {})

    def test_missing_function(self):
        d = {}

        with self.assertRaisesRegex(
            objc.error, "cannot find function 'nosuchfunction'"
        ):
            objc.loadFunctionList(function_list, d, [("nosuchfunction", b"v")], False)
        self.assertEqual(d, {})

        objc.loadFunctionList(function_list, d, [("nosuchfunction", b"v")], True)
        self.assertEqual(d, {})
