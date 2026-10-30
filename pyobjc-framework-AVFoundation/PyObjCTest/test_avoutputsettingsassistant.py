import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVOutputSettingsAssistant(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AVFoundation.AVOutputSettingsPreset, str)

    def test_constants(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1280x720, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1920x1080, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset3840x2160, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC1920x1080, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC3840x2160, str)

    @min_os_level("12.1")
    def test_constants12_1(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC7680x4320, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC960x960, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC1440x1440, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC4320x2160, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC4320x4320, str)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetMVHEVC7680x7680, str)
