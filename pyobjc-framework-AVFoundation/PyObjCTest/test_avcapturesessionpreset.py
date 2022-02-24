import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureSessionPreset(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVCaptureSessionPreset, str)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetPhoto, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetHigh, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetMedium, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetLow, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset320x240, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset352x288, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset1280x720, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame1280x720, str)
