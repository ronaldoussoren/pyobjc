from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCDeviceHaptics(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(GameController.GCHapticsLocality, str)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameController.GCHapticsLocalityDefault, str)
        self.assertIsInstance(GameController.GCHapticsLocalityAll, str)
        self.assertIsInstance(GameController.GCHapticsLocalityHandles, str)
        self.assertIsInstance(GameController.GCHapticsLocalityLeftHandle, str)
        self.assertIsInstance(GameController.GCHapticsLocalityRightHandle, str)
        self.assertIsInstance(GameController.GCHapticsLocalityTriggers, str)
        self.assertIsInstance(GameController.GCHapticsLocalityLeftTrigger, str)
        self.assertIsInstance(GameController.GCHapticsLocalityRightTrigger, str)

        self.assertIsInstance(GameController.GCHapticDurationInfinite, float)
