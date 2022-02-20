from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPass(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKPassType)

    def test_constants(self):
        self.assertEqual(PassKit.PKPassTypeBarcode, 0)
        self.assertEqual(PassKit.PKPassTypeSecureElement, 1)
        self.assertEqual(PassKit.PKPassTypePayment, 1)

    def test_methods(self):
        self.assertResultIsBOOL(PassKit.PKPass.isRemotePass)
