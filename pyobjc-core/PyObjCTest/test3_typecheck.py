from PyObjCTools.TestSupport import *
import objc

class TestPython3Types (TestCase):
    # Add tests here for all metadata and function arguments (when py3k and py2
    # behaviour is different)

    def testSelectorArguments(self):
        self.assertRaises(TypeError, objc.selector, "hello", signature=b"v@:")
        self.assertRaises(TypeError, objc.selector, b"hello", signature="v@:")

    def testSelectorAttributes(self):
        o = objc.lookUpClass('NSObject').alloc().init()

        m = o.description
        self.assertIsInstance(m.selector, bytes)
        self.assertIsInstance(m.signature, bytes)

        meta = m.__metadata__()
        self.assertIsInstance(meta['retval']['type'], bytes)
        for a in meta['arguments']:
            self.assertIsInstance(a['type'], bytes)

    def testFunctionLookup(self):
        NSBundle = objc.lookUpClass('NSBundle')
        bundle = NSBundle.bundleForClass_(NSBundle)

        tab = [
                ( 'NSHomeDirectory', b'@'),
        ]
        d = {}
        objc.loadBundleFunctions(bundle, d, tab)
        self.assertIn('NSHomeDirectory', d)


        tab = [
                ( 'NSHomeDirectory', '@'),
        ]
        self.assertRaises(TypeError, objc.loadBundleFunctions, bundle, d, tab)

        tab = [
                ( b'NSHomeDirectory', b'@'),
        ]
        self.assertRaises(TypeError, objc.loadBundleFunctions, bundle, d, tab)

    def testVariableLookup(self):
        NSBundle = objc.lookUpClass('NSBundle')
        bundle = NSBundle.bundleForClass_(NSBundle)

        tab = [
            ('NSAppleScriptErrorMessage', b'@'),
        ]

        d = {}
        objc.loadBundleVariables(bundle, d, tab)
        self.assertIn('NSAppleScriptErrorMessage', d)



        tab = [
            ('NSAppleScriptErrorMessage', '@'),
        ]

        self.assertRaises(TypeError, objc.loadBundleVariables, bundle, d, tab)

        tab = [
            (b'NSAppleScriptErrorMessage', b'@'),
        ]

        self.assertRaises(TypeError, objc.loadBundleVariables, bundle, d, tab)



if __name__ == "__main__":
    main()
