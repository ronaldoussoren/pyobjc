import VideoToolbox
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure

VTCompressionOutputCallback = b"v^v^viI^{opaqueCMSampleBuffer=}"
VTCompressionOutputHandler = b"viQ^{opaqueCMSampleBuffer=}"


class TestVTCompressionSession(TestCase):
    def test_enums(self):
        self.assertIsEnumType(VideoToolbox.VTCompressionSessionOptionFlags)
        self.assertEqual(VideoToolbox.kVTCompressionSessionBeginFinalPass, 1 << 0)

    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderSpecification_EncoderID, str)

    @expectedFailure
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTCompressionSessionRef)

    def test_functions(self):
        self.assertArgIsFunction(
            VideoToolbox.VTCompressionSessionCreate,
            7,
            VTCompressionOutputCallback,
            True,
        )
        self.assertArgIsOut(VideoToolbox.VTCompressionSessionCreate, 9)
        self.assertArgIsCFRetained(VideoToolbox.VTCompressionSessionCreate, 9)

        VideoToolbox.VTCompressionSessionInvalidate

        self.assertIsInstance(VideoToolbox.VTCompressionSessionGetTypeID(), int)

        VideoToolbox.VTCompressionSessionGetPixelBufferPool

        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEncodeFrame, 6)

        VideoToolbox.VTCompressionSessionCompleteFrames

        VideoToolbox.VTCompressionSessionPrepareToEncodeFrames

    @min_os_level("10.10")
    def test_functions10_10(self):
        VideoToolbox.VTCompressionSessionBeginPass

        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEndPass, 1)

        self.assertNotIsInstance(
            VideoToolbox.VTCompressionSessionGetTimeRangesForNextPass, objc.function
        )

    @min_os_level("10.11")
    def test_functions10_11(self):
        self.assertArgIsOut(
            VideoToolbox.VTCompressionSessionEncodeFrameWithOutputHandler, 5
        )
        self.assertArgIsBlock(
            VideoToolbox.VTCompressionSessionEncodeFrameWithOutputHandler,
            6,
            VTCompressionOutputHandler,
        )

    @min_os_level("14.0")
    def test_functions14_0(self):
        self.assertResultIsBOOL(VideoToolbox.VTIsStereoMVHEVCEncodeSupported)

        self.assertArgHasType(
            VideoToolbox.VTCompressionSessionEncodeMultiImageFrame, 5, b"^v"
        )
        self.assertArgIsOut(VideoToolbox.VTCompressionSessionEncodeMultiImageFrame, 6)

        self.assertArgIsOut(
            VideoToolbox.VTCompressionSessionEncodeMultiImageFrameWithOutputHandler, 5
        )
        self.assertArgIsBlock(
            VideoToolbox.VTCompressionSessionEncodeMultiImageFrameWithOutputHandler,
            6,
            VTCompressionOutputHandler,
        )
