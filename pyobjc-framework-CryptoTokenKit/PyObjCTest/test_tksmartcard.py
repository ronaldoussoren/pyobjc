import objc

from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTKSmartCard(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardPINCharset)
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardPINCompletion)
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardPINConfirmation)
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardPINEncoding)
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardPINJustification)
        self.assertIsEnumType(CryptoTokenKit.TKSmartCardSlotState)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(CryptoTokenKit.TKSmartCardSlotManager, objc.objc_class)
        self.assertIsInstance(CryptoTokenKit.TKSmartCardSlot, objc.objc_class)
        self.assertIsInstance(CryptoTokenKit.TKSmartCard, objc.objc_class)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCardSlotManager.getSlotWithName_reply_, 1, b"v@"
        )

        self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.valid)
        self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.sensitive)
        self.assertArgIsBOOL(CryptoTokenKit.TKSmartCard.setSensitive_, 0)
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCard.beginSessionWithReply_,
            0,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCard.transmitRequest_reply_, 1, b"v@@"
        )
        self.assertResultIsBOOL(CryptoTokenKit.TKSmartCard.useExtendedLength)
        self.assertArgIsBOOL(CryptoTokenKit.TKSmartCard.setUseExtendedLength_, 0)
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCard.sendIns_p1_p2_data_le_reply_, 5, b"v@S@"
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCardUserInteraction.runWithReply_, 0, b"vZ@"
        )
        self.assertResultIsBOOL(CryptoTokenKit.TKSmartCardUserInteraction.cancel)

        self.assertResultIsBOOL(
            CryptoTokenKit.TKSmartCardUserInteractionForConfirmation.result
        )
        self.assertArgIsBOOL(
            CryptoTokenKit.TKSmartCardUserInteractionForConfirmation.setResult_, 0
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            CryptoTokenKit.TKSmartCard.inSessionWithError_executeBlock_
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCard.inSessionWithError_executeBlock_, 0
        )
        self.assertArgIsBlock(
            CryptoTokenKit.TKSmartCard.inSessionWithError_executeBlock_, 1, b"Zo^@"
        )

        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCard.sendIns_p1_p2_data_le_sw_error_, 5
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCard.sendIns_p1_p2_data_le_sw_error_, 6
        )
