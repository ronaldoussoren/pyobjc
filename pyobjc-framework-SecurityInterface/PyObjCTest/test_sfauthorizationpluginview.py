from PyObjCTools.TestSupport import *

import SecurityInterface

class TestSFAuthorizationPluginView (TestCase):
    def test_constants(self):
        self.assertEqual(SecurityInterface.SFButtonTypeCancel, SecurityInterface.NSCancelButton)
        self.assertEqual(SecurityInterface.SFButtonTypeOK, SecurityInterface.NSOKButton)
        self.assertEqual(SecurityInterface.SFButtonTypeBack, SecurityInterface.SFButtonTypeCancel)
        self.assertEqual(SecurityInterface.SFButtonTypeLogin, SecurityInterface.SFButtonTypeOK)

        self.assertEqual(SecurityInterface.SFViewTypeIdentityAndCredentials, 0)
        self.assertEqual(SecurityInterface.SFViewTypeCredentials, 1)

        self.assertIsInstance(SecurityInterface.SFAuthorizationPluginViewUserNameKey, unicode)
        self.assertIsInstance(SecurityInterface.SFAuthorizationPluginViewUserShortNameKey, unicode)
        self.assertIsInstance(SecurityInterface.SFDisplayViewException, unicode)

    def test_classes(self):
        SecurityInterface.SFAuthorizationPluginView

    def test_methods(self):
        # XXX: initWithCallbacks_andEngineRef_: needs tests that exercise this,
        #      after binding Security framework...

        self.assertArgIsBOOL(SecurityInterface.SFAuthorizationPluginView.setEnabled_, 0)
        self.assertArgIsBOOL(SecurityInterface.SFAuthorizationPluginView.setButton_enabled_, 1)

if __name__ == "__main__":
    main()
