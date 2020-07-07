from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentPass(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKPaymentPassActivationStateActivated, 0)
        self.assertEqual(PassKit.PKPaymentPassActivationStateRequiresActivation, 1)
        self.assertEqual(PassKit.PKPaymentPassActivationStateActivating, 2)
        self.assertEqual(PassKit.PKPaymentPassActivationStateSuspended, 3)
        self.assertEqual(PassKit.PKPaymentPassActivationStateDeactivated, 4)
