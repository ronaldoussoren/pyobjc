from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCDeviceHaptics(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(GameController.GCHapticsLocalityDefault, str)
        self.assertIsInstance(GameController.GCHapticsLocalityAll, str)
        self.assertIsInstance(GameController.GCHapticsLocalityHandles, str)
        self.assertIsInstance(GameController.GCHapticsLocalityLeftHandle, str)
        self.assertIsInstance(GameController.GCHapticsLocalityRightHandle, str)
        self.assertIsInstance(GameController.GCHapticsLocalityTriggers, str)
        self.assertIsInstance(GameController.GCHapticsLocalityLeftTrigger, str)
        self.assertIsInstance(GameController.GCHapticsLocalityRightTrigger, str)

        self.assertIsInstance(GameController.GCHapticDurationInfinite, float)
