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

    def test_protocol_methods(self):
        # Informal protocol
        self.assertResultIsBOOL(
            TestSFAuthorizationViewHelper.authorizationViewShouldDeauthorize_
        )

    def test_manual(self):
        view = SecurityInterface.SFAuthorizationView.alloc().initWithFrame_(
            ((0, 0), (300, 300))
        )
        self.assertIsInstance(view, SecurityInterface.SFAuthorizationView)

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            view.authorizationRights(1)

        rights = view.authorizationRights()
        self.assertIs(rights, None)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            view.setAuthorizationRights_(None, 1)

        view.setAuthorizationRights_(None)
