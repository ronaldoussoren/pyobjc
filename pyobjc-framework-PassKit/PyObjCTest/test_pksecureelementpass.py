from PyObjCTools.TestSupport import TestCase, min_os_level

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

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(PassKit.PKSecureElementPass.isProvisioningAvailable)
