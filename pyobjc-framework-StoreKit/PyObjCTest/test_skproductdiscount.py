import StoreKit
from PyObjCTools.TestSupport import TestCase


class TestSKProductDiscount(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(StoreKit.SKProductDiscountPaymentMode)
        self.assertIsEnumType(StoreKit.SKProductDiscountType)

    def test_constants(self):
        self.assertEqual(StoreKit.SKProductDiscountPaymentModePayAsYouGo, 0)
        self.assertEqual(StoreKit.SKProductDiscountPaymentModePayUpFront, 1)
        self.assertEqual(StoreKit.SKProductDiscountPaymentModeFreeTrial, 2)

        self.assertEqual(StoreKit.SKProductDiscountTypeIntroductory, 0)
        self.assertEqual(StoreKit.SKProductDiscountTypeSubscription, 1)
