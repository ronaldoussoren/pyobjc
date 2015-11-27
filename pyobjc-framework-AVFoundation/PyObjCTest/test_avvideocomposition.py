from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVVideoCompositionHelper (AVFoundation.NSObject):
    def videoComposition_shouldContinueValidatingAfterFindingInvalidValueForKey_(self, a, b): return 1
    def videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_(self, a, b): return 1
    def videoComposition_shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction_(self, a, b): return 1
    def videoComposition_shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction_layerInstruction_asset_(self, a, b, c, d): return 1


class TestAVVideoComposition (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVVideoCompositionInstruction.enablePostProcessing)
        self.assertResultIsBOOL(AVFoundation.AVMutableVideoCompositionInstruction.enablePostProcessing)
        self.assertArgIsBOOL(AVFoundation.AVMutableVideoCompositionInstruction.setEnablePostProcessing_, 0)

        self.assertResultIsBOOL(AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_, 1)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_, 2)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getTransformRampForTime_startTransform_endTransform_timeRange_, 3)

        self.assertResultIsBOOL(AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_, 1)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_, 2)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getOpacityRampForTime_startOpacity_endOpacity_timeRange_, 3)

        self.assertResultIsBOOL(AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_, 1)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_, 2)
        self.assertArgIsOut(AVFoundation.AVVideoCompositionLayerInstruction.getCropRectangleRampForTime_startCropRectangle_endCropRectangle_timeRange_, 3)


        self.assertResultIsBOOL(TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidValueForKey_)
        self.assertResultIsBOOL(TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_)
        self.assertArgHasType(TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingEmptyTimeRange_, 1, b'{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}')
        self.assertResultIsBOOL(TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction_)
        self.assertResultIsBOOL(TestAVVideoCompositionHelper.videoComposition_shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction_layerInstruction_asset_)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVVideoComposition.isValidForAsset_timeRange_validationDelegate_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBlock(AVFoundation.AVVideoComposition.videoCompositionWithAsset_applyingCIFiltersWithHandler_, 1, b'v@')
        self.assertArgIsBlock(AVFoundation.AVMutableVideoComposition.videoCompositionWithAsset_applyingCIFiltersWithHandler_, 1, b'v@')

    def testProtocols(self):
        objc.protocolNamed('AVVideoCompositionValidationHandling')

if __name__ == "__main__":
    main()
