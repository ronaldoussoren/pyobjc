import StoreKit
from PyObjCTools.TestSupport import TestCase


class TestSKProductDiscount(TestCase):
    def test_enums(self):
        self.assertIsEnumType(StoreKit.SKProductDiscountPaymentMode)
        self.assertEqual(StoreKit.SKProductDiscountPaymentModePayAsYouGo, 0)
        self.assertEqual(StoreKit.SKProductDiscountPaymentModePayUpFront, 1)
        self.assertEqual(StoreKit.SKProductDiscountPaymentModeFreeTrial, 2)

        self.assertIsEnumType(StoreKit.SKProductDiscountType)
        self.assertEqual(StoreKit.SKProductDiscountTypeIntroductory, 0)
        self.assertEqual(StoreKit.SKProductDiscountTypeSubscription, 1)
