from PyObjCTools.TestSupport import *
import VideoToolbox

VTDecompressionOutputHandler = b'viI^{__CVBuffer=}' + VideoToolbox.CMTime.__typestr__ + VideoToolbox.CMTime.__typestr__


class TestVTDecompressionSession (TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTDecompressionSessionRef)

    @min_os_level('10.8')
    def test_functions_manual(self):
        # XXX: The implementation is complex enough to require tests.
        self.assertIsNotInstance(VideoToolbox.VTDecompressionSessionCreate, objc.function)

    @min_os_level('10.8')
    def test_functions(self):
        VideoToolbox.VTDecompressionSessionInvalidate
        VideoToolbox.VTDecompressionSessionGetTypeID

        self.assertArgIsOut(VideoToolbox.VTDecompressionSessionDecodeFrame, 4)

        self.assertArgIsOut(VideoToolbox.VTDecompressionSessionDecodeFrameWithOutputHandler, 3)
        self.assertArgIsBlock(VideoToolbox.VTDecompressionSessionDecodeFrameWithOutputHandler, 4, VTDecompressionOutputHandler)

        VideoToolbox.VTDecompressionSessionFinishDelayedFrames

        self.assertResultIsBOOL(VideoToolbox.VTDecompressionSessionCanAcceptFormatDescription)

        VideoToolbox.VTDecompressionSessionWaitForAsynchronousFrames

        self.assertArgIsOut(VideoToolbox.VTDecompressionSessionCopyBlackPixelBuffer, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTDecompressionSessionCopyBlackPixelBuffer, 1)

        self.assertResultIsBOOL(VideoToolbox.VTIsHardwareDecodeSupported)


if __name__ == "__main__":
    main()
