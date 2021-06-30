from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentSummaryItem(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKPaymentSummaryItemTypeFinal, 0)
        self.assertEqual(PassKit.PKPaymentSummaryItemTypePending, 1)
