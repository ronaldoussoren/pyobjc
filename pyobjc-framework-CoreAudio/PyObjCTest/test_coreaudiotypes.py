import sys

import CoreAudio
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc


class TestAudioDriverPlugIn(TestCase):
    def assert_buffer_size(self, buf, size):
        self.assertIsInstance(buf, memoryview)
        self.assertEqual(buf.itemsize, 1)
        self.assertEqual(buf.nbytes, size)

    def testConstants(self):
        self.assertEqual(CoreAudio.kAudio_UnimplementedError, -4)
        self.assertEqual(CoreAudio.kAudio_FileNotFoundError, -43)
        self.assertEqual(CoreAudio.kAudio_FilePermissionError, -54)
        self.assertEqual(CoreAudio.kAudio_TooManyFilesOpenError, -42)
        self.assertEqual(CoreAudio.kAudio_BadFilePathError, fourcc(b"!pth"))
        self.assertEqual(CoreAudio.kAudio_ParamError, -50)
        self.assertEqual(CoreAudio.kAudio_MemFullError, -108)

        self.assertEqual(CoreAudio.kAudioFormatLinearPCM, fourcc(b"lpcm"))
        self.assertEqual(CoreAudio.kAudioFormatAC3, fourcc(b"ac-3"))
        self.assertEqual(CoreAudio.kAudioFormat60958AC3, fourcc(b"cac3"))
        self.assertEqual(CoreAudio.kAudioFormatAppleIMA4, fourcc(b"ima4"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC, fourcc(b"aac "))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4CELP, fourcc(b"celp"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4HVXC, fourcc(b"hvxc"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4TwinVQ, fourcc(b"twvq"))
        self.assertEqual(CoreAudio.kAudioFormatMACE3, fourcc(b"MAC3"))
        self.assertEqual(CoreAudio.kAudioFormatMACE6, fourcc(b"MAC6"))
        self.assertEqual(CoreAudio.kAudioFormatULaw, fourcc(b"ulaw"))
        self.assertEqual(CoreAudio.kAudioFormatALaw, fourcc(b"alaw"))
        self.assertEqual(CoreAudio.kAudioFormatQDesign, fourcc(b"QDMC"))
        self.assertEqual(CoreAudio.kAudioFormatQDesign2, fourcc(b"QDM2"))
        self.assertEqual(CoreAudio.kAudioFormatQUALCOMM, fourcc(b"Qclp"))
        self.assertEqual(CoreAudio.kAudioFormatMPEGLayer1, fourcc(b".mp1"))
        self.assertEqual(CoreAudio.kAudioFormatMPEGLayer2, fourcc(b".mp2"))
        self.assertEqual(CoreAudio.kAudioFormatMPEGLayer3, fourcc(b".mp3"))
        self.assertEqual(CoreAudio.kAudioFormatTimeCode, fourcc(b"time"))
        self.assertEqual(CoreAudio.kAudioFormatMIDIStream, fourcc(b"midi"))
        self.assertEqual(CoreAudio.kAudioFormatParameterValueStream, fourcc(b"apvs"))
        self.assertEqual(CoreAudio.kAudioFormatAppleLossless, fourcc(b"alac"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_HE, fourcc(b"aach"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_LD, fourcc(b"aacl"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_ELD, fourcc(b"aace"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_ELD_SBR, fourcc(b"aacf"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_ELD_V2, fourcc(b"aacg"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_HE_V2, fourcc(b"aacp"))
        self.assertEqual(CoreAudio.kAudioFormatMPEG4AAC_Spatial, fourcc(b"aacs"))
        self.assertEqual(CoreAudio.kAudioFormatAMR, fourcc(b"samr"))
        self.assertEqual(CoreAudio.kAudioFormatAMR_WB, fourcc(b"sawb"))
        self.assertEqual(CoreAudio.kAudioFormatAudible, fourcc(b"AUDB"))
        self.assertEqual(CoreAudio.kAudioFormatiLBC, fourcc(b"ilbc"))
        self.assertEqual(CoreAudio.kAudioFormatDVIIntelIMA, 0x6D730011)
        self.assertEqual(CoreAudio.kAudioFormatMicrosoftGSM, 0x6D730031)
        self.assertEqual(CoreAudio.kAudioFormatAES3, fourcc(b"aes3"))
        self.assertEqual(CoreAudio.kAudioFormatEnhancedAC3, fourcc(b"ec-3"))
        self.assertEqual(CoreAudio.kAudioFormatFLAC, fourcc(b"flac"))
        self.assertEqual(CoreAudio.kAudioFormatOpus, fourcc(b"opus"))

        self.assertEqual(CoreAudio.kAudioFormatFlagIsFloat, 1 << 0)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsBigEndian, 1 << 1)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsSignedInteger, 1 << 2)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsPacked, 1 << 3)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsAlignedHigh, 1 << 4)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsNonInterleaved, 1 << 5)
        self.assertEqual(CoreAudio.kAudioFormatFlagIsNonMixable, 1 << 6)
        self.assertEqual(CoreAudio.kAudioFormatFlagsAreAllClear, 0x80000000)

        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsFloat, CoreAudio.kAudioFormatFlagIsFloat
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsBigEndian,
            CoreAudio.kAudioFormatFlagIsBigEndian,
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsSignedInteger,
            CoreAudio.kAudioFormatFlagIsSignedInteger,
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsPacked, CoreAudio.kAudioFormatFlagIsPacked
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsAlignedHigh,
            CoreAudio.kAudioFormatFlagIsAlignedHigh,
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsNonInterleaved,
            CoreAudio.kAudioFormatFlagIsNonInterleaved,
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagIsNonMixable,
            CoreAudio.kAudioFormatFlagIsNonMixable,
        )
        self.assertEqual(CoreAudio.kLinearPCMFormatFlagsSampleFractionShift, 7)
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagsSampleFractionMask,
            0x3F << CoreAudio.kLinearPCMFormatFlagsSampleFractionShift,
        )
        self.assertEqual(
            CoreAudio.kLinearPCMFormatFlagsAreAllClear,
            CoreAudio.kAudioFormatFlagsAreAllClear,
        )

        self.assertEqual(CoreAudio.kAppleLosslessFormatFlag_16BitSourceData, 1)
        self.assertEqual(CoreAudio.kAppleLosslessFormatFlag_20BitSourceData, 2)
        self.assertEqual(CoreAudio.kAppleLosslessFormatFlag_24BitSourceData, 3)
        self.assertEqual(CoreAudio.kAppleLosslessFormatFlag_32BitSourceData, 4)

        if sys.byteorder == "big":
            self.assertEqual(
                CoreAudio.kAudioFormatFlagsNativeEndian,
                CoreAudio.kAudioFormatFlagIsBigEndian,
            )
        else:
            self.assertEqual(CoreAudio.kAudioFormatFlagsNativeEndian, 0)

        self.assertEqual(
            CoreAudio.kAudioFormatFlagsCanonical,
            CoreAudio.kAudioFormatFlagIsFloat
            | CoreAudio.kAudioFormatFlagsNativeEndian
            | CoreAudio.kAudioFormatFlagIsPacked,
        )
        self.assertEqual(
            CoreAudio.kAudioFormatFlagsAudioUnitCanonical,
            CoreAudio.kAudioFormatFlagIsFloat
            | CoreAudio.kAudioFormatFlagsNativeEndian
            | CoreAudio.kAudioFormatFlagIsPacked
            | CoreAudio.kAudioFormatFlagIsNonInterleaved,
        )
        self.assertEqual(
            CoreAudio.kAudioFormatFlagsNativeFloatPacked,
            CoreAudio.kAudioFormatFlagIsFloat
            | CoreAudio.kAudioFormatFlagsNativeEndian
            | CoreAudio.kAudioFormatFlagIsPacked,
        )

        self.assertEqual(CoreAudio.kSMPTETimeType24, 0)
        self.assertEqual(CoreAudio.kSMPTETimeType25, 1)
        self.assertEqual(CoreAudio.kSMPTETimeType30Drop, 2)
        self.assertEqual(CoreAudio.kSMPTETimeType30, 3)
        self.assertEqual(CoreAudio.kSMPTETimeType2997, 4)
        self.assertEqual(CoreAudio.kSMPTETimeType2997Drop, 5)
        self.assertEqual(CoreAudio.kSMPTETimeType60, 6)
        self.assertEqual(CoreAudio.kSMPTETimeType5994, 7)
        self.assertEqual(CoreAudio.kSMPTETimeType60Drop, 8)
        self.assertEqual(CoreAudio.kSMPTETimeType5994Drop, 9)
        self.assertEqual(CoreAudio.kSMPTETimeType50, 10)
        self.assertEqual(CoreAudio.kSMPTETimeType2398, 11)

        self.assertEqual(CoreAudio.kSMPTETimeUnknown, 0)
        self.assertEqual(CoreAudio.kSMPTETimeValid, 1 << 0)
        self.assertEqual(CoreAudio.kSMPTETimeRunning, 1 << 1)

        self.assertEqual(CoreAudio.kAudioTimeStampNothingValid, 0)
        self.assertEqual(CoreAudio.kAudioTimeStampSampleTimeValid, 1 << 0)
        self.assertEqual(CoreAudio.kAudioTimeStampHostTimeValid, 1 << 1)
        self.assertEqual(CoreAudio.kAudioTimeStampRateScalarValid, 1 << 2)
        self.assertEqual(CoreAudio.kAudioTimeStampWordClockTimeValid, 1 << 3)
        self.assertEqual(CoreAudio.kAudioTimeStampSMPTETimeValid, 1 << 4)
        self.assertEqual(
            CoreAudio.kAudioTimeStampSampleHostTimeValid,
            CoreAudio.kAudioTimeStampSampleTimeValid
            | CoreAudio.kAudioTimeStampHostTimeValid,
        )

        self.assertEqual(CoreAudio.kAudioChannelLabel_Unknown, 0xFFFFFFFF)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Unused, 0)
        self.assertEqual(CoreAudio.kAudioChannelLabel_UseCoordinates, 100)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Left, 1)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Right, 2)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Center, 3)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LFEScreen, 4)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LeftSurround, 5)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RightSurround, 6)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LeftCenter, 7)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RightCenter, 8)
        self.assertEqual(CoreAudio.kAudioChannelLabel_CenterSurround, 9)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LeftSurroundDirect, 10)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RightSurroundDirect, 11)
        self.assertEqual(CoreAudio.kAudioChannelLabel_TopCenterSurround, 12)
        self.assertEqual(CoreAudio.kAudioChannelLabel_VerticalHeightLeft, 13)
        self.assertEqual(CoreAudio.kAudioChannelLabel_VerticalHeightCenter, 14)
        self.assertEqual(CoreAudio.kAudioChannelLabel_VerticalHeightRight, 15)
        self.assertEqual(CoreAudio.kAudioChannelLabel_TopBackLeft, 16)
        self.assertEqual(CoreAudio.kAudioChannelLabel_TopBackCenter, 17)
        self.assertEqual(CoreAudio.kAudioChannelLabel_TopBackRight, 18)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RearSurroundLeft, 33)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RearSurroundRight, 34)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LeftWide, 35)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RightWide, 36)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LFE2, 37)
        self.assertEqual(CoreAudio.kAudioChannelLabel_LeftTotal, 38)
        self.assertEqual(CoreAudio.kAudioChannelLabel_RightTotal, 39)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HearingImpaired, 40)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Narration, 41)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Mono, 42)
        self.assertEqual(CoreAudio.kAudioChannelLabel_DialogCentricMix, 43)
        self.assertEqual(CoreAudio.kAudioChannelLabel_CenterSurroundDirect, 44)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Haptic, 45)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Ambisonic_W, 200)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Ambisonic_X, 201)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Ambisonic_Y, 202)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Ambisonic_Z, 203)
        self.assertEqual(CoreAudio.kAudioChannelLabel_MS_Mid, 204)
        self.assertEqual(CoreAudio.kAudioChannelLabel_MS_Side, 205)
        self.assertEqual(CoreAudio.kAudioChannelLabel_XY_X, 206)
        self.assertEqual(CoreAudio.kAudioChannelLabel_XY_Y, 207)
        self.assertEqual(CoreAudio.kAudioChannelLabel_BinauralLeft, 208)
        self.assertEqual(CoreAudio.kAudioChannelLabel_BinauralRight, 209)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HeadphonesLeft, 301)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HeadphonesRight, 302)
        self.assertEqual(CoreAudio.kAudioChannelLabel_ClickTrack, 304)
        self.assertEqual(CoreAudio.kAudioChannelLabel_ForeignLanguage, 305)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete, 400)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_0, (1 << 16) | 0)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_1, (1 << 16) | 1)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_2, (1 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_3, (1 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_4, (1 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_5, (1 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_6, (1 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_7, (1 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_8, (1 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_9, (1 << 16) | 9)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_10, (1 << 16) | 10)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_11, (1 << 16) | 11)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_12, (1 << 16) | 12)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_13, (1 << 16) | 13)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_14, (1 << 16) | 14)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_15, (1 << 16) | 15)
        self.assertEqual(CoreAudio.kAudioChannelLabel_Discrete_65535, (1 << 16) | 65535)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN, 500)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_0, (2 << 16) | 0)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_1, (2 << 16) | 1)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_2, (2 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_3, (2 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_4, (2 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_5, (2 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_6, (2 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_7, (2 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_8, (2 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_9, (2 << 16) | 9)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_10, (2 << 16) | 10)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_11, (2 << 16) | 11)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_12, (2 << 16) | 12)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_13, (2 << 16) | 13)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_14, (2 << 16) | 14)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_15, (2 << 16) | 15)
        self.assertEqual(CoreAudio.kAudioChannelLabel_HOA_ACN_65024, (2 << 16) | 65024)
        self.assertEqual(CoreAudio.kAudioChannelLabel_BeginReserved, 0xF0000000)
        self.assertEqual(CoreAudio.kAudioChannelLabel_EndReserved, 0xFFFFFFFE)
        self.assertEqual(CoreAudio.kAudioChannelBit_Left, 1 << 0)
        self.assertEqual(CoreAudio.kAudioChannelBit_Right, 1 << 1)
        self.assertEqual(CoreAudio.kAudioChannelBit_Center, 1 << 2)
        self.assertEqual(CoreAudio.kAudioChannelBit_LFEScreen, 1 << 3)
        self.assertEqual(CoreAudio.kAudioChannelBit_LeftSurround, 1 << 4)
        self.assertEqual(CoreAudio.kAudioChannelBit_RightSurround, 1 << 5)
        self.assertEqual(CoreAudio.kAudioChannelBit_LeftCenter, 1 << 6)
        self.assertEqual(CoreAudio.kAudioChannelBit_RightCenter, 1 << 7)
        self.assertEqual(CoreAudio.kAudioChannelBit_CenterSurround, 1 << 8)
        self.assertEqual(CoreAudio.kAudioChannelBit_LeftSurroundDirect, 1 << 9)
        self.assertEqual(CoreAudio.kAudioChannelBit_RightSurroundDirect, 1 << 10)
        self.assertEqual(CoreAudio.kAudioChannelBit_TopCenterSurround, 1 << 11)
        self.assertEqual(CoreAudio.kAudioChannelBit_VerticalHeightLeft, 1 << 12)
        self.assertEqual(CoreAudio.kAudioChannelBit_VerticalHeightCenter, 1 << 13)
        self.assertEqual(CoreAudio.kAudioChannelBit_VerticalHeightRight, 1 << 14)
        self.assertEqual(CoreAudio.kAudioChannelBit_TopBackLeft, 1 << 15)
        self.assertEqual(CoreAudio.kAudioChannelBit_TopBackCenter, 1 << 16)
        self.assertEqual(CoreAudio.kAudioChannelBit_TopBackRight, 1 << 17)
        self.assertEqual(CoreAudio.kAudioChannelFlags_AllOff, 0)
        self.assertEqual(CoreAudio.kAudioChannelFlags_RectangularCoordinates, 1 << 0)
        self.assertEqual(CoreAudio.kAudioChannelFlags_SphericalCoordinates, 1 << 1)
        self.assertEqual(CoreAudio.kAudioChannelFlags_Meters, 1 << 2)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_LeftRight, 0)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_BackFront, 1)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_DownUp, 2)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_Azimuth, 0)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_Elevation, 1)
        self.assertEqual(CoreAudio.kAudioChannelCoordinates_Distance, 2)

        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_UseChannelDescriptions, (0 << 16) | 0
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_UseChannelBitmap, (1 << 16) | 0
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Mono, (100 << 16) | 1)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Stereo, (101 << 16) | 2)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_StereoHeadphones, (102 << 16) | 2
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MatrixStereo, (103 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MidSide, (104 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_XY, (105 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Binaural, (106 << 16) | 2)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_Ambisonic_B_Format, (107 << 16) | 4
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Quadraphonic, (108 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Pentagonal, (109 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Hexagonal, (110 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Octagonal, (111 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Cube, (112 << 16) | 8)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_MPEG_1_0,
            CoreAudio.kAudioChannelLayoutTag_Mono,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_MPEG_2_0,
            CoreAudio.kAudioChannelLayoutTag_Stereo,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_3_0_A, (113 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_3_0_B, (114 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_4_0_A, (115 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_4_0_B, (116 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_A, (117 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_B, (118 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_C, (119 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_D, (120 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_A, (121 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_B, (122 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_C, (123 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_D, (124 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_6_1_A, (125 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_A, (126 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_B, (127 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_C, (128 << 16) | 8)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_Emagic_Default_7_1, (129 << 16) | 8
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_SMPTE_DTV, (130 << 16) | 8)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_1_0,
            CoreAudio.kAudioChannelLayoutTag_Mono,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_2_0,
            CoreAudio.kAudioChannelLayoutTag_Stereo,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_ITU_2_1, (131 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_ITU_2_2, (132 << 16) | 4)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_3_0,
            CoreAudio.kAudioChannelLayoutTag_MPEG_3_0_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_3_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_4_0_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_3_2,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_3_2_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_ITU_3_4_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_C,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_0,
            CoreAudio.kAudioChannelLayoutTag_Mono,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_1,
            CoreAudio.kAudioChannelLayoutTag_Stereo,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_2,
            CoreAudio.kAudioChannelLayoutTag_ITU_2_1,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_3,
            CoreAudio.kAudioChannelLayoutTag_ITU_2_2,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_4, (133 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_5, (134 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_6, (135 << 16) | 5)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_7,
            CoreAudio.kAudioChannelLayoutTag_MPEG_3_0_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_8,
            CoreAudio.kAudioChannelLayoutTag_MPEG_4_0_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_9,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_A,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_10, (136 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_11, (137 << 16) | 5)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_12,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_13,
            CoreAudio.kAudioChannelLayoutTag_DVD_8,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_14,
            CoreAudio.kAudioChannelLayoutTag_DVD_9,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_15,
            CoreAudio.kAudioChannelLayoutTag_DVD_10,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_16,
            CoreAudio.kAudioChannelLayoutTag_DVD_11,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_17,
            CoreAudio.kAudioChannelLayoutTag_DVD_12,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DVD_18, (138 << 16) | 5)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_19,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_B,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DVD_20,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_B,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_4,
            CoreAudio.kAudioChannelLayoutTag_Quadraphonic,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_5,
            CoreAudio.kAudioChannelLayoutTag_Pentagonal,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_6,
            CoreAudio.kAudioChannelLayoutTag_Hexagonal,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_8,
            CoreAudio.kAudioChannelLayoutTag_Octagonal,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_5_0,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_B,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_6_0, (139 << 16) | 6
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_7_0, (140 << 16) | 7
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_7_0_Front, (148 << 16) | 7
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_5_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_6_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_6_1_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_7_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_C,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AudioUnit_7_1_Front,
            CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_A,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_3_0,
            CoreAudio.kAudioChannelLayoutTag_MPEG_3_0_B,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_Quadraphonic,
            CoreAudio.kAudioChannelLayoutTag_Quadraphonic,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_4_0,
            CoreAudio.kAudioChannelLayoutTag_MPEG_4_0_B,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_5_0,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_0_D,
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_5_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_5_1_D,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AAC_6_0, (141 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AAC_6_1, (142 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AAC_7_0, (143 << 16) | 7)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_7_1,
            CoreAudio.kAudioChannelLayoutTag_MPEG_7_1_B,
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AAC_7_1_B, (183 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AAC_7_1_C, (184 << 16) | 8)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_AAC_Octagonal, (144 << 16) | 8
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_TMH_10_2_std, (145 << 16) | 16
        )
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_TMH_10_2_full, (146 << 16) | 21
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_1_0_1, (149 << 16) | 2)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_3_0, (150 << 16) | 3)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_3_1, (151 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_3_0_1, (152 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_2_1_1, (153 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_AC3_3_1_1, (154 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC_6_0_A, (155 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC_7_0_A, (156 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_6_1_A, (157 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_6_1_B, (158 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_6_1_C, (159 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_A, (160 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_B, (161 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_C, (162 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_D, (163 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_E, (164 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_F, (165 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_G, (166 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EAC3_7_1_H, (167 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_3_1, (168 << 16) | 4)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_4_1, (169 << 16) | 5)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_0_A, (170 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_0_B, (171 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_0_C, (172 << 16) | 6)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_1_A, (173 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_1_B, (174 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_1_C, (175 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_7_0, (176 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_7_1, (177 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_8_0_A, (178 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_8_0_B, (179 << 16) | 8)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_8_1_A, (180 << 16) | 9)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_8_1_B, (181 << 16) | 9)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_DTS_6_1_D, (182 << 16) | 7)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_HOA_ACN_SN3D, (190 << 16) | 0)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_HOA_ACN_N3D, (191 << 16) | 0)
        self.assertEqual(
            CoreAudio.kAudioChannelLayoutTag_DiscreteInOrder, (147 << 16) | 0
        )
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_BeginReserved, 0xF0000000)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_EndReserved, 0xFFFEFFFF)
        self.assertEqual(CoreAudio.kAudioChannelLayoutTag_Unknown, 0xFFFF0000)

        self.assertEqual(CoreAudio.kMPEG4Object_AAC_Main, 1)
        self.assertEqual(CoreAudio.kMPEG4Object_AAC_LC, 2)
        self.assertEqual(CoreAudio.kMPEG4Object_AAC_SSR, 3)
        self.assertEqual(CoreAudio.kMPEG4Object_AAC_LTP, 4)
        self.assertEqual(CoreAudio.kMPEG4Object_AAC_SBR, 5)
        self.assertEqual(CoreAudio.kMPEG4Object_AAC_Scalable, 6)
        self.assertEqual(CoreAudio.kMPEG4Object_TwinVQ, 7)
        self.assertEqual(CoreAudio.kMPEG4Object_CELP, 8)
        self.assertEqual(CoreAudio.kMPEG4Object_HVXC, 9)

    def testStructs(self):
        v = CoreAudio.AudioValueRange()
        self.assertEqual(v.mMinimum, 0.0)
        self.assertEqual(v.mMaximum, 0.0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.AudioStreamBasicDescription()
        self.assertEqual(v.mSampleRate, 0.0)
        self.assertEqual(v.mFormatID, 0)
        self.assertEqual(v.mFormatFlags, 0)
        self.assertEqual(v.mBytesPerPacket, 0)
        self.assertEqual(v.mFramesPerPacket, 0)
        self.assertEqual(v.mBytesPerFrame, 0)
        self.assertEqual(v.mChannelsPerFrame, 0)
        self.assertEqual(v.mBitsPerChannel, 0)
        self.assertEqual(v.mReserved, 0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.AudioStreamPacketDescription()
        self.assertEqual(v.mStartOffset, 0)
        self.assertEqual(v.mVariableFramesInPacket, 0)
        self.assertEqual(v.mDataByteSize, 0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.SMPTETime()
        self.assertEqual(v.mSubframes, 0)
        self.assertEqual(v.mSubframeDivisor, 0)
        self.assertEqual(v.mCounter, 0)
        self.assertEqual(v.mType, 0)
        self.assertEqual(v.mFlags, 0)
        self.assertEqual(v.mHours, 0)
        self.assertEqual(v.mMinutes, 0)
        self.assertEqual(v.mSeconds, 0)
        self.assertEqual(v.mFrames, 0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.AudioTimeStamp()
        self.assertEqual(v.mSampleTime, 0.0)
        self.assertEqual(v.mHostTime, 0)
        self.assertEqual(v.mRateScalar, 0.0)
        self.assertEqual(v.mWordClockTime, 0)
        self.assertEqual(v.mSMPTETime, CoreAudio.SMPTETime())
        self.assertEqual(v.mFlags, 0)
        self.assertEqual(v.mReserved, 0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.AudioClassDescription()
        self.assertEqual(v.mType, 0)
        self.assertEqual(v.mSubType, 0)
        self.assertEqual(v.mManufacturer, 0)
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
        CoreAudio.TestAudioFormatNativeEndian

        self.assertArgIsIn(CoreAudio.IsAudioFormatNativeEndian, 0)
        self.assertResultHasType(CoreAudio.IsAudioFormatNativeEndian, objc._C_BOOL)

        self.assertArgHasType(CoreAudio.CalculateLPCMFlags, 2, objc._C_BOOL)
        self.assertArgHasType(CoreAudio.CalculateLPCMFlags, 3, objc._C_BOOL)
        self.assertArgHasType(CoreAudio.CalculateLPCMFlags, 4, objc._C_BOOL)

        self.assertArgIsOut(CoreAudio.FillOutASBDForLPCM, 0)
        self.assertArgHasType(CoreAudio.FillOutASBDForLPCM, 5, objc._C_BOOL)
        self.assertArgHasType(CoreAudio.FillOutASBDForLPCM, 6, objc._C_BOOL)
        self.assertArgHasType(CoreAudio.FillOutASBDForLPCM, 7, objc._C_BOOL)

        self.assertArgIsOut(CoreAudio.FillOutAudioTimeStampWithSampleTime, 0)
        self.assertArgIsOut(CoreAudio.FillOutAudioTimeStampWithHostTime, 0)
        self.assertArgIsOut(CoreAudio.FillOutAudioTimeStampWithSampleAndHostTime, 0)

    @min_os_level("10.11")
    def test_functions10_11(self):
        CoreAudio.AudioChannelLayoutTag_GetNumberOfChannels


class TestManualWrappers(TestCase):
    def assert_buffer_size(self, buf, size):
        self.assertIsInstance(buf, memoryview)
        self.assertEqual(buf.itemsize, 1)
        self.assertEqual(buf.nbytes, size)

    def testAudioBuffer(self):
        buf = CoreAudio.AudioBuffer()
        self.assertEqual(buf.mNumberChannels, 1)
        self.assertEqual(buf.mData, None)

        buf = CoreAudio.AudioBuffer(num_channels=50)
        self.assertEqual(buf.mNumberChannels, 50)
        self.assertEqual(buf.mData, None)

        buf = CoreAudio.AudioBuffer(num_channels=5, buffer_size=1024)
        self.assertEqual(buf.mNumberChannels, 5)
        v = buf.mData
        self.assert_buffer_size(v, 1024)

        buf.create_buffer(2048)
        v2 = buf.mData
        self.assert_buffer_size(v2, 2048)

    def testAudioBufferList(self):
        bl = CoreAudio.AudioBufferList(2)
        self.assertEqual(len(bl), 2)

        i0 = bl[0]
        i1 = bl[1]
        i_m1 = bl[-1]
        i_m2 = bl[-2]

        self.assertIs(i0, i_m2)
        self.assertIs(i1, i_m1)

        self.assertIsNot(i0, i1)

        self.assertIsInstance(i0, CoreAudio.AudioBuffer)
        self.assertIsInstance(i1, CoreAudio.AudioBuffer)

        with self.assertRaises(IndexError):
            bl[2]

        with self.assertRaises(IndexError):
            bl[-4]

    def testAudioValueTranslation(self):
        avt = CoreAudio.AudioValueTranslation()
        self.assertEqual(avt.mInputDataSize, 0)
        self.assertEqual(avt.mInputData, None)
        self.assertEqual(avt.mInputDataSize, 0)
        self.assertEqual(avt.mOutputData, None)
        self.assertEqual(avt.mOutputDataSize, 0)

        avt.create_input_buffer(1024)

        self.assertEqual(avt.mInputDataSize, 1024)
        v = avt.mInputData
        self.assert_buffer_size(v, 1024)

        self.assertEqual(avt.mOutputData, None)
        self.assertEqual(avt.mOutputDataSize, 0)

        avt.create_output_buffer(2048)

        self.assertEqual(avt.mInputDataSize, 1024)
        v = avt.mInputData
        self.assert_buffer_size(v, 1024)

        self.assertEqual(avt.mOutputDataSize, 2048)
        v = avt.mOutputData
        self.assert_buffer_size(v, 2048)

        avt = CoreAudio.AudioValueTranslation(input_buffer_size=50)

        self.assertEqual(avt.mInputDataSize, 50)
        v = avt.mInputData
        self.assert_buffer_size(v, 50)

        self.assertEqual(avt.mOutputData, None)
        self.assertEqual(avt.mOutputDataSize, 0)

        avt = CoreAudio.AudioValueTranslation(output_buffer_size=40)

        self.assertEqual(avt.mOutputDataSize, 40)
        v = avt.mOutputData
        self.assert_buffer_size(v, 40)

        self.assertEqual(avt.mInputData, None)
        self.assertEqual(avt.mInputDataSize, 0)

    def test_AudioChannelDescription(self):
        v = CoreAudio.AudioChannelDescription()
        self.assertEqual(v.mChannelLabel, 0)
        self.assertEqual(v.mChannelFlags, 0)
        self.assertEqual(v.mCoordinates, (0.0, 0.0, 0.0))

        v = CoreAudio.AudioChannelDescription(
            mChannelLabel=1, mChannelFlags=2, mCoordinates=(5, 6, 7)
        )
        self.assertEqual(v.mChannelLabel, 1)
        self.assertEqual(v.mChannelFlags, 2)
        self.assertEqual(v.mCoordinates, (5.0, 6.0, 7.0))

    def test_AudioChannelLayout(self):

        with self.assertRaises(TypeError):
            v = CoreAudio.AudioChannelLayout()

        v = CoreAudio.AudioChannelLayout(num_channels=2)
        self.assertEqual(v.mChannelLayoutTag, 0)
        self.assertEqual(v.mChannelBitmap, 0)
        self.assertEqual(len(v), 2)

        i0 = v[0]
        i1 = v[1]

        i_m1 = v[-1]
        i_m2 = v[-2]

        self.assertIs(i0, i_m2)
        self.assertIs(i1, i_m1)

        self.assertIsNot(i0, i1)

        with self.assertRaises(IndexError):
            v[2]

        with self.assertRaises(IndexError):
            v[-4]
