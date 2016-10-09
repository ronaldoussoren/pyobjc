import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CryptoTokenKit

    class TestTKError (TestCase):
        def testConstants(self):
            self.assertIsInstance(CryptoTokenKit.TKErrorDomain, unicode)

            self.assertEqual(CryptoTokenKit.TKErrorCodeNotImplemented, -1)
            self.assertEqual(CryptoTokenKit.TKErrorCodeCommunicationError, -2)
            self.assertEqual(CryptoTokenKit.TKErrorCodeCorruptedData, -3)
            self.assertEqual(CryptoTokenKit.TKErrorCodeCanceledByUser, -4)
            self.assertEqual(CryptoTokenKit.TKErrorAuthenticationFailed, -5)
            self.assertEqual(CryptoTokenKit.TKErrorCodeAuthenticationFailed, -5)
            self.assertEqual(CryptoTokenKit.TKErrorObjectNotFound, -6)
            self.assertEqual(CryptoTokenKit.TKErrorCodeObjectNotFound, -6)
            self.assertEqual(CryptoTokenKit.TKErrorTokenNotFound, -7)
            self.assertEqual(CryptoTokenKit.TKErrorCodeTokenNotFound, -7)
            self.assertEqual(CryptoTokenKit.TKErrorCodeBadParameter, -8)
            self.assertEqual(CryptoTokenKit.TKErrorCodeAuthenticationNeeded, -9)


if __name__ == "__main__":
    main()
