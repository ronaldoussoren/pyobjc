import SecurityInterface
from PyObjCTools.TestSupport import TestCase


class TestSFAuthorizationViewHelper(SecurityInterface.NSObject):
    def authorizationViewShouldDeauthorize_(self, v):
        return 1


class TestSFAuthorizationView(TestCase):
    def test_constants(self):
        self.assertEqual(SecurityInterface.SFAuthorizationStartupState, 0)
        self.assertEqual(SecurityInterface.SFAuthorizationViewLockedState, 1)
        self.assertEqual(SecurityInterface.SFAuthorizationViewInProgressState, 2)
        self.assertEqual(SecurityInterface.SFAuthorizationViewUnlockedState, 3)

    def test_classes(self):
        SecurityInterface.SFAuthorizationView

    def test_methods(self):
        self.assertResultIsBOOL(SecurityInterface.SFAuthorizationView.updateStatus_)
        self.assertArgIsBOOL(SecurityInterface.SFAuthorizationView.setAutoupdate_, 0)
        self.assertArgIsBOOL(
            SecurityInterface.SFAuthorizationView.setAutoupdate_interval_, 0
        )
        self.assertArgIsBOOL(SecurityInterface.SFAuthorizationView.setEnabled_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFAuthorizationView.isEnabled)
        self.assertResultIsBOOL(SecurityInterface.SFAuthorizationView.authorize_)
        self.assertResultIsBOOL(SecurityInterface.SFAuthorizationView.deauthorize_)

        self.assertResultIsBOOL(
            TestSFAuthorizationViewHelper.authorizationViewShouldDeauthorize_
        )
