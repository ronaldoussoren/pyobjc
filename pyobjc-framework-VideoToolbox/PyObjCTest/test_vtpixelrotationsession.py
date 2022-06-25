from PyObjCTools.TestSupport import TestCase, min_os_level

import VideoToolbox


class TestVTPixelRotationSession(TestCase):
    @min_os_level("13.0")
    def test_cftypes(self):
        self.assertIsCFType(VideoToolbox.VTPixelRotationSessionRef)

    @min_os_level("13.0")
    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTPixelRotationSessionCreate, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTPixelRotationSessionCreate, 1)

        VideoToolbox.VTPixelRotationSessionInvalidate

        self.assertIsInstance(VideoToolbox.VTPixelRotationSessionGetTypeID(), int)

        VideoToolbox.VTPixelRotationSessionRotateImage
