import CoreHaptics
from PyObjCTools.TestSupport import *


class TestCHHapticEvent(TestCase):
    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeHapticTransient, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeHapticContinuous, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeAudioContinuous, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventTypeAudioCustom, unicode)
