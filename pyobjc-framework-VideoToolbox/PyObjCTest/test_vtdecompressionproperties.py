import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTDecompressionProperties(TestCase):
    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_PixelBufferPool, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_PixelBufferPoolIsShared, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_ContentHasInterframeDependencies,
            str,
        )
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_ThreadCount, str)
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_FieldMode, str)
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_FieldMode_BothFields, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_FieldMode_TopFieldOnly, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_FieldMode_BottomFieldOnly, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_FieldMode_SingleField, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_FieldMode_DeinterlaceFields, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_DeinterlaceMode, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_DeinterlaceMode_VerticalFilter, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_DeinterlaceMode_Temporal, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_ReducedResolutionDecode, str
        )
        self.assertIsInstance(VideoToolbox.kVTDecompressionResolutionKey_Width, str)
        self.assertIsInstance(VideoToolbox.kVTDecompressionResolutionKey_Height, str)
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_ReducedCoefficientDecode, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_ReducedFrameDelivery, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_OnlyTheseFrames, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_AllFrames, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_IFrames, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_OnlyTheseFrames_KeyFrames, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_PixelTransferProperties, str
        )

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder,
            str,
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(VideoToolbox.kVTDecompressionPropertyKey_RealTime, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionProperty_TemporalLevelLimit, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID, str
        )

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_MaximizePowerEfficiency, str
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_UsingGPURegistryID, str
        )

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata,
            str,
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs,
            str,
        )
