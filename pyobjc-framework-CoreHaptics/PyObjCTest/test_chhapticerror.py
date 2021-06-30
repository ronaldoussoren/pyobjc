import CoreHaptics
from PyObjCTools.TestSupport import TestCase


class TestCHHapticErrors(TestCase):
    def test_constants(self):
        self.assertEqual(CoreHaptics.CHHapticErrorCodeEngineNotRunning, -4805)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeOperationNotPermitted, -4806)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeEngineStartTimeout, -4808)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeNotSupported, -4809)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeServerInitFailed, -4810)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeServerInterrupted, -4811)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidPatternPlayer, -4812)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidPatternData, -4813)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidPatternDictionary, -4814)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidAudioSession, -4815)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidEngineParameter, -4816)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidParameterType, -4820)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidEventType, -4821)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidEventTime, -4822)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidEventDuration, -4823)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidAudioResource, -4824)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeResourceNotAvailable, -4825)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeBadEventEntry, -4830)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeBadParameterEntry, -4831)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInvalidTime, -4840)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeFileNotFound, -4851)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeInsufficientPower, -4897)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeUnknownError, -4898)
        self.assertEqual(CoreHaptics.CHHapticErrorCodeMemoryError, -4899)
