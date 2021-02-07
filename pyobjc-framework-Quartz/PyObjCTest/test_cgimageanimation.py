from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc

CGImageSourceAnimationBlock = b"vl@o^" + objc._C_BOOL


class TestCGImageAnimation(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.kCGImageAnimationStatus_ParameterError, -22140)
        self.assertEqual(Quartz.kCGImageAnimationStatus_CorruptInputImage, -22141)
        self.assertEqual(Quartz.kCGImageAnimationStatus_UnsupportedFormat, -22142)
        self.assertEqual(Quartz.kCGImageAnimationStatus_IncompleteInputImage, -22143)
        self.assertEqual(Quartz.kCGImageAnimationStatus_AllocationFailure, -22144)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Quartz.kCGImageAnimationStartIndex, str)
        self.assertIsInstance(Quartz.kCGImageAnimationDelayTime, str)
        self.assertIsInstance(Quartz.kCGImageAnimationLoopCount, str)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertArgIsBlock(
            Quartz.CGAnimateImageAtURLWithBlock, 2, CGImageSourceAnimationBlock
        )
        self.assertArgIsBlock(
            Quartz.CGAnimateImageDataWithBlock, 2, CGImageSourceAnimationBlock
        )
