import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure, fourcc
import objc


class TestCMFormatDescription(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_InvalidParameter, -12710)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_AllocationFailed, -12711)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_ValueNotAvailable, -12718)

        self.assertEqual(CoreMedia.kCMMediaType_Video, fourcc(b"vide"))
        self.assertEqual(CoreMedia.kCMMediaType_Audio, fourcc(b"soun"))
        self.assertEqual(CoreMedia.kCMMediaType_Muxed, fourcc(b"muxx"))
        self.assertEqual(CoreMedia.kCMMediaType_Text, fourcc(b"text"))
        self.assertEqual(CoreMedia.kCMMediaType_ClosedCaption, fourcc(b"clcp"))
        self.assertEqual(CoreMedia.kCMMediaType_Subtitle, fourcc(b"sbtl"))
        self.assertEqual(CoreMedia.kCMMediaType_TimeCode, fourcc(b"tmcd"))
        self.assertEqual(CoreMedia.kCMMediaType_Metadata, fourcc(b"meta"))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422, fourcc(b"apcn"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422LT, fourcc(b"apcs"))
        self.assertEqual(
            CoreMedia.kCMVideoCodecType_AppleProRes422Proxy, fourcc(b"apco")
        )
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAW, fourcc(b"aprn"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAWHQ, fourcc(b"aprh"))

        self.assertEqual(CoreMedia.kCMAudioCodecType_AAC_LCProtected, fourcc(b"paac"))
        self.assertEqual(
            CoreMedia.kCMAudioCodecType_AAC_AudibleProtected, fourcc(b"aaac")
        )

        self.assertEqual(CoreMedia.kCMVideoCodecType_DisparityHEVC, fourcc(b"dish"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DepthHEVC, fourcc(b"deph"))

        self.assertEqual(
            CoreMedia.kCMAudioFormatDescriptionMask_StreamBasicDescription, 1 << 0
        )
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_MagicCookie, 1 << 1)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_ChannelLayout, 1 << 2)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_Extensions, 1 << 3)
        self.assertEqual(
            CoreMedia.kCMAudioFormatDescriptionMask_All,
            CoreMedia.kCMAudioFormatDescriptionMask_StreamBasicDescription
            | CoreMedia.kCMAudioFormatDescriptionMask_MagicCookie
            | CoreMedia.kCMAudioFormatDescriptionMask_ChannelLayout
            | CoreMedia.kCMAudioFormatDescriptionMask_Extensions,
        )

        self.assertEqual(CoreMedia.kCMPixelFormat_32ARGB, 32)
        self.assertEqual(CoreMedia.kCMPixelFormat_32BGRA, fourcc(b"BGRA"))
        self.assertEqual(CoreMedia.kCMPixelFormat_24RGB, 24)
        self.assertEqual(CoreMedia.kCMPixelFormat_16BE555, 16)
        self.assertEqual(CoreMedia.kCMPixelFormat_16BE565, fourcc(b"B565"))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE555, fourcc(b"L555"))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE565, fourcc(b"L565"))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE5551, fourcc(b"5551"))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr8, fourcc(b"2vuy"))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr8_yuvs, fourcc(b"yuvs"))
        self.assertEqual(CoreMedia.kCMPixelFormat_444YpCbCr8, fourcc(b"v308"))
        self.assertEqual(CoreMedia.kCMPixelFormat_4444YpCbCrA8, fourcc(b"v408"))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr16, fourcc(b"v216"))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr10, fourcc(b"v210"))
        self.assertEqual(CoreMedia.kCMPixelFormat_444YpCbCr10, fourcc(b"v410"))
        self.assertEqual(CoreMedia.kCMPixelFormat_8IndexedGray_WhiteIsZero, 0x00000028)

        self.assertEqual(
            CoreMedia.kCMVideoCodecType_422YpCbCr8, CoreMedia.kCMPixelFormat_422YpCbCr8
        )
        self.assertEqual(CoreMedia.kCMVideoCodecType_Animation, fourcc(b"rle "))
        self.assertEqual(CoreMedia.kCMVideoCodecType_Cinepak, fourcc(b"cvid"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_JPEG, fourcc(b"jpeg"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_JPEG_OpenDML, fourcc(b"dmb1"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_SorensonVideo, fourcc(b"SVQ1"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_SorensonVideo3, fourcc(b"SVQ3"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_H263, fourcc(b"h263"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_H264, fourcc(b"avc1"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_HEVC, fourcc(b"hvc1"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_HEVCWithAlpha, fourcc(b"muxa"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DolbyVisionHEVC, fourcc(b"dvh1"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG4Video, fourcc(b"mp4v"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG2Video, fourcc(b"mp2v"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG1Video, fourcc(b"mp1v"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_VP9, fourcc(b"vp09"))

        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCNTSC, fourcc(b"dvc "))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPAL, fourcc(b"dvcp"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCProPAL, fourcc(b"dvpp"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPro50NTSC, fourcc(b"dv5n"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPro50PAL, fourcc(b"dv5p"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD720p60, fourcc(b"dvhp"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD720p50, fourcc(b"dvhq"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080i60, fourcc(b"dvh6"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080i50, fourcc(b"dvh5"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080p30, fourcc(b"dvh3"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080p25, fourcc(b"dvh2"))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes4444XQ, fourcc(b"ap4x"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes4444, fourcc(b"ap4h"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422HQ, fourcc(b"apch"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422, fourcc(b"apcn"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422LT, fourcc(b"apcs"))
        self.assertEqual(
            CoreMedia.kCMVideoCodecType_AppleProRes422Proxy, fourcc(b"apco")
        )

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAW, fourcc(b"aprn"))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAWHQ, fourcc(b"aprh"))

        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p30, fourcc(b"hdv1"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080i60, fourcc(b"hdv2"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080i50, fourcc(b"hdv3"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p24, fourcc(b"hdv4"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p25, fourcc(b"hdv5"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p24, fourcc(b"hdv6"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p25, fourcc(b"hdv7"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p30, fourcc(b"hdv8"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p60, fourcc(b"hdv9"))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p50, fourcc(b"hdva"))
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080i60_VBR35, fourcc(b"xdv2")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080i50_VBR35, fourcc(b"xdv3")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p24_VBR35, fourcc(b"xdv6")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p25_VBR35, fourcc(b"xdv7")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p30_VBR35, fourcc(b"xdv8")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p24_VBR35, fourcc(b"xdv4")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p25_VBR35, fourcc(b"xdv5")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p30_VBR35, fourcc(b"xdv1")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p50_VBR35, fourcc(b"xdva")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p60_VBR35, fourcc(b"xdv9")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080i60_VBR35, fourcc(b"xdvb")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080i50_VBR35, fourcc(b"xdvc")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p24_VBR35, fourcc(b"xdvd")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p25_VBR35, fourcc(b"xdve")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p30_VBR35, fourcc(b"xdvf")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p50_CBR50, fourcc(b"xd5a")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p60_CBR50, fourcc(b"xd59")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080i60_CBR50, fourcc(b"xd5b")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080i50_CBR50, fourcc(b"xd5c")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p24_CBR50, fourcc(b"xd5d")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p25_CBR50, fourcc(b"xd5e")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p30_CBR50, fourcc(b"xd5f")
        )
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_540p, fourcc(b"xdhd"))
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_540p, fourcc(b"xdh2")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50, fourcc(b"xd54")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50, fourcc(b"xd55")
        )
        self.assertEqual(
            CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50, fourcc(b"xd51")
        )
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XF, fourcc(b"xfz1"))

        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG1System, fourcc(b"mp1s"))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG2Transport, fourcc(b"mp2t"))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG2Program, fourcc(b"mp2p"))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_DV, fourcc(b"dv  "))

        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_CEA608, fourcc(b"c608"))
        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_CEA708, fourcc(b"c708"))
        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_ATSC, fourcc(b"atcc"))

        self.assertEqual(CoreMedia.kCMTextFormatType_QTText, fourcc(b"text"))
        self.assertEqual(CoreMedia.kCMTextFormatType_3GText, fourcc(b"tx3g"))

        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollIn, 0x00000020)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollOut, 0x00000040)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirectionMask, 0x00000180)
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_scrollDirection_bottomToTop, 0x00000000
        )
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_scrollDirection_rightToLeft, 0x00000080
        )
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_scrollDirection_topToBottom, 0x00000100
        )
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_scrollDirection_leftToRight, 0x00000180
        )
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_continuousKaraoke, 0x00000800)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_writeTextVertically, 0x00020000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_fillTextRegion, 0x00040000)
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_obeySubtitleFormatting, 0x20000000
        )
        self.assertEqual(
            CoreMedia.kCMTextDisplayFlag_forcedSubtitlesPresent, 0x40000000
        )
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_allSubtitlesForced, 0x80000000)

        self.assertEqual(CoreMedia.kCMTextJustification_left_top, 0)
        self.assertEqual(CoreMedia.kCMTextJustification_centered, 1)
        self.assertEqual(CoreMedia.kCMTextJustification_bottom_right, -1)

        self.assertEqual(CoreMedia.kCMSubtitleFormatType_3GText, fourcc(b"tx3g"))
        self.assertEqual(CoreMedia.kCMSubtitleFormatType_WebVTT, fourcc(b"wvtt"))

        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_TimeCode32, fourcc(b"tmcd"))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_TimeCode64, fourcc(b"tc64"))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_Counter32, fourcc(b"cn32"))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_Counter64, fourcc(b"cn64"))

        self.assertEqual(CoreMedia.kCMTimeCodeFlag_DropFrame, 1 << 0)
        self.assertEqual(CoreMedia.kCMTimeCodeFlag_24HourMax, 1 << 1)
        self.assertEqual(CoreMedia.kCMTimeCodeFlag_NegTimesOK, 1 << 2)

        self.assertEqual(CoreMedia.kCMMetadataFormatType_ICY, fourcc(b"icy "))
        self.assertEqual(CoreMedia.kCMMetadataFormatType_ID3, fourcc(b"id3 "))
        self.assertEqual(CoreMedia.kCMMetadataFormatType_Boxed, fourcc(b"mebx"))
        self.assertEqual(CoreMedia.kCMMetadataFormatType_EMSG, fourcc(b"emsg"))

    @min_os_level("10.7")
    def test_constants10_7(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_OriginalCompressionSettings, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_VerbatimSampleDescription, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_VerbatimISOSampleEntry, str
        )

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FormatName, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Depth, str)

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureWidthRational, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureHeightRational, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_FullRangeVideo, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ICCProfile, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_BytesPerRow, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionConformsToMPEG2VideoProfile, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_TemporalQuality, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_SpatialQuality, str
        )

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Version, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_RevisionLevel, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Vendor, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionVendor_Apple, str)

        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_DisplayFlags, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_BackgroundColor, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Red, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Green, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Blue, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Alpha, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_DefaultTextBox, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Top, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Left, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Bottom, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Right, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_DefaultStyle, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_StartChar, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Font, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_FontFace, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionStyle_ForegroundColor, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_FontSize, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_HorizontalJustification, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_VerticalJustification, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_EndChar, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_FontTable, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_TextJustification, str
        )
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Height, str)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Ascent, str)
        self.assertIsInstance(
            CoreMedia.kCMTextFormatDescriptionExtension_DefaultFontName, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTimeCodeFormatDescriptionExtension_SourceReferenceName, str
        )
        self.assertIsInstance(CoreMedia.kCMTimeCodeFormatDescriptionKey_Value, str)
        self.assertIsInstance(CoreMedia.kCMTimeCodeFormatDescriptionKey_LangCode, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtensionKey_MetadataKeyTable, str
        )
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_Namespace, str)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_Value, str)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_LocalID, str)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_P22, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_DataType, str)
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionKey_DataTypeNamespace, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionKey_ConformingDataTypes, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionKey_LanguageTag, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag,
            str,
        )

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_VerbatimImageDescription, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_CleanAperture, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureWidth, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureHeight, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureHorizontalOffset, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_CleanApertureVerticalOffset, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FieldCount, str)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FieldDetail, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionFieldDetail_TemporalTopFirst, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionFieldDetail_TemporalBottomFirst, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionFieldDetail_SpatialFirstLineEarly, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionFieldDetail_SpatialFirstLineLate, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_PixelAspectRatio, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ColorPrimaries, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionColorPrimaries_ITU_R_709_2, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionColorPrimaries_EBU_3213, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_SMPTE_C, str)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_DCI_P3, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_P3_D65, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionColorPrimaries_ITU_R_2020, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_TransferFunction, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_709_2, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_240M_1995, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_UseGamma, str
        )

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_2020, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_GammaLevel, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_YCbCrMatrix, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_709_2, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_601_4, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionYCbCrMatrix_SMPTE_240M_1995, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_2020, str)

        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ChromaLocationTopField, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ChromaLocationBottomField, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Left, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Center, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_TopLeft, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Top, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionChromaLocation_BottomLeft, str
        )
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Bottom, str)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_DV420, str)

        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionKey_StructuralDependency, str
        )
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_SetupData, str)
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_SetupData,
            str,
        )

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_ST_428_1, str
        )

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_ST_2084_PQ, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_2100_HLG, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_MasteringDisplayColorVolume, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ContentLightLevelInfo, str
        )

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionTransferFunction_Linear, str
        )

    @min_os_level("10.14.4")
    def test_constants10_14_4(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_AlternativeTransferCharacteristics,
            str,
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_sRGB, str)
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_AuxiliaryTypeInfo, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_AlphaChannelMode, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionAlphaChannelMode_StraightAlpha, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionAlphaChannelMode_PremultipliedAlpha, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ContainsAlphaChannel, str
        )

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_ProtectedContentOriginalFormat, str
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_BitsPerComponent, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_HorizontalFieldOfView, str
        )
        self.assertIsInstance(
            CoreMedia.kCMFormatDescriptionExtension_AmbientViewingEnvironment, str
        )

    def test_structs(self):
        v = CoreMedia.CMVideoDimensions()
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertPickleRoundTrips(v)

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMFormatDescriptionRef)

    @expectedFailure
    @min_os_level("10.7")
    def test_functions_manual(self):
        self.assertNotIsInstance(
            CoreMedia.CMVideoFormatDescriptionCreateFromH264ParameterSets, objc.function
        )
        self.assertNotIsInstance(
            CoreMedia.CMVideoFormatDescriptionCreateFromHEVCParameterSets, objc.function
        )

        self.fail(
            "CMVideoFormatDescriptionGetH264ParameterSetAtIndex"
        )  # Needs manual wrapper
        self.fail(
            "CMVideoFormatDescriptionGetHEVCParameterSetAtIndex"
        )  # Needs manual wrapper

    @min_os_level("10.7")
    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMFormatDescriptionCreate, 4)
        self.assertArgIsCFRetained(CoreMedia.CMFormatDescriptionCreate, 4)

        self.assertIsInstance(CoreMedia.CMFormatDescriptionGetTypeID(), int)

        self.assertResultIsBOOL(CoreMedia.CMFormatDescriptionEqual)

        self.assertResultIsBOOL(CoreMedia.CMFormatDescriptionEqualIgnoringExtensionKeys)

        CoreMedia.CMFormatDescriptionGetMediaType
        CoreMedia.CMFormatDescriptionGetMediaSubType
        CoreMedia.CMFormatDescriptionGetExtensions
        CoreMedia.CMFormatDescriptionGetExtension

        self.assertArgIsIn(CoreMedia.CMAudioFormatDescriptionCreate, 3)
        self.assertArgIsIn(CoreMedia.CMAudioFormatDescriptionCreate, 5)
        self.assertArgSizeInArg(CoreMedia.CMAudioFormatDescriptionCreate, 5, 4)
        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCreate, 7)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCreate, 7)

        CoreMedia.CMAudioFormatDescriptionGetStreamBasicDescription

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetMagicCookie, 1)
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetMagicCookie, 1)

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetChannelLayout, 1)
        self.assertResultSizeInArg(
            CoreMedia.CMAudioFormatDescriptionGetChannelLayout, 1
        )

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetFormatList, 1)
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetFormatList, 1)

        # XXX: Need to derefence pointer
        CoreMedia.CMAudioFormatDescriptionGetRichestDecodableFormat
        CoreMedia.CMAudioFormatDescriptionGetMostCompatibleFormat

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCreateSummary, 3)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCreateSummary, 3)

        self.assertResultIsBOOL(CoreMedia.CMAudioFormatDescriptionEqual)
        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionEqual, 3)

        self.assertArgIsOut(CoreMedia.CMVideoFormatDescriptionCreate, 5)
        self.assertArgIsCFRetained(CoreMedia.CMVideoFormatDescriptionCreate, 5)

        self.assertArgIsOut(CoreMedia.CMVideoFormatDescriptionCreateForImageBuffer, 2)
        self.assertArgIsCFRetained(
            CoreMedia.CMVideoFormatDescriptionCreateForImageBuffer, 2
        )

        self.assertIs(
            CoreMedia.CMVideoFormatDescriptionGetCodecType,
            CoreMedia.CMFormatDescriptionGetMediaSubType,
        )

        CoreMedia.CMVideoFormatDescriptionGetDimensions
        CoreMedia.CMVideoFormatDescriptionGetPresentationDimensions
        CoreMedia.CMVideoFormatDescriptionGetCleanAperture
        CoreMedia.CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers

        self.assertResultIsBOOL(CoreMedia.CMVideoFormatDescriptionMatchesImageBuffer)

        self.assertArgIsOut(CoreMedia.CMMuxedFormatDescriptionCreate, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMuxedFormatDescriptionCreate, 3)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetDisplayFlags, 1)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetJustification, 1)
        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetJustification, 2)

        self.assertArgIsBOOL(CoreMedia.CMTextFormatDescriptionGetDefaultTextBox, 1)
        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetDefaultTextBox, 3)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 1)
        self.assertArgHasType(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 2, b"o^Z"
        )
        self.assertArgHasType(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 3, b"o^Z"
        )
        self.assertArgHasType(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 4, b"o^Z"
        )
        self.assertArgHasType(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 5, b"o^" + objc._C_CGFloat
        )
        self.assertArgHasType(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 6, b"o^" + objc._C_CGFloat
        )
        self.assertArgIsFixedSize(
            CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 6, 4
        )

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetFontName, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTextFormatDescriptionGetFontName, 2)

        self.assertIs(
            CoreMedia.CMSubtitleFormatDescriptionGetFormatType,
            CoreMedia.CMFormatDescriptionGetMediaSubType,
        )

        self.assertArgIsOut(CoreMedia.CMTimeCodeFormatDescriptionCreate, 6)
        self.assertArgIsCFRetained(CoreMedia.CMTimeCodeFormatDescriptionCreate, 6)

        CoreMedia.CMTimeCodeFormatDescriptionGetFrameDuration
        CoreMedia.CMTimeCodeFormatDescriptionGetFrameQuanta
        CoreMedia.CMTimeCodeFormatDescriptionGetTimeCodeFlags

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateWithKeys, 3)
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataFormatDescriptionCreateWithKeys, 3
        )

        CoreMedia.CMMetadataFormatDescriptionGetKeyWithLocalID

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertArgIsOut(
            CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataSpecifications, 3
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataSpecifications, 3
        )

        self.assertArgIsOut(
            CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications,
            3,
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications,
            3,
        )

        self.assertArgIsOut(
            CoreMedia.CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions,
            3,
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions,
            3,
        )

        CoreMedia.CMMetadataFormatDescriptionGetIdentifiers
