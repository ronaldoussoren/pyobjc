from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentMethod(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKPaymentMethodType)

    def test_constants(self):
        self.assertEqual(PassKit.PKPaymentMethodTypeUnknown, 0)
        self.assertEqual(PassKit.PKPaymentMethodTypeDebit, 1)
        self.assertEqual(PassKit.PKPaymentMethodTypeCredit, 2)
        self.assertEqual(PassKit.PKPaymentMethodTypePrepaid, 3)
        self.assertEqual(PassKit.PKPaymentMethodTypeStore, 4)
        self.assertEqual(PassKit.PKPaymentMethodTypeEMoney, 5)
