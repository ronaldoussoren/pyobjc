import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CryptoTokenKit

    class TestTkSmartCardATR (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(CryptoTokenKit.TKSmartCardATRInterfaceGroup, objc.objc_class)
            self.assertIsInstance(CryptoTokenKit.TKSmartCardATR, objc.objc_class)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBlock(CryptoTokenKit.TKSmartCardATR.initWithSource_, 0, b"i@")

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(CryptoTokenKit.TKSmartCardProtocolNone, 0)
            self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT0, 1)
            self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT1, 2)
            self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT15, 1 << 15)
            self.assertEqual(CryptoTokenKit.TKSmartCardProtocolAny, (1 << 16) - 1)


if __name__ == "__main__":
    main()
