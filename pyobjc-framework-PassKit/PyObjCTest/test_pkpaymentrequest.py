from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKPaymentRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKAddressField)
        self.assertIsEnumType(PassKit.PKMerchantCapability)
        self.assertIsEnumType(PassKit.PKShippingContactEditingMode)
        self.assertIsEnumType(PassKit.PKShippingType)

    def test_constants(self):
        self.assertEqual(PassKit.PKMerchantCapability3DS, 1 << 0)
        self.assertEqual(PassKit.PKMerchantCapabilityEMV, 1 << 1)
        self.assertEqual(PassKit.PKMerchantCapabilityCredit, 1 << 2)
        self.assertEqual(PassKit.PKMerchantCapabilityDebit, 1 << 3)
        self.assertEqual(PassKit.PKMerchantCapabilityInstantFundsOut, 1 << 7)

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

        self.assertEqual(PassKit.PKShippingContactEditingModeAvailable, 1)
        self.assertEqual(PassKit.PKShippingContactEditingModeStorePickup, 2)
        self.assertEqual(
            PassKit.PKShippingContactEditingModeEnabled,
            PassKit.PKShippingContactEditingModeAvailable,
        )

        self.assertIsEnumType(PassKit.PKApplePayLaterAvailability)
        self.assertEqual(PassKit.PKApplePayLaterAvailable, 0)
        self.assertEqual(PassKit.PKApplePayLaterUnavailableItemIneligible, 1)
        self.assertEqual(PassKit.PKApplePayLaterUnavailableRecurringTransaction, 2)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(PassKit.PKPaymentRequest.supportsCouponCode)
        self.assertArgIsBOOL(PassKit.PKPaymentRequest.setSupportsCouponCode_, 0)
