from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLARightStore(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.rightForIdentifier_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.saveRight_identifier_completion_, 2, b"v@@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.saveRight_identifier_secret_completion_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.removeRight_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.removeRightForIdentifier_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            LocalAuthentication.LARightStore.removeAllRightsWithCompletion_, 0, b"v@"
        )
