import SecurityInterface
import Security
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
        rights = [
            Security.AuthorizationItem(
                name=Security.kAuthorizationRightExecute,
                valueLength=11,
                value=b"/usr/bin/id",
                flags=0,
            ),
            Security.AuthorizationItem(
                name=Security.kAuthorizationEnvironmentPrompt,
                valueLength=0,
                value=None,
                flags=0,
            ),
        ]

        view.setAuthorizationRights_(rights)

        rights = view.authorizationRights()
        self.assertEqual(
            rights,
            (
                (
                    Security.AuthorizationItem(
                        name=b"system.privilege.admin",
                        valueLength=11,
                        value=b"/usr/bin/id",
                        flags=0,
                    ),
                    (
                        Security.AuthorizationItem(
                            name=b"prompt", valueLength=0, value=None, flags=0
                        )
                    ),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            view.setAuthorizationRights_(42)

        with self.assertRaisesRegex(TypeError, r"items\[0\] is not a sequence"):
            view.setAuthorizationRights_([42])

        with self.assertRaisesRegex(
            TypeError, r"items\[0\] is not a sequence of 4 items"
        ):
            view.setAuthorizationRights_([()])

        with self.assertRaisesRegex(TypeError, r"items\[0\].name is not a byte string"):
            view.setAuthorizationRights_([("key", 5, b"value", 0)])

        with self.assertRaisesRegex(
            TypeError, r"items\[0\].valueLength is not an integer"
        ):
            view.setAuthorizationRights_([(b"key", "5", b"value", 0)])

        with self.assertRaisesRegex(
            TypeError, r"items\[0\].value is not a byte string of length 5"
        ):
            view.setAuthorizationRights_([(b"key", 5, "value", 0)])

        with self.assertRaisesRegex(
            TypeError, r"items\[0\].value is None, valueLength != 0"
        ):
            view.setAuthorizationRights_([(b"key", 5, None, 0)])

        with self.assertRaisesRegex(
            TypeError, r"items\[0\].value is not a byte string of length 5"
        ):
            view.setAuthorizationRights_([(b"key", 5, "val", 0)])

        with self.assertRaisesRegex(TypeError, r"items\[0\].flags is not an integer"):
            view.setAuthorizationRights_([(b"key", 5, b"value", "0")])
