import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level

VTMotionEstimationOutputHandler = b"viq@@"


class TestVTMotionEstimationSession(TestCase):
    def test_constants(self):
        self.assertIsEnumType(VideoToolbox.VTMotionEstimationFrameFlags)
        self.assertEqual(
            VideoToolbox.kVTMotionEstimationFrameFlags_CurrentBufferWillBeNextReferenceBuffer,
            1 << 0,
        )

        self.assertIsEnumType(VideoToolbox.VTMotionEstimationInfoFlags)
        self.assertEqual(VideoToolbox.kVTMotionEstimationInfoFlags_Reserved0, 1 << 0)

    @min_os_level("26.0")
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTMotionEstimationSessionRef)

    @min_os_level("26.0")
    def test_functions(self):
        VideoToolbox.VTMotionEstimationSessionGetTypeID

        self.assertArgIsOut(VideoToolbox.VTMotionEstimationSessionCreate, 4)
        self.assertArgIsCFRetained(VideoToolbox.VTMotionEstimationSessionCreate, 4)

        self.assertArgIsOut(
            VideoToolbox.VTMotionEstimationSessionCopySourcePixelBufferAttributes, 1
        )
        self.assertArgIsCFRetained(
            VideoToolbox.VTMotionEstimationSessionCopySourcePixelBufferAttributes, 1
        )

        VideoToolbox.VTMotionEstimationSessionInvalidate

        self.assertArgIsBlock(
            VideoToolbox.VTMotionEstimationSessionEstimateMotionVectors,
            5,
            VTMotionEstimationOutputHandler,
        )

        VideoToolbox.VTMotionEstimationSessionCompleteFrames
