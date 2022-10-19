from PyObjCTools.TestSupport import TestCase

import SafetyKit
import objc


class TestSAEmergencyResponseManagerHelper(SafetyKit.NSObject):
    def emergencyResponseManager_didUpdateVoiceCallStatus_(self, a, b):
        pass


class TestSAEmergencyResponseManager(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SAEmergencyResponseDelegate")

    def test_constants(self):
        self.assertIsEnumType(SafetyKit.SAEmergencyResponseManagerVoiceCallStatus)
        self.assertEqual(SafetyKit.SAEmergencyResponseManagerVoiceCallStatusDialing, 0)
        self.assertEqual(SafetyKit.SAEmergencyResponseManagerVoiceCallStatusActive, 1)
        self.assertEqual(
            SafetyKit.SAEmergencyResponseManagerVoiceCallStatusDisconnected, 2
        )
        self.assertEqual(SafetyKit.SAEmergencyResponseManagerVoiceCallStatusFailed, 3)

    def test_methods(self):
        self.assertArgIsBlock(
            SafetyKit.SAEmergencyResponseManager.dialVoiceCallToPhoneNumber_completionHandler_,
            1,
            b"vZ@",
        )

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestSAEmergencyResponseManagerHelper.emergencyResponseManager_didUpdateVoiceCallStatus_,
            1,
            objc._C_NSInteger,
        )
