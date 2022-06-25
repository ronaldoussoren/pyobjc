from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import CryptoTokenKit


class TestTKTokenHelper(CryptoTokenKit.NSObject):
    def tokenSession_beginAuthForOperation_constraint_error_(self, s, o, c, e):
        return 1

    def tokenSession_supportsOperation_usingKey_algorithm_(self, s, o, k, a):
        return 1

    def tokenSession_signData_usingKey_algorithm_error_(self, s, d, k, a, e):
        return 1

    def tokenSession_decryptData_usingKey_algorithm_error_(self, s, d, k, a, e):
        return 1

    def tokenSession_performKeyExchangeWithPublicKey_usingKey_algorithm_parameters_error_(
        self, s, pk, k, a, p, e
    ):
        return 1

    def token_createSessionWithError_(self, t, e):
        return 1

    def tokenDriver_tokenForConfiguration_error_(self, a, b, c):
        pass


class TestTKToken(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CryptoTokenKit.TKTokenOperation)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(CryptoTokenKit.TKTokenOperationNone, 0)
        self.assertEqual(CryptoTokenKit.TKTokenOperationReadData, 1)
        self.assertEqual(CryptoTokenKit.TKTokenOperationSignData, 2)
        self.assertEqual(CryptoTokenKit.TKTokenOperationDecryptData, 3)
        self.assertEqual(CryptoTokenKit.TKTokenOperationPerformKeyExchange, 4)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeyAlgorithm.isAlgorithm_)
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeyAlgorithm.supportsAlgorithm_)

        self.assertResultIsBOOL(CryptoTokenKit.TKTokenAuthOperation.finishWithError_)
        self.assertArgIsOut(CryptoTokenKit.TKTokenAuthOperation.finishWithError_, 0)

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("TKTokenSessionDelegate")
        self.assertProtocolExists("TKTokenDelegate")
        self.assertProtocolExists("TKTokenDriverDelegate")

    @min_sdk_level("10.12")
    def testProtocolMethods(self):
        self.assertArgHasType(
            TestTKTokenHelper.tokenSession_beginAuthForOperation_constraint_error_,
            3,
            b"o^@",
        )
        self.assertResultIsBOOL(
            TestTKTokenHelper.tokenSession_supportsOperation_usingKey_algorithm_
        )
        self.assertArgHasType(
            TestTKTokenHelper.tokenSession_signData_usingKey_algorithm_error_, 4, b"o^@"
        )
        self.assertArgHasType(
            TestTKTokenHelper.tokenSession_decryptData_usingKey_algorithm_error_,
            4,
            b"o^@",
        )
        self.assertArgHasType(
            TestTKTokenHelper.tokenSession_performKeyExchangeWithPublicKey_usingKey_algorithm_parameters_error_,
            5,
            b"o^@",
        )

        self.assertArgHasType(
            TestTKTokenHelper.token_createSessionWithError_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestTKTokenHelper.tokenDriver_tokenForConfiguration_error_, 2, b"o^@"
        )
