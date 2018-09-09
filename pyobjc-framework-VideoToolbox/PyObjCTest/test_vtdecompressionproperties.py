from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTDecompressionProperties (TestCase):
    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_PixelBufferPool, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_PixelBufferPoolIsShared, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ContentHasInterframeDependencies, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ThreadCount, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_FieldMode, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_FieldMode_BothFields, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_FieldMode_TopFieldOnly, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_FieldMode_BottomFieldOnly, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_FieldMode_SingleField, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_FieldMode_DeinterlaceFields, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_DeinterlaceMode, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_DeinterlaceMode_VerticalFilter, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_DeinterlaceMode_Temporal, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ReducedResolutionDecode, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionResolutionKey_Width, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionResolutionKey_Height, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ReducedCoefficientDecode, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ReducedFrameDelivery, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_OnlyTheseFrames, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_AllFrames, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_IFrames, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_KeyFrames, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_PixelTransferProperties, unicode)

    @min_os_level('10.9')
    def test_constants10_9(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder, unicode)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder, unicode)

    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_RealTime, unicode)

    @min_os_level('10.13')
    def test_constants10_13(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionProperty_TemporalLevelLimit, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID, unicode)

    @min_os_level('10.14')
    def test_constants10_14(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_MaximizePowerEfficiency, unicode)


if __name__ == "__main__":
    main()
