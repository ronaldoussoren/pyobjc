import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CryptoTokenKit

    class TestTKSmartCard (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(CryptoTokenKit.TKSmartCardSlotManager, objc.objc_class)
            self.assertIsInstance(CryptoTokenKit.TKSmartCardSlot, objc.objc_class)
            self.assertIsInstance(CryptoTokenKit.TKSmartCard, objc.objc_class)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBlock(CryptoTokenKit.TKSmartCardSlotManager.getSlotWithName_reply_, 1, b"v@")

            self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.valid)
            self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.sensitive)
            self.assertArgIsBOOL(CryptoTokenKit.TKSmartCard.setSensitive_, 0)
            self.assertArgIsBlock(CryptoTokenKit.TKSmartCard.beginSessionWithReply_, 0, b"v" + objc._C_NSBOOL + b"@")
            self.assertArgIsBlock(CryptoTokenKit.TKSmartCard.transmitRequest_reply_, 1, b"v@@")
            self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.useExtendedLength)
            self.assertArgIsBOOL(CryptoTokenKit.TKSmartCard.setUseExtendedLength_, 0)
            self.assertArgIsBlock(CryptoTokenKit.TKSmartCard.sendIns_p1_p2_data_le_reply_, 5, b"v@S@")

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotStateMissing, 0)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotStateEmpty, 1)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotStateProbing, 2)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotStateMuteCard, 3)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotStateValidCard, 4)

            # Deprecated:
            self.assertEqual(CryptoTokenKit.TKSmartCardNoSlot, 0)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotEmpty, 1)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotProbing, 2)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotMuteCard, 3)
            self.assertEqual(CryptoTokenKit.TKSmartCardSlotValidCard, 4)




if __name__ == "__main__":
    main()
