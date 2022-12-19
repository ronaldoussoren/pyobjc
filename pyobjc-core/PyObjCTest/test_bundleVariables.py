import objc
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_object_proxy import NoObjectiveC

from . import fnd as Foundation


class TestBundleVariables(TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testStrings(self):
        d = {}
        objc.loadBundleVariables(
            self.bundle,
            d,
            [
                ("NSAppleScriptErrorMessage", b"@"),
                ("NSBundleDidLoadNotification", b"@"),
            ],
        )

        self.assertIn("NSBundleDidLoadNotification", d)
        self.assertIn("NSAppleScriptErrorMessage", d)

        self.assertIsInstance(d["NSAppleScriptErrorMessage"], objc.pyobjc_unicode)
        self.assertIsInstance(d["NSBundleDidLoadNotification"], objc.pyobjc_unicode)

    def testSimple(self):
        d = {}
        objc.loadBundleVariables(
            self.bundle,
            d,
            [
                ("NSDebugEnabled", objc._C_NSBOOL),
                ("NSFoundationVersionNumber", objc._C_DBL),
            ],
        )

        self.assertIn("NSDebugEnabled", d)
        self.assertIn("NSFoundationVersionNumber", d)

        self.assertIsInstance(d["NSFoundationVersionNumber"], float)
        self.assertIsInstance(d["NSDebugEnabled"], int)

    def test_missing(self):
        d = {}
        objc.loadBundleVariables(
            self.bundle,
            d,
            [
                ("NSFoundationVersionNumber", objc._C_DBL),
                ("NoSuchVariable", objc._C_NSBOOL),
            ],
        )
        self.assertEqual(len(d), 1)
        self.assertIn("NSFoundationVersionNumber", d)

        d = {}
        with self.assertRaisesRegex(objc.error, "cannot find a variable"):
            objc.loadBundleVariables(
                self.bundle,
                d,
                [
                    ("NSDebugEnabled", objc._C_NSBOOL),
                    ("NoSuchVariable", objc._C_NSBOOL),
                    ("NSFoundationVersionNumber", objc._C_DBL),
                ],
                False,
            )
        self.assertEqual(len(d), 1)
        self.assertIn("NSDebugEnabled", d)

    def test_parsing_arguments(self):
        with self.assertRaisesRegex(
            TypeError, r"function missing required argument 'bundle' \(pos 1\)"
        ):
            objc.loadBundleVariables()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            objc.loadBundleVariables(NoObjectiveC(), {}, [])

        with self.assertRaisesRegex(
            ValueError,
            r"NSInvalidArgumentException - -\[OC_BuiltinPythonUnicode bundlePath\]: unrecognized selector sent to instance",
        ):
            # This exception is suboptimal, but does show that the bridge doesn't crash when an incorrect value is passed.
            objc.loadBundleVariables("", {}, [])

        with self.assertRaisesRegex(TypeError, "argument 2 must be dict, not int"):
            objc.loadBundleVariables(self.bundle, 42, [])

        with self.assertRaisesRegex(TypeError, "variableInfo not a sequence"):
            objc.loadBundleVariables(self.bundle, {}, 42)

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.loadBundleVariables(self.bundle, {}, [], "hello")

        with self.assertRaisesRegex(TypeError, "item 0 has type int not tuple"):
            objc.loadBundleVariables(self.bundle, {}, [42])

        with self.assertRaisesRegex(
            TypeError, r"variableInfo\(\) takes exactly 2 arguments \(0 given\)"
        ):
            objc.loadBundleVariables(self.bundle, {}, [()])

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            objc.loadBundleVariables(self.bundle, {}, [(NoObjectiveC(), b"@")])


class TestSpecialVariables(TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

        g = {}
        objc.loadBundleFunctions(
            self.bundle, g, [("CFStringGetTypeID", objc._C_NSUInteger)]
        )

        self.cfstring_typeid = g["CFStringGetTypeID"]()

    def test_parsing_arguments(self):
        with self.assertRaisesRegex(
            TypeError, r"function missing required argument 'bundle' \(pos 1\)"
        ):
            objc.loadSpecialVar()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            objc.loadSpecialVar(NoObjectiveC(), {}, 42, "hello")

        with self.assertRaisesRegex(
            ValueError,
            r"NSInvalidArgumentException - -\[OC_BuiltinPythonUnicode bundlePath\]: unrecognized selector sent to instance",
        ):
            # This exception is suboptimal, but does show that the bridge doesn't crash when an incorrect value is passed.
            objc.loadSpecialVar("", {}, 42, "hello")

        with self.assertRaisesRegex(TypeError, "argument 2 must be dict, not int"):
            objc.loadSpecialVar(self.bundle, 42, 42, "hello")

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.loadSpecialVar(self.bundle, {}, "42", "hello")

        with self.assertRaisesRegex(TypeError, "variable name not a string"):
            objc.loadSpecialVar(self.bundle, {}, 42, 0)

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.loadSpecialVar(self.bundle, {}, 42, "hello", "world")

    def test_existing_value(self):
        g = {}
        objc.loadSpecialVar(self.bundle, g, self.cfstring_typeid, "NSCocoaErrorDomain")
        self.assertIsInstance(g["NSCocoaErrorDomain"], objc.lookUpClass("NSString"))

    def test_missing_value(self):
        g = {}
        objc.loadSpecialVar(self.bundle, g, self.cfstring_typeid, "NSCocoaErrorDomainX")
        self.assertEqual(g, {})

        with self.assertRaisesRegex(objc.error, "cannot find a variable"):
            objc.loadSpecialVar(
                self.bundle, g, self.cfstring_typeid, "NSCocoaErrorDomainX", False
            )

        self.assertEqual(g, {})
