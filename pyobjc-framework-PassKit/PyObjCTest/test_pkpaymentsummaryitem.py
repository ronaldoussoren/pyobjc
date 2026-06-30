from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentSummaryItem(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PassKit.PKPaymentSummaryItemType)
        self.assertEqual(PassKit.PKPaymentSummaryItemTypeFinal, 0)
        self.assertEqual(PassKit.PKPaymentSummaryItemTypePending, 1)
