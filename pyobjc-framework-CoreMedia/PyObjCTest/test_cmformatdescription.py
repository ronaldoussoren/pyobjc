from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMFormatDescription (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_InvalidParameter, -12710)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_AllocationFailed, -12711)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_ValueNotAvailable, -12718)

        self.assertEqual(CoreMedia.kCMMediaType_Video, fourcc(b'vide'))
        self.assertEqual(CoreMedia.kCMMediaType_Audio, fourcc(b'soun'))
        self.assertEqual(CoreMedia.kCMMediaType_Muxed, fourcc(b'muxx'))
        self.assertEqual(CoreMedia.kCMMediaType_Text, fourcc(b'text'))
        self.assertEqual(CoreMedia.kCMMediaType_ClosedCaption, fourcc(b'clcp'))
        self.assertEqual(CoreMedia.kCMMediaType_Subtitle, fourcc(b'sbtl'))
        self.assertEqual(CoreMedia.kCMMediaType_TimeCode, fourcc(b'tmcd'))
        self.assertEqual(CoreMedia.kCMMediaType_Metadata, fourcc(b'meta'))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422, fourcc(b'apcn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422LT, fourcc(b'apcs'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422Proxy, fourcc(b'apco'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAW, fourcc(b'aprn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAWHQ, fourcc(b'aprh'))

        self.assertEqual(CoreMedia.kCMAudioCodecType_AAC_LCProtected, fourcc(b'paac'))
        self.assertEqual(CoreMedia.kCMAudioCodecType_AAC_AudibleProtected, fourcc(b'aaac'))

        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_StreamBasicDescription, 1<<0)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_MagicCookie, 1<<1)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_ChannelLayout, 1<<2)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_Extensions, 1<<3)
        self.assertEqual(CoreMedia.kCMAudioFormatDescriptionMask_All,  CoreMedia.kCMAudioFormatDescriptionMask_StreamBasicDescription
                                | CoreMedia.kCMAudioFormatDescriptionMask_MagicCookie
                                | CoreMedia.kCMAudioFormatDescriptionMask_ChannelLayout
                                | CoreMedia.kCMAudioFormatDescriptionMask_Extensions)

        self.assertEqual(CoreMedia.kCMPixelFormat_32ARGB, 32)
        self.assertEqual(CoreMedia.kCMPixelFormat_32BGRA, fourcc(b'BGRA'))
        self.assertEqual(CoreMedia.kCMPixelFormat_24RGB, 24)
        self.assertEqual(CoreMedia.kCMPixelFormat_16BE555, 16)
        self.assertEqual(CoreMedia.kCMPixelFormat_16BE565, fourcc(b'B565'))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE555, fourcc(b'L555'))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE565, fourcc(b'L565'))
        self.assertEqual(CoreMedia.kCMPixelFormat_16LE5551, fourcc(b'5551'))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr8, fourcc(b'2vuy'))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr8_yuvs, fourcc(b'yuvs'))
        self.assertEqual(CoreMedia.kCMPixelFormat_444YpCbCr8, fourcc(b'v308'))
        self.assertEqual(CoreMedia.kCMPixelFormat_4444YpCbCrA8, fourcc(b'v408'))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr16, fourcc(b'v216'))
        self.assertEqual(CoreMedia.kCMPixelFormat_422YpCbCr10, fourcc(b'v210'))
        self.assertEqual(CoreMedia.kCMPixelFormat_444YpCbCr10, fourcc(b'v410'))
        self.assertEqual(CoreMedia.kCMPixelFormat_8IndexedGray_WhiteIsZero, 0x00000028)

        self.assertEqual(CoreMedia.kCMVideoCodecType_422YpCbCr8,CoreMedia.kCMPixelFormat_422YpCbCr8)
        self.assertEqual(CoreMedia.kCMVideoCodecType_Animation, fourcc(b'rle '))
        self.assertEqual(CoreMedia.kCMVideoCodecType_Cinepak, fourcc(b'cvid'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_JPEG, fourcc(b'jpeg'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_JPEG_OpenDML, fourcc(b'dmb1'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_SorensonVideo, fourcc(b'SVQ1'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_SorensonVideo3, fourcc(b'SVQ3'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_H263, fourcc(b'h263'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_H264, fourcc(b'avc1'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_HEVC, fourcc(b'hvc1'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG4Video, fourcc(b'mp4v'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG2Video, fourcc(b'mp2v'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_MPEG1Video, fourcc(b'mp1v'))

        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCNTSC, fourcc(b'dvc '))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPAL, fourcc(b'dvcp'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCProPAL, fourcc(b'dvpp'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPro50NTSC, fourcc(b'dv5n'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPro50PAL, fourcc(b'dv5p'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD720p60, fourcc(b'dvhp'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD720p50, fourcc(b'dvhq'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080i60, fourcc(b'dvh6'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080i50, fourcc(b'dvh5'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080p30, fourcc(b'dvh3'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_DVCPROHD1080p25, fourcc(b'dvh2'))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes4444XQ, fourcc(b'ap4x'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes4444, fourcc(b'ap4h'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422HQ, fourcc(b'apch'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422, fourcc(b'apcn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422LT, fourcc(b'apcs'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422Proxy, fourcc(b'apco'))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAW, fourcc(b'aprn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAWHQ, fourcc(b'aprh'))

        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p30, fourcc(b'hdv1'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080i60, fourcc(b'hdv2'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080i50, fourcc(b'hdv3'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p24, fourcc(b'hdv4'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p25, fourcc(b'hdv5'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p24, fourcc(b'hdv6'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p25, fourcc(b'hdv7'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_1080p30, fourcc(b'hdv8'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p60, fourcc(b'hdv9'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_HDV_720p50, fourcc(b'hdva'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080i60_VBR35, fourcc(b'xdv2'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080i50_VBR35, fourcc(b'xdv3'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p24_VBR35, fourcc(b'xdv6'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p25_VBR35, fourcc(b'xdv7'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_1080p30_VBR35, fourcc(b'xdv8'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p24_VBR35, fourcc(b'xdv4'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p25_VBR35, fourcc(b'xdv5'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p30_VBR35, fourcc(b'xdv1'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p50_VBR35, fourcc(b'xdva'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_720p60_VBR35, fourcc(b'xdv9'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080i60_VBR35, fourcc(b'xdvb'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080i50_VBR35, fourcc(b'xdvc'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p24_VBR35, fourcc(b'xdvd'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p25_VBR35, fourcc(b'xdve'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_EX_1080p30_VBR35, fourcc(b'xdvf'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p50_CBR50, fourcc(b'xd5a'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p60_CBR50, fourcc(b'xd59'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080i60_CBR50, fourcc(b'xd5b'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080i50_CBR50, fourcc(b'xd5c'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p24_CBR50, fourcc(b'xd5d'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p25_CBR50, fourcc(b'xd5e'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_1080p30_CBR50, fourcc(b'xd5f'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD_540p, fourcc(b'xdhd'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_540p, fourcc(b'xdh2'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50, fourcc(b'xd54'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50, fourcc(b'xd55'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50, fourcc(b'xd51'))
        self.assertEqual(CoreMedia.kCMMPEG2VideoProfile_XF, fourcc(b'xfz1'))

        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG1System, fourcc(b'mp1s'))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG2Transport, fourcc(b'mp2t'))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_MPEG2Program, fourcc(b'mp2p'))
        self.assertEqual(CoreMedia.kCMMuxedStreamType_DV, fourcc(b'dv  '))

        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_CEA608, fourcc(b'c608'))
        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_CEA708, fourcc(b'c708'))
        self.assertEqual(CoreMedia.kCMClosedCaptionFormatType_ATSC, fourcc(b'atcc'))

        self.assertEqual(CoreMedia.kCMTextFormatType_QTText, fourcc(b'text'))
        self.assertEqual(CoreMedia.kCMTextFormatType_3GText, fourcc(b'tx3g'))

        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollIn, 0x00000020)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollOut, 0x00000040)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirectionMask, 0x00000180)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirection_bottomToTop, 0x00000000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirection_rightToLeft, 0x00000080)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirection_topToBottom, 0x00000100)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_scrollDirection_leftToRight, 0x00000180)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_continuousKaraoke, 0x00000800)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_writeTextVertically, 0x00020000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_fillTextRegion, 0x00040000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_obeySubtitleFormatting, 0x20000000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_forcedSubtitlesPresent, 0x40000000)
        self.assertEqual(CoreMedia.kCMTextDisplayFlag_allSubtitlesForced, 0x80000000)

        self.assertEqual(CoreMedia.kCMTextJustification_left_top,  0)
        self.assertEqual(CoreMedia.kCMTextJustification_centered,  1)
        self.assertEqual(CoreMedia.kCMTextJustification_bottom_right, -1)

        self.assertEqual(CoreMedia.kCMSubtitleFormatType_3GText, fourcc(b'tx3g'))
        self.assertEqual(CoreMedia.kCMSubtitleFormatType_WebVTT, fourcc(b'wvtt'))

        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_TimeCode32, fourcc(b'tmcd'))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_TimeCode64, fourcc(b'tc64'))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_Counter32, fourcc(b'cn32'))
        self.assertEqual(CoreMedia.kCMTimeCodeFormatType_Counter64, fourcc(b'cn64'))

        self.assertEqual(CoreMedia.kCMTimeCodeFlag_DropFrame, 1 << 0)
        self.assertEqual(CoreMedia.kCMTimeCodeFlag_24HourMax, 1 << 1)
        self.assertEqual(CoreMedia.kCMTimeCodeFlag_NegTimesOK, 1 << 2)

        self.assertEqual(CoreMedia.kCMMetadataFormatType_ICY, fourcc(b'icy '))
        self.assertEqual(CoreMedia.kCMMetadataFormatType_ID3, fourcc(b'id3 '))
        self.assertEqual(CoreMedia.kCMMetadataFormatType_Boxed, fourcc(b'mebx'))


    @min_os_level('10.7')
    def test_constants10_7(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_OriginalCompressionSettings, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_VerbatimSampleDescription, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_VerbatimISOSampleEntry, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FormatName, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Depth, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureWidthRational, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureHeightRational, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FullRangeVideo, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ICCProfile, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_BytesPerRow, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionConformsToMPEG2VideoProfile, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_TemporalQuality, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_SpatialQuality, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Version, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_RevisionLevel, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_Vendor, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionVendor_Apple, unicode)

        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_DisplayFlags, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_BackgroundColor, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Red, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Green, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Blue, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionColor_Alpha, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_DefaultTextBox, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Top, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Left, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Bottom, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionRect_Right, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_DefaultStyle, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_StartChar, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Font, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_FontFace, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_ForegroundColor, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_FontSize, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_HorizontalJustification, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_VerticalJustification, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_EndChar, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_FontTable, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_TextJustification, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Height, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionStyle_Ascent, unicode)
        self.assertIsInstance(CoreMedia.kCMTextFormatDescriptionExtension_DefaultFontName, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeCodeFormatDescriptionExtension_SourceReferenceName, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeCodeFormatDescriptionKey_Value, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeCodeFormatDescriptionKey_LangCode, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtensionKey_MetadataKeyTable, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_Namespace, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_Value, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_LocalID, unicode)

    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_P22, unicode)

    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_DataType, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_DataTypeNamespace, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_ConformingDataTypes, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_LanguageTag, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag, unicode)

    @min_os_level('10.11')
    def test_constants10_11(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_VerbatimImageDescription, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_CleanAperture, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureWidth, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureHeight, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureHorizontalOffset, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_CleanApertureVerticalOffset, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FieldCount, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_FieldDetail, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionFieldDetail_TemporalTopFirst, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionFieldDetail_TemporalBottomFirst, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionFieldDetail_SpatialFirstLineEarly, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionFieldDetail_SpatialFirstLineLate, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_PixelAspectRatio, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ColorPrimaries, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_ITU_R_709_2, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_EBU_3213, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_SMPTE_C, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_DCI_P3, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_P3_D65, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionColorPrimaries_ITU_R_2020, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_TransferFunction, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_709_2, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_240M_1995, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_UseGamma, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_2020, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_GammaLevel, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_YCbCrMatrix, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_709_2, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_601_4, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionYCbCrMatrix_SMPTE_240M_1995, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionYCbCrMatrix_ITU_R_2020, unicode)

        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ChromaLocationTopField, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ChromaLocationBottomField, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Left, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Center, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_TopLeft, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Top, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_BottomLeft, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_Bottom, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionChromaLocation_DV420, unicode)

        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_StructuralDependency, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionKey_SetupData, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataFormatDescriptionMetadataSpecificationKey_SetupData, unicode)

    @min_os_level('10.12')
    def test_constants10_12(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_ST_428_1, unicode)

    @min_os_level('10.13')
    def test_constants10_13(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_SMPTE_ST_2084_PQ, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_ITU_R_2100_HLG, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_MasteringDisplayColorVolume, unicode)
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionExtension_ContentLightLevelInfo, unicode)

    @min_os_level('10.14')
    def test_constants10_14(self):
        self.assertIsInstance(CoreMedia.kCMFormatDescriptionTransferFunction_Linear, unicode)

    def test_structs(self):
        v = CoreMedia.CMVideoDimensions()
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMFormatDescriptionRef)


    @expectedFailure
    @min_os_level('10.7')
    def test_functions_manual(self):
        self.assertIsNotInstance(CoreMedia.CMVideoFormatDescriptionCreateFromH264ParameterSets, objc.function)
        self.assertIsNotInstance(CoreMedia.CMVideoFormatDescriptionCreateFromHEVCParameterSets, objc.function)

        self.fail("CMVideoFormatDescriptionGetH264ParameterSetAtIndex") # Needs manual wrapper
        self.fail("CMVideoFormatDescriptionGetHEVCParameterSetAtIndex") # Needs manual wrapper

    @min_os_level('10.7')
    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMFormatDescriptionCreate, 4)
        self.assertArgIsCFRetained(CoreMedia.CMFormatDescriptionCreate, 4)

        self.assertIsInstance(CoreMedia.CMFormatDescriptionGetTypeID(), (int, long))

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
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetChannelLayout, 1)

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
        self.assertArgIsCFRetained(CoreMedia.CMVideoFormatDescriptionCreateForImageBuffer, 2)


        self.assertIs(CoreMedia.CMVideoFormatDescriptionGetCodecType, CoreMedia.CMFormatDescriptionGetMediaSubType)

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
        self.assertArgHasType(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 2, b'o^Z')
        self.assertArgHasType(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 3, b'o^Z')
        self.assertArgHasType(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 4, b'o^Z')
        self.assertArgHasType(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 5, b'o^' + objc._C_CGFloat)
        self.assertArgHasType(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 6, b'o^' + objc._C_CGFloat)
        self.assertArgIsFixedSize(CoreMedia.CMTextFormatDescriptionGetDefaultStyle, 6, 4)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionGetFontName, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTextFormatDescriptionGetFontName, 2)

        self.assertIs(CoreMedia.CMSubtitleFormatDescriptionGetFormatType, CoreMedia.CMFormatDescriptionGetMediaSubType)

        self.assertArgIsOut(CoreMedia.CMTimeCodeFormatDescriptionCreate, 6)
        self.assertArgIsCFRetained(CoreMedia.CMTimeCodeFormatDescriptionCreate, 6)

        CoreMedia.CMTimeCodeFormatDescriptionGetFrameDuration
        CoreMedia.CMTimeCodeFormatDescriptionGetFrameQuanta
        CoreMedia.CMTimeCodeFormatDescriptionGetTimeCodeFlags

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateWithKeys, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateWithKeys, 3)


        CoreMedia.CMMetadataFormatDescriptionGetKeyWithLocalID

    @min_os_level('10.10')
    def test_functions10_10(self):
        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataSpecifications, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataSpecifications, 3)

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications, 3)

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions, 3)

        CoreMedia.CMMetadataFormatDescriptionGetIdentifiers
if __name__ == "__main__":
    main()
