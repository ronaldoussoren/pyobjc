from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentRequest(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKMerchantCapability3DS, 1 << 0)
        self.assertEqual(PassKit.PKMerchantCapabilityEMV, 1 << 1)
        self.assertEqual(PassKit.PKMerchantCapabilityCredit, 1 << 2)
        self.assertEqual(PassKit.PKMerchantCapabilityDebit, 1 << 3)

        self.assertEqual(PassKit.PKAddressFieldNone, 0)
        self.assertEqual(PassKit.PKAddressFieldPostalAddress, 1 << 0)
        self.assertEqual(PassKit.PKAddressFieldPhone, 1 << 1)
        self.assertEqual(PassKit.PKAddressFieldEmail, 1 << 2)
        self.assertEqual(PassKit.PKAddressFieldName, 1 << 3)
        self.assertEqual(
            PassKit.PKAddressFieldAll,
            PassKit.PKAddressFieldPostalAddress
            | PassKit.PKAddressFieldPhone
            | PassKit.PKAddressFieldEmail
            | PassKit.PKAddressFieldName,
        )

        self.assertEqual(PassKit.PKShippingTypeShipping, 0)
        self.assertEqual(PassKit.PKShippingTypeDelivery, 1)
        self.assertEqual(PassKit.PKShippingTypeStorePickup, 2)
        self.assertEqual(PassKit.PKShippingTypeServicePickup, 3)

        self.assertEqual(PassKit.PKPaymentSummaryItemTypeFinal, 0)
        self.assertEqual(PassKit.PKPaymentSummaryItemTypePending, 1)
