from PyObjCTools.TestSupport import TestCase

import SafetyKit


class TestSACrashDetectionEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SafetyKit.SACrashDetectionEventResponse)
        self.assertEqual(SafetyKit.SACrashDetectionEventResponseAttempted, 0)
        self.assertEqual(SafetyKit.SACrashDetectionEventResponseDisabled, 1)
