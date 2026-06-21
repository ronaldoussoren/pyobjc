import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

VTCompressionOutputCallback = b"v^v^viI^{opaqueCMSampleBuffer=}"


class TestAVAssetWritingPlanner(TestCase):
    def test_structs(self):
        v = AVFoundation.AVPlannedVideoSegmentBoundaryGuidelines()
        self.assertEqual(v.minimumFrameCount, 0)
        self.assertEqual(v.minimumDuration, AVFoundation.CMTime())

    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetWritingPlanner.planTrack_withSegmentsGeneratedBy_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetWritingPlanner.executePlanWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetWritingPlanner.executePlanOnQueue_withCompletionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsOut(
            AVFoundation.AVPlannedVideoSegmentWritingRequest.resumableAssetWriterInputWithMediaType_outputSettings_sourceFormatHint_returningError_,
            3,
        )

        self.assertArgIsBlock(
            AVFoundation.AVPlannedVideoSegmentWritingRequest.createResumableCompressionSessionWithAllocator_width_height_codecType_encoderSpecification_sourceImageBufferAttributes_compressedDataAllocator_outputCallback_outputCallbackRefCon_returningError_,
            7,
            VTCompressionOutputCallback,
        )
        self.assertArgIsOut(
            AVFoundation.AVPlannedVideoSegmentWritingRequest.createResumableCompressionSessionWithAllocator_width_height_codecType_encoderSpecification_sourceImageBufferAttributes_compressedDataAllocator_outputCallback_outputCallbackRefCon_returningError_,
            9,
        )
