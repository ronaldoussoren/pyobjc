from PyObjCTools.TestSupport import TestCase
import Intents


class TestINPaymentMethodTypes(TestCase):
    def test_constants(self):
        self.assertEqual(Intents.INPaymentMethodTypeUnknown, 0)
        self.assertEqual(Intents.INPaymentMethodTypeChecking, 1)
        self.assertEqual(Intents.INPaymentMethodTypeSavings, 2)
        self.assertEqual(Intents.INPaymentMethodTypeBrokerage, 3)
        self.assertEqual(Intents.INPaymentMethodTypeDebit, 4)
        self.assertEqual(Intents.INPaymentMethodTypeCredit, 5)
        self.assertEqual(Intents.INPaymentMethodTypePrepaid, 6)
        self.assertEqual(Intents.INPaymentMethodTypeStore, 7)
        self.assertEqual(Intents.INPaymentMethodTypeApplePay, 8)
