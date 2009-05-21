import objc
import PyObjCTest.fnd as Foundation
from PyObjCTools.TestSupport import *

class TestBundleVariables (TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testStrings(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                (u'NSAppleScriptErrorMessage', '@'),
                (u'NSBundleDidLoadNotification', '@'),
            ])

        self.assert_(u'NSBundleDidLoadNotification' in d)
        self.assert_(u'NSAppleScriptErrorMessage' in d)

        self.assert_(isinstance(d[u'NSAppleScriptErrorMessage'], objc.pyobjc_unicode))
        self.assert_(isinstance(d[u'NSBundleDidLoadNotification'], objc.pyobjc_unicode))

    def testSimple(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                (u'NSDebugEnabled', objc._C_NSBOOL),
                (u'NSFoundationVersionNumber', objc._C_DBL),
            ])

        self.assert_(u'NSDebugEnabled' in d)
        self.assert_(u'NSFoundationVersionNumber' in d)

        self.assert_(isinstance(d[u'NSFoundationVersionNumber'], float))
        self.assert_(isinstance(d[u'NSDebugEnabled'], int))


if __name__ == "__main__":
    main()


