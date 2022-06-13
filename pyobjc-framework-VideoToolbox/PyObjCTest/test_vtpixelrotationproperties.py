from PyObjCTools.TestSupport import TestCase, min_os_level

import VideoToolbox


class TestVTPixelRotationProperties(TestCase):
    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(VideoToolbox.kVTPixelRotationPropertyKey_Rotation, str)
        self.assertIsInstance(VideoToolbox.kVTRotation_0, str)
        self.assertIsInstance(VideoToolbox.kVTRotation_CW90, str)
        self.assertIsInstance(VideoToolbox.kVTRotation_180, str)
        self.assertIsInstance(VideoToolbox.kVTRotation_CCW90, str)
        self.assertIsInstance(
            VideoToolbox.kVTPixelRotationPropertyKey_FlipHorizontalOrientation, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelRotationPropertyKey_FlipVerticalOrientation, str
        )
