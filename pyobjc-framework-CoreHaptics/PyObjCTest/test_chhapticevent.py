import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestCHHapticEvent(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(CoreHaptics.CHHapticEventType, str)

    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeHapticTransient, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeHapticContinuous, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeAudioContinuous, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeAudioCustom, str)
