from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKSecureElementPass(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKSecureElementPassActivationState)

    def test_constants(self):
        self.assertEqual(PassKit.PKSecureElementPassActivationStateActivated, 0)
        self.assertEqual(
            PassKit.PKSecureElementPassActivationStateRequiresActivation, 1
        )
        self.assertEqual(PassKit.PKSecureElementPassActivationStateActivating, 2)
        self.assertEqual(PassKit.PKSecureElementPassActivationStateSuspended, 3)
        self.assertEqual(PassKit.PKSecureElementPassActivationStateDeactivated, 4)
