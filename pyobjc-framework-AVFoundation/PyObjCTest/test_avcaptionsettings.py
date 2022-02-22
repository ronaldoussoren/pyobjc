import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptionSettings(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVCaptionSettingsKey, str)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(AVFoundation.AVCaptionMediaTypeKey, str)
        self.assertIsInstance(AVFoundation.AVCaptionMediaSubTypeKey, str)
        self.assertIsInstance(AVFoundation.AVCaptionTimeCodeFrameDurationKey, str)
        self.assertIsInstance(AVFoundation.AVCaptionUseDropFrameTimeCodeKey, str)
