from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLARight(TestCase):
    def test_constants(self):
        self.assertIsEnumType(LocalAuthentication.LARightState)
        self.assertEqual(LocalAuthentication.LARightStateUnknown, 0)
        self.assertEqual(LocalAuthentication.LARightStateAuthorizing, 1)
        self.assertEqual(LocalAuthentication.LARightStateAuthorized, 2)
        self.assertEqual(LocalAuthentication.LARightStateNotAuthorized, 3)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LARight.authorizeWithLocalizedReason_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARight.checkCanAuthorizeWithCompletion_, 0, b"v@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARight.deauthorizeWithCompletion_, 0, b"v"
        )
