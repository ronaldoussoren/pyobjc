import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVVideoCompositionHelper(AVFoundation.NSObject):
    def videoComposition_shouldContinueValidatingAfterFindingInvalidValueForKey_(  # noqa: B950
        self, a, b
    ):
        return 1

    def videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_(
        self, a, b
    ):
        return 1

    def videoComposition_shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction_(  # noqa: B950
        self, a, b
    ):
        return 1

    def videoComposition_shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction_layerInstruction_asset_(  # noqa: B950
        self, a, b, c, d
    ):
        return 1


class TestAVVideoComposition(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionInstruction.enablePostProcessing
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMutableVideoCompositionInstruction.enablePostProcessing  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVMutableVideoCompositionInstruction.setEnablePostProcessing_,  # noqa: B950
            0,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidValueForKey_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_  # noqa: B950
        )
        self.assertArgHasType(
            TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_,  # noqa: B950
            1,
            b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}",
        )
        self.assertResultIsBOOL(
            TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction_layerInstruction_asset_  # noqa: B950
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(
            AVFoundation.AVVideoComposition.isValidForAsset_timeRange_validationDelegate_  # noqa: B950
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            AVFoundation.AVVideoComposition.videoCompositionWithAsset_applyingCIFiltersWithHandler_,  # noqa: B950
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVMutableVideoComposition.videoCompositionWithAsset_applyingCIFiltersWithHandler_,  # noqa: B950
            1,
            b"v@",
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAsset.findUnusedTrackIDWithCompletionHandler_,  # noqa: B950
            0,
            b"vi@",
        )

    def testProtocols(self):
        objc.protocolNamed("AVVideoCompositionValidationHandling")
