import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAnimation(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVLayerVideoGravity, str)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCoreAnimationBeginTimeAtZero, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspect, str)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspectFill, str)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResize, str)
