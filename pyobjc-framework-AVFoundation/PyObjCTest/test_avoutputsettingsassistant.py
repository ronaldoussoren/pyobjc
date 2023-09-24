import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVOutputSettingsAssistant(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVOutputSettingsPreset, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1280x720, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1920x1080, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset3840x2160, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC1920x1080, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC3840x2160, str)

    @min_os_level("12.1")
    def testConstants12_1(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC7680x4320, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC960x960, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC1440x1440, str)
