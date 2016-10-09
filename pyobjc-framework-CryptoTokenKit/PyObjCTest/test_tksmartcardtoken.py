import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CryptoTokenKit

    class TestTKSmartCardTokenHelper (CryptoTokenKit.NSObject):
        def tokenDriver_createTokenForSmartCard_AID_error_(self, d, sc, a, e):
            return 1

    class TestTKSmartCardToken (TestCase):
        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('TKSmartCardTokenDriverDelegate')

        @min_sdk_level('10.12')
        def testMethods(self):
            self.assertArgHasType(TestTKSmartCardTokenHelper.tokenDriver_createTokenForSmartCard_AID_error_, 3, b'o^@')


if __name__ == "__main__":
    main()
