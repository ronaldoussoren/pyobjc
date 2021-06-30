import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTUtilities(TestCase):
    @min_os_level("10.11")
    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)
        self.assertArgIsCFRetained(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)

    @min_os_level("11.0")
    def test_functions11_0(self):
        VideoToolbox.VTRegisterSupplementalVideoDecoderIfAvailable
