import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureReactions(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(AVFoundation.AVCaptureReactionType, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeThumbsUp, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeThumbsDown, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeBalloons, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeHeart, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeFireworks, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeRain, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeConfetti, str)
        self.assertIsInstance(AVFoundation.AVCaptureReactionTypeLasers, str)

    @min_os_level("14.0")
    def test_functions14_0(self):
        AVFoundation.AVCaptureReactionSystemImageNameForType
