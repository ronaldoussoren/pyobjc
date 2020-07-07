from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCInputNames(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(GameController.GCInputButtonA, str)
        self.assertIsInstance(GameController.GCInputButtonB, str)
        self.assertIsInstance(GameController.GCInputButtonX, str)
        self.assertIsInstance(GameController.GCInputButtonY, str)

        self.assertIsInstance(GameController.GCInputDirectionPad, str)
        self.assertIsInstance(GameController.GCInputLeftThumbstick, str)
        self.assertIsInstance(GameController.GCInputRightThumbstick, str)

        self.assertIsInstance(GameController.GCInputLeftShoulder, str)
        self.assertIsInstance(GameController.GCInputRightShoulder, str)
        self.assertIsInstance(GameController.GCInputLeftTrigger, str)
        self.assertIsInstance(GameController.GCInputRightTrigger, str)
        self.assertIsInstance(GameController.GCInputLeftThumbstickButton, str)
        self.assertIsInstance(GameController.GCInputRightThumbstickButton, str)

        self.assertIsInstance(GameController.GCInputButtonHome, str)
        self.assertIsInstance(GameController.GCInputButtonMenu, str)
        self.assertIsInstance(GameController.GCInputButtonOptions, str)

        self.assertIsInstance(GameController.GCInputXboxPaddleOne, str)
        self.assertIsInstance(GameController.GCInputXboxPaddleTwo, str)
        self.assertIsInstance(GameController.GCInputXboxPaddleThree, str)
        self.assertIsInstance(GameController.GCInputXboxPaddleFour, str)

        self.assertIsInstance(GameController.GCInputDualShockTouchpadOne, str)
        self.assertIsInstance(GameController.GCInputDualShockTouchpadTwo, str)
        self.assertIsInstance(GameController.GCInputDualShockTouchpadButton, str)
