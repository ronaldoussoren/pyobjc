from PyObjCTools.TestSupport import *
import VideoToolbox

VTCompressionOutputCallback = b'v^v^viI^{opaqueCMSampleBuffer=}'
VTCompressionOutputHandler = b'vi@^{opaqueCMSampleBuffer=}'

class TestVTCompressionSession (TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTCompressionSessionRef)

    def test_constants(self):
        self.assertEqual(VideoToolbox.kVTCompressionSessionBeginFinalPass, 1<<0)

    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderSpecification_EncoderID, unicode)

    @min_os_level('10.8')
    def test_functions(self):
        self.assertArgIsFunction(VideoToolbox.VTCompressionSessionCreate, 7, VTCompressionOutputCallback, True)
        self.assertArgIsOut(VideoToolbox.VTCompressionSessionCreate, 9)
        self.assertArgIsCFRetained(VideoToolbox.VTCompressionSessionCreate, 9)

        VideoToolbox.VTCompressionSessionInvalidate

        self.assertIsInstance(VideoToolbox.VTCompressionSessionGetTypeID(), (int, long))

        VideoToolbox.VTCompressionSessionGetPixelBufferPool

        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEncodeFrame, 6)

        VideoToolbox.VTCompressionSessionCompleteFrames

    @min_os_level('10.9')
    def test_functions10_9(self):
        VideoToolbox.VTCompressionSessionPrepareToEncodeFrames

    @min_os_level('10.10')
    def test_functions10_10(self):
        VideoToolbox.VTCompressionSessionBeginPass

        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEndPass, 1)

        self.assertIsNotInstance(VideoToolbox.VTCompressionSessionGetTimeRangesForNextPass, objc.function)

    @min_os_level('10.11')
    def test_functions10_11(self):
        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEncodeFrameWithOutputHandler, 5)
        self.assertArgIsBlock(VideoToolbox.VTCompressionSessionEncodeFrameWithOutputHandler, 6, VTCompressionOutputHandler)


if __name__ == "__main__":
    main()
