import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTCompressionProperties(TestCase):
    def test_constants(self):
        self.assertEqual(VideoToolbox.kVTUnlimitedFrameDelayCount, -1)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_NumberOfPendingFrames, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelBufferPoolIsShared, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxKeyFrameInterval, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AllowTemporalCompression, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AllowFrameReordering, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AverageBitRate, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_DataRateLimits, str
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_Quality, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MoreFramesBeforeStart, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MoreFramesAfterEnd, str
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_ProfileLevel, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_1_3, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Extended_5_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L3, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L3, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L4, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L3, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L4, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H263_Profile0_Level10, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H263_Profile0_Level45, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H263_Profile3_Level45, str)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_Depth, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxFrameDelayCount, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxH264SliceBytes, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_SourceFrameCount, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ExpectedFrameRate, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ExpectedDuration, str
        )
        self.assertIsInstance(VideoToolbox.kVTEncodeFrameOptionKey_ForceKeyFrame, str)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_CleanAperture, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelAspectRatio, str
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_FieldCount, str)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_FieldDetail, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AspectRatio16x9, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ProgressiveScan, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ColorPrimaries, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_TransferFunction, str
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_YCbCrMatrix, str)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_ICCProfile, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelTransferProperties, str
        )
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_0, str)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_AutoLevel, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_AutoLevel, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Extended_AutoLevel, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_0, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_1, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_2, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_AutoLevel, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_H264EntropyMode, str
        )
        self.assertIsInstance(VideoToolbox.kVTH264EntropyMode_CAVLC, str)
        self.assertIsInstance(VideoToolbox.kVTH264EntropyMode_CABAC, str)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_RealTime, str)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder,
            str,
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_GammaLevel, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MultiPassStorage, str
        )

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_HEVC_Main_AutoLevel, str)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_HEVC_Main10_AutoLevel, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_BaseLayerFrameRate, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MasteringDisplayColorVolume, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ContentLightLevelInfo, str
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_EncoderID, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_AllowOpenGOP, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaximizePowerEfficiency, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID, str
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_TargetQualityForAlpha, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AlphaChannelMode, str
        )
        self.assertIsInstance(VideoToolbox.kVTAlphaChannelMode_StraightAlpha, str)
        self.assertIsInstance(VideoToolbox.kVTAlphaChannelMode_PremultipliedAlpha, str)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_UsingGPURegistryID, str
        )

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HDRMetadataInsertionMode, str
        )
        self.assertIsInstance(VideoToolbox.kVTHDRMetadataInsertionMode_None, str)
        self.assertIsInstance(VideoToolbox.kVTHDRMetadataInsertionMode_Auto, str)

        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PreserveDynamicHDRMetadata, str
        )

    @min_os_level("11.3")
    def test_constants11_3(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_BaseLayerFrameRateFraction,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_EnableLowLatencyRateControl,
            str,
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H264_ConstrainedBaseline_AutoLevel,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H264_ConstrainedHigh_AutoLevel,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_BaseLayerBitRateFraction,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_SupportsBaseFrameQP,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTEncodeFrameOptionKey_BaseFrameQP,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxAllowedFrameQP,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_EnableLTR,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTEncodeFrameOptionKey_ForceLTRRefresh,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTSampleAttachmentKey_RequireLTRAcknowledgementToken,
            str,
        )

    @min_os_level("12.3")
    def test_constants12_3(self):
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_HEVC_Main42210_AutoLevel,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_OutputBitDepth,
            str,
        )

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ConstantBitRate,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ReferenceBufferCount,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MinAllowedFrameQP,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PreserveAlphaChannel,
            str,
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_RecommendedParallelizationLimit,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumFrameCount,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MVHEVCVideoLayerIDs,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MVHEVCViewIDs,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HeroEye,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_StereoCameraBaseline,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HorizontalDisparityAdjustment,
            str,
        )

    @min_os_level("14.0")
    def test_constants14_2(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HasLeftStereoEyeView,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HasRightStereoEyeView,
            str,
        )

    @min_os_level("14.4")
    def test_constants14_4(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_CalculateMeanSquaredError,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTSampleAttachmentKey_QualityMetrics,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_HorizontalFieldOfView,
            str,
        )
