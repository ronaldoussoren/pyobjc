from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTkSmartCardATR(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardProtocol)
        self.assertEqual(CryptoTokenKit.TKSmartCardProtocolNone, 0)
        self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT0, 1)
        self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT1, 2)
        self.assertEqual(CryptoTokenKit.TKSmartCardProtocolT15, 1 << 15)
        self.assertEqual(CryptoTokenKit.TKSmartCardProtocolAny, (1 << 16) - 1)

    @min_os_level("10.10")
    def test_methods(self):
        self.assertArgIsBlock(CryptoTokenKit.TKSmartCardATR.initWithSource_, 0, b"i@")
