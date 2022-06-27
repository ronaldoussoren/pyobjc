from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAPublicKey(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LAPublicKey.exportBytesWithCompletion_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LAPublicKey.encryptData_secKeyAlgorithm_completion_,
            2,
            b"v@@",
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAPublicKey.canEncryptUsingSecKeyAlgorithm_
        )
        self.assertArgIsBlock(
            LocalAuthentication.LAPublicKey.verifyData_signature_secKeyAlgorithm_completion_,
            3,
            b"v@",
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAPublicKey.canVerifyUsingSecKeyAlgorithm_
        )
