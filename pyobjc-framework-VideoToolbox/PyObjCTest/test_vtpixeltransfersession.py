from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTPixelTransferSession (TestCase):
    @expectedFailure
    @min_os_level('10.10')
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTPixelTransferSessionRef)


    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTPixelTransferSessionCreate, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTPixelTransferSessionCreate, 1)

        VideoToolbox.VTPixelTransferSessionInvalidate
        VideoToolbox.VTPixelTransferSessionGetTypeID
        VideoToolbox.VTPixelTransferSessionTransferImage


if __name__ == "__main__":
    main()
