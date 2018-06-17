from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVOutputSettingsAssistant (TestCase):
    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset640x480, unicode)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset960x540, unicode)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1280x720, unicode)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset1920x1080, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPreset3840x2160, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC1920x1080, unicode)
        self.assertIsInstance(AVFoundation.AVOutputSettingsPresetHEVC3840x2160, unicode)


if __name__ == "__main__":
    main()
