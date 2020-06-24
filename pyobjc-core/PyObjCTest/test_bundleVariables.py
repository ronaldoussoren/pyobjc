import objc
from PyObjCTools.TestSupport import TestCase

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
