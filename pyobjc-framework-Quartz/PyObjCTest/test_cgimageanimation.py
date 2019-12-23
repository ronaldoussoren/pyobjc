from PyObjCTools.TestSupport import *
from Quartz import *

CGImageSourceAnimationBlock = b"vl@o^" + objc._C_BOOL


class TestCGImageAnimation(TestCase):
    def test_constants(self):
        self.assertEqual(kCGImageAnimationStatus_ParameterError, -22140)
        self.assertEqual(kCGImageAnimationStatus_CorruptInputImage, -22141)
        self.assertEqual(kCGImageAnimationStatus_UnsupportedFormat, -22142)
        self.assertEqual(kCGImageAnimationStatus_IncompleteInputImage, -22143)
        self.assertEqual(kCGImageAnimationStatus_AllocationFailure, -22144)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(kCGImageAnimationStartIndex, unicode)
        self.assertIsInstance(kCGImageAnimationDelayTime, unicode)
        self.assertIsInstance(kCGImageAnimationLoopCount, unicode)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertArgIsBlock(
            CGAnimateImageAtURLWithBlock, 2, CGImageSourceAnimationBlock
        )
        self.assertArgIsBlock(
            CGAnimateImageDataWithBlock, 2, CGImageSourceAnimationBlock
        )


if __name__ == "__main__":
    main()
