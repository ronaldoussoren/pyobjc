import objc
import Foundation
import unittest

class TestBundleVariables (unittest.TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testStrings(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                ('NSAppleScriptErrorMessage', '@'),
                ('NSBundleDidLoadNotification', '@'),
            ])

        self.assert_('NSBundleDidLoadNotification' in d)
        self.assert_('NSAppleScriptErrorMessage' in d)

        self.assert_(isinstance(d['NSAppleScriptErrorMessage'], objc.pyobjc_unicode))
        self.assert_(isinstance(d['NSBundleDidLoadNotification'], objc.pyobjc_unicode))

    def testSimple(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                ('NSDebugEnabled', objc._C_NSBOOL),
                ('NSFoundationVersionNumber', objc._C_DBL),
            ])

        self.assert_('NSDebugEnabled' in d)
        self.assert_('NSFoundationVersionNumber' in d)

        self.assert_(isinstance(d['NSFoundationVersionNumber'], float))
        self.assert_(isinstance(d['NSDebugEnabled'], int))


if __name__ == "__main__":
    unittest.main()


