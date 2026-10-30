import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVCaptureSessionPreset(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AVFoundation.AVCaptureSessionPreset, str)

    def test_constants(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetPhoto, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetHigh, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetMedium, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetLow, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset320x240, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset352x288, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset1280x720, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame1280x720, str)
