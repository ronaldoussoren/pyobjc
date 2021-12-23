import objc
from PyObjCTools.TestSupport import TestCase


class TestPython3Types(TestCase):
    # Add tests here for all metadata and function arguments (when py3k and py2
    # behaviour is different)

    def testSelectorArguments(self):
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.selector(lambda x: None, "hello", signature=b"v@:")
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.selector(lambda x: None, b"hello", signature="v@:")
        with self.assertRaisesRegex(TypeError, "argument 'method' must be callable"):
            objc.selector(42, b"hello", signature=b"v@:")

    def testSelectorAttributes(self):
        o = objc.lookUpClass("NSObject").alloc().init()

        m = o.description
        self.assertIsInstance(m.selector, bytes)
        self.assertIsInstance(m.signature, bytes)

        meta = m.__metadata__()
        self.assertIsInstance(meta["retval"]["type"], bytes)
        for a in meta["arguments"]:
            self.assertIsInstance(a["type"], bytes)

    def testFunctionLookup(self):
        NSBundle = objc.lookUpClass("NSBundle")
        bundle = NSBundle.bundleForClass_(NSBundle)

        tab = [("NSHomeDirectory", b"@")]
        d = {}
        objc.loadBundleFunctions(bundle, d, tab)
        self.assertIn("NSHomeDirectory", d)

        tab = [("NSHomeDirectory", "@")]
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.loadBundleFunctions(bundle, d, tab)

        tab = [(b"NSHomeDirectory", b"@")]
        with self.assertRaisesRegex(TypeError, "functionInfo name not a string"):
            objc.loadBundleFunctions(bundle, d, tab)

    def testVariableLookup(self):
        NSBundle = objc.lookUpClass("NSBundle")
        bundle = NSBundle.bundleForClass_(NSBundle)

        tab = [("NSAppleScriptErrorMessage", b"@")]

        d = {}
        objc.loadBundleVariables(bundle, d, tab)
        self.assertIn("NSAppleScriptErrorMessage", d)

        tab = [("NSAppleScriptErrorMessage", "@")]

        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.loadBundleVariables(bundle, d, tab)

        tab = [(b"NSAppleScriptErrorMessage", b"@")]

        with self.assertRaisesRegex(
            TypeError, r"variableInfo\(\) argument 1 must be str, not bytes"
        ):
            objc.loadBundleVariables(bundle, d, tab)
