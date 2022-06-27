from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAPrivateKey(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LAPrivateKey.signData_secKeyAlgorithm_completion_,
            2,
            b"v@@",
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAPrivateKey.canSignUsingSecKeyAlgorithm_
        )
        self.assertArgIsBlock(
            LocalAuthentication.LAPrivateKey.decryptData_secKeyAlgorithm_completion_,
            2,
            b"v@@",
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAPrivateKey.canDecryptUsingSecKeyAlgorithm_
        )
        self.assertArgIsBlock(
            LocalAuthentication.LAPrivateKey.exchangeKeysWithPublicKey_secKeyAlgorithm_secKeyParameters_completion_,
            3,
            b"v@@",
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAPrivateKey.canExchangeKeysUsingSecKeyAlgorithm_
        )
