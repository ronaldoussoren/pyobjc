import VideoToolbox
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure

VTDecompressionOutputHandler = (
    b"viI^{__CVBuffer=}"
    + VideoToolbox.CMTime.__typestr__
    + VideoToolbox.CMTime.__typestr__
)

VTDecompressionOutputMultiImageCallback = (
    b"v^v^viQ^{OpaqueCMTaggedBufferGroup=}"
    + VideoToolbox.CMTime.__typestr__
    + VideoToolbox.CMTime.__typestr__
)

VTDecompressionMultiImageCapableOutputHandler = (
    b"viQ^{__CVBuffer=}^{OpaqueCMTaggedBufferGroup=}"
    + VideoToolbox.CMTime.__typestr__
    + VideoToolbox.CMTime.__typestr__
)


class TestVTDecompressionSession(TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTDecompressionSessionRef)

    @min_os_level("10.8")
    def test_functions_manual(self):
        # XXX: The implementation is complex enough to require tests.
        self.assertNotIsInstance(
            VideoToolbox.VTDecompressionSessionCreate, objc.function
        )

    @min_os_level("10.8")
    def test_functions(self):
        VideoToolbox.VTDecompressionSessionInvalidate
        VideoToolbox.VTDecompressionSessionGetTypeID

        self.assertArgIsOut(VideoToolbox.VTDecompressionSessionDecodeFrame, 4)

        VideoToolbox.VTDecompressionSessionFinishDelayedFrames

        self.assertResultIsBOOL(
            VideoToolbox.VTDecompressionSessionCanAcceptFormatDescription
        )

        VideoToolbox.VTDecompressionSessionWaitForAsynchronousFrames

        self.assertArgIsOut(VideoToolbox.VTDecompressionSessionCopyBlackPixelBuffer, 1)
        self.assertArgIsCFRetained(
            VideoToolbox.VTDecompressionSessionCopyBlackPixelBuffer, 1
        )

    @min_os_level("10.11")
    def test_functions10_11(self):
        self.assertArgIsOut(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithOutputHandler, 3
        )
        self.assertArgIsBlock(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithOutputHandler,
            4,
            VTDecompressionOutputHandler,
        )

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertResultIsBOOL(VideoToolbox.VTIsHardwareDecodeSupported)

    @min_os_level("14.0")
    def test_functions14_0(self):
        self.assertResultIsBOOL(VideoToolbox.VTIsStereoMVHEVCDecodeSupported)

        self.assertArgIsFunction(
            VideoToolbox.VTDecompressionSessionSetMultiImageCallback,
            1,
            VTDecompressionOutputMultiImageCallback,
            True,
        )
        self.assertArgHasType(
            VideoToolbox.VTDecompressionSessionSetMultiImageCallback, 2, b"^v"
        )

        self.assertArgIsOut(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler,
            3,
        )
        self.assertArgIsBlock(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler,
            4,
            VTDecompressionMultiImageCapableOutputHandler,
        )

    @min_os_level("26.0")
    def test_functions26_0(self):
        self.assertArgIsInOut(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithOptions, 5
        )

        self.assertArgIsBlock(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithOptionsAndOutputHandler,
            5,
            VTDecompressionOutputHandler,
        )
        self.assertArgIsInOut(
            VideoToolbox.VTDecompressionSessionDecodeFrameWithOptionsAndOutputHandler, 4
        )
