from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureSessionPreset (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetPhoto, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetHigh, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetMedium, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetLow, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset320x240, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset352x288, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset640x480, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset960x540, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset1280x720, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame960x540, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame1280x720, unicode)


if __name__ == "__main__":
    main()
