from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import GameController


class TestGCInputNames(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
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

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(GameController.GCInputButtonShare, str)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(GameController.GCInputSteeringWheel, str)
        self.assertIsInstance(GameController.GCInputShifter, str)
        self.assertIsInstance(GameController.GCInputPedalAccelerator, str)
        self.assertIsInstance(GameController.GCInputPedalBrake, str)
        self.assertIsInstance(GameController.GCInputPedalClutch, str)
        self.assertIsInstance(GameController.GCInputLeftPaddle, str)
        self.assertIsInstance(GameController.GCInputRightPaddle, str)

    def test_enum_types(self):
        self.assertIsTypedEnum(GameController.GCInputElementName, str)
        self.assertIsTypedEnum(GameController.GCInputButtonName, str)
        self.assertIsTypedEnum(GameController.GCInputAxisName, str)
        self.assertIsTypedEnum(GameController.GCInputDirectionPadName, str)

    @min_sdk_level("13.0")
    def test_protocols(self):
        pass

        # These are compile time only protocols:
        # self.assertProtocolExists("GCPhysicalInputElementName")
        # self.assertProtocolExists("GCButtonElementName")
        # self.assertProtocolExists("GCAxisElementName")
        # self.assertProtocolExists("GCSwitchElementName")
        # self.assertProtocolExists("GCDirectionPadElementName")
