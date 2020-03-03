import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVOutputSettingsAssistent(TestCase):
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

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVOutputSettingsPresetHEVC1920x1080WithAlpha, str
        )
        self.assertIsInstance(
            AVFoundation.AVOutputSettingsPresetHEVC3840x2160WithAlpha, str
        )
