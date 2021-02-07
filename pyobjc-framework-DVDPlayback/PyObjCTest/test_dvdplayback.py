import DVDPlayback
from PyObjCTools.TestSupport import TestCase, fourcc

DVDFatalErrCallBackFunctionPtr = b"vi^v"
DVDEventCallBackFunctionPtr = b"vILL^v"


class TestDVDPlayback(TestCase):
    def testConstants(self):
        self.assertEqual(DVDPlayback.kDVDErrorUnknown, -70001)
        self.assertEqual(DVDPlayback.kDVDErrorInitializingLib, -70002)
        self.assertEqual(DVDPlayback.kDVDErrorUninitializedLib, -70003)
        self.assertEqual(DVDPlayback.kDVDErrorNotAllowedDuringPlayback, -70004)
        self.assertEqual(DVDPlayback.kDVDErrorUnassignedGrafPort, -70005)
        self.assertEqual(DVDPlayback.kDVDErrorAlreadyPlaying, -70006)
        self.assertEqual(DVDPlayback.kDVDErrorNoFatalErrCallBack, -70007)
        self.assertEqual(DVDPlayback.kDVDErrorIsAlreadySleeping, -70008)
        self.assertEqual(DVDPlayback.kDVDErrorDontNeedWakeup, -70009)
        self.assertEqual(DVDPlayback.kDVDErrorTimeOutOfRange, -70010)
        self.assertEqual(DVDPlayback.kDVDErrorUserActionNoOp, -70011)
        self.assertEqual(DVDPlayback.kDVDErrorMissingDrive, -70012)
        self.assertEqual(DVDPlayback.kDVDErrorNotSupportedConfiguration, -70013)
        self.assertEqual(DVDPlayback.kDVDErrorNotSupportedFunction, -70014)
        self.assertEqual(DVDPlayback.kDVDErrorNoValidMedia, -70015)
        self.assertEqual(DVDPlayback.kDVDErrorWrongParam, -70016)
        self.assertEqual(DVDPlayback.kDVDErrorMissingGraphicsDevice, -70017)
        self.assertEqual(DVDPlayback.kDVDErrorGraphicsDevice, -70018)
        self.assertEqual(DVDPlayback.kDVDErrorPlaybackOpen, -70019)
        self.assertEqual(DVDPlayback.kDVDErrorInvalidRegionCode, -70020)
        self.assertEqual(DVDPlayback.kDVDErrorRgnMgrInstall, -70021)
        self.assertEqual(DVDPlayback.kDVDErrorMismatchedRegionCode, -70022)
        self.assertEqual(DVDPlayback.kDVDErrorNoMoreRegionSets, -70023)
        self.assertEqual(DVDPlayback.kDVDErrordRegionCodeUninitialized, -70024)
        self.assertEqual(DVDPlayback.kDVDErrorAuthentification, -70025)
        self.assertEqual(DVDPlayback.kDVDErrorOutOfVideoMemory, -70026)
        self.assertEqual(DVDPlayback.kDVDErrorNoAudioOutputDevice, -70027)
        self.assertEqual(DVDPlayback.kDVDErrorSystem, -70028)
        self.assertEqual(DVDPlayback.kDVDErrorNavigation, -70029)
        self.assertEqual(DVDPlayback.kDVDErrorInvalidBookmarkVersion, -70030)
        self.assertEqual(DVDPlayback.kDVDErrorInvalidBookmarkSize, -70031)
        self.assertEqual(DVDPlayback.kDVDErrorInvalidBookmarkForMedia, -70032)
        self.assertEqual(DVDPlayback.kDVDErrorNoValidBookmarkForLastPlay, -70033)
        self.assertEqual(DVDPlayback.kDVDErrorDisplayAuthentification, -70034)

        self.assertEqual(DVDPlayback.kDVDStateUnknown, 0)
        self.assertEqual(DVDPlayback.kDVDStatePlaying, 1)
        self.assertEqual(DVDPlayback.kDVDStatePlayingStill, 2)
        self.assertEqual(DVDPlayback.kDVDStatePaused, 3)
        self.assertEqual(DVDPlayback.kDVDStateStopped, 4)
        self.assertEqual(DVDPlayback.kDVDStateScanning, 5)
        self.assertEqual(DVDPlayback.kDVDStateIdle, 6)
        self.assertEqual(DVDPlayback.kDVDStatePlayingSlow, 7)

        self.assertEqual(DVDPlayback.kDVDMenuTitle, 0)
        self.assertEqual(DVDPlayback.kDVDMenuRoot, 1)
        self.assertEqual(DVDPlayback.kDVDMenuSubPicture, 2)
        self.assertEqual(DVDPlayback.kDVDMenuAudio, 3)
        self.assertEqual(DVDPlayback.kDVDMenuAngle, 4)
        self.assertEqual(DVDPlayback.kDVDMenuPTT, 5)
        self.assertEqual(DVDPlayback.kDVDMenuNone, 6)

        self.assertEqual(DVDPlayback.kDVDTimeCodeUninitialized, 0)
        self.assertEqual(DVDPlayback.kDVDTimeCodeElapsedSeconds, 1)
        self.assertEqual(DVDPlayback.kDVDTimeCodeRemainingSeconds, 2)
        self.assertEqual(DVDPlayback.kDVDTimeCodeTitleDurationSeconds, 3)
        self.assertEqual(DVDPlayback.kDVDTimeCodeChapterElapsedSeconds, 4)
        self.assertEqual(DVDPlayback.kDVDTimeCodeChapterRemainingSeconds, 5)
        self.assertEqual(DVDPlayback.kDVDTimeCodeChapterDurationSeconds, 6)

        self.assertEqual(DVDPlayback.kDVDScanDirectionForward, 0)
        self.assertEqual(DVDPlayback.kDVDScanDirectionBackward, 1)

        self.assertEqual(DVDPlayback.kDVDScanRateOneEigth, -8)
        self.assertEqual(DVDPlayback.kDVDScanRateOneFourth, -4)
        self.assertEqual(DVDPlayback.kDVDScanRateOneHalf, -2)
        self.assertEqual(DVDPlayback.kDVDScanRate1x, 1)
        self.assertEqual(DVDPlayback.kDVDScanRate2x, 2)
        self.assertEqual(DVDPlayback.kDVDScanRate4x, 4)
        self.assertEqual(DVDPlayback.kDVDScanRate8x, 8)
        self.assertEqual(DVDPlayback.kDVDScanRate16x, 16)
        self.assertEqual(DVDPlayback.kDVDScanRate32x, 32)

        self.assertEqual(DVDPlayback.kDVDAspectRatioUninitialized, 0)
        self.assertEqual(DVDPlayback.kDVDAspectRatio4x3, 1)
        self.assertEqual(DVDPlayback.kDVDAspectRatio4x3PanAndScan, 2)
        self.assertEqual(DVDPlayback.kDVDAspectRatio16x9, 3)
        self.assertEqual(DVDPlayback.kDVDAspectRatioLetterBox, 4)

        self.assertEqual(DVDPlayback.kDVDFormatUninitialized, 0)
        self.assertEqual(DVDPlayback.kDVDFormatNTSC, 1)
        self.assertEqual(DVDPlayback.kDVDFormatPAL, 2)
        self.assertEqual(DVDPlayback.kDVDFormatNTSC_HDTV, 3)
        self.assertEqual(DVDPlayback.kDVDFormatPAL_HDTV, 4)

        self.assertEqual(DVDPlayback.kDVDAudioModeUninitialized, 0)
        self.assertEqual(DVDPlayback.kDVDAudioModeProLogic, 1 << 0)
        self.assertEqual(DVDPlayback.kDVDAudioModeSPDIF, 1 << 1)

        self.assertEqual(DVDPlayback.kDVDAudioUnknownFormat, 0)
        self.assertEqual(DVDPlayback.kDVDAudioAC3Format, 1)
        self.assertEqual(DVDPlayback.kDVDAudioMPEG1Format, 2)
        self.assertEqual(DVDPlayback.kDVDAudioMPEG2Format, 3)
        self.assertEqual(DVDPlayback.kDVDAudioPCMFormat, 4)
        self.assertEqual(DVDPlayback.kDVDAudioDTSFormat, 5)
        self.assertEqual(DVDPlayback.kDVDAudioSDDSFormat, 6)
        self.assertEqual(DVDPlayback.kDVDAudioMLPFormat, 7)
        self.assertEqual(DVDPlayback.kDVDAudioDDPlusFormat, 8)
        self.assertEqual(DVDPlayback.kDVDAudioDTSHDFormat, 9)

        self.assertEqual(DVDPlayback.kDVDLanguageCodeUninitialized, fourcc(b"??  "))
        self.assertEqual(DVDPlayback.kDVDLanguageNoPreference, fourcc(b"**  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeNone, fourcc(b"00  "))

        self.assertEqual(DVDPlayback.kDVDLanguageCodeAfar, fourcc(b"aa  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAbkhazian, fourcc(b"ab  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAfrikaans, fourcc(b"af  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAmharic, fourcc(b"am  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeArabic, fourcc(b"ar  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAssamese, fourcc(b"as  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAymara, fourcc(b"ay  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAzerbaijani, fourcc(b"az  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBashkir, fourcc(b"ba  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeByelorussian, fourcc(b"be  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBulgarian, fourcc(b"bg  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBihari, fourcc(b"bh  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBislama, fourcc(b"bi  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBengali, fourcc(b"bn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTibetan, fourcc(b"bo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBreton, fourcc(b"br  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeCatalan, fourcc(b"ca  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeCorsican, fourcc(b"co  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeCzech, fourcc(b"cs  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeWelsh, fourcc(b"cy  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeDanish, fourcc(b"da  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGerman, fourcc(b"de  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBhutani, fourcc(b"dz  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGreek, fourcc(b"el  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeEnglish, fourcc(b"en  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeEsperanto, fourcc(b"eo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSpanish, fourcc(b"es  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeEstonian, fourcc(b"et  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBasque, fourcc(b"eu  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodePersian, fourcc(b"fa  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeFinnish, fourcc(b"fi  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeFiji, fourcc(b"fj  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeFaeroese, fourcc(b"fo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeFrench, fourcc(b"fr  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeFrisian, fourcc(b"fy  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeIrish, fourcc(b"ga  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeScotsGaelic, fourcc(b"gd  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGalician, fourcc(b"gl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGuarani, fourcc(b"gn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGujarati, fourcc(b"gu  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeHausa, fourcc(b"ha  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeHindi, fourcc(b"hi  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeCroatian, fourcc(b"hr  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeHungarian, fourcc(b"hu  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeArmenian, fourcc(b"hy  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeInterlingua, fourcc(b"ia  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeInterlingue, fourcc(b"ie  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeInupiak, fourcc(b"ik  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeIndonesian, fourcc(b"in  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeIcelandic, fourcc(b"is  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeItalian, fourcc(b"it  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeHebrew, fourcc(b"iw  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeJapanese, fourcc(b"ja  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeYiddish, fourcc(b"ji  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeJavanese, fourcc(b"jw  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGeorgian, fourcc(b"ka  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKazakh, fourcc(b"kk  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeGreenlandic, fourcc(b"kl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeCambodian, fourcc(b"km  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKannada, fourcc(b"kn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKorean, fourcc(b"ko  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKashmiri, fourcc(b"ks  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKurdish, fourcc(b"ku  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKirghiz, fourcc(b"ky  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeLatin, fourcc(b"la  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeLingala, fourcc(b"ln  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeLaothian, fourcc(b"lo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeLithuanian, fourcc(b"lt  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeLatvian, fourcc(b"lv  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMalagasy, fourcc(b"mg  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMaori, fourcc(b"mi  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMacedonian, fourcc(b"mk  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMalayalam, fourcc(b"ml  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMongolian, fourcc(b"mn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMoldavian, fourcc(b"mo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMarathi, fourcc(b"mr  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMalay, fourcc(b"ms  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeMaltese, fourcc(b"mt  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeBurmese, fourcc(b"my  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeNauru, fourcc(b"na  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeNepali, fourcc(b"ne  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeDutch, fourcc(b"nl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeNorwegian, fourcc(b"no  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeOccitan, fourcc(b"oc  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeOromo, fourcc(b"om  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeOriya, fourcc(b"or  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodePunjabi, fourcc(b"pa  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodePolish, fourcc(b"pl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodePashto, fourcc(b"ps  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodePortugese, fourcc(b"pt  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeQuechua, fourcc(b"qu  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeRhaetoRomance, fourcc(b"rm  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKirundi, fourcc(b"rn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeRomanian, fourcc(b"ro  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeRussian, fourcc(b"ru  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeKinyarwanda, fourcc(b"rw  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSanskrit, fourcc(b"sa  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSindhi, fourcc(b"sd  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSangro, fourcc(b"sg  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSerboCroatian, fourcc(b"sh  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSinghalese, fourcc(b"si  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSlovak, fourcc(b"sk  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSlovenian, fourcc(b"sl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSamoan, fourcc(b"sm  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeShona, fourcc(b"sn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSomali, fourcc(b"so  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeAlbanian, fourcc(b"sq  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSerbian, fourcc(b"sr  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSiswati, fourcc(b"ss  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSesotho, fourcc(b"st  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSudanese, fourcc(b"su  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSwedish, fourcc(b"sv  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSwahili, fourcc(b"sw  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTamil, fourcc(b"ta  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTelugu, fourcc(b"te  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTajik, fourcc(b"tg  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeThai, fourcc(b"th  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTigrinya, fourcc(b"ti  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTurkmen, fourcc(b"tk  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTagalog, fourcc(b"tl  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeSetswana, fourcc(b"tn  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTonga, fourcc(b"to  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTurkish, fourcc(b"tr  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTsonga, fourcc(b"ts  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTatar, fourcc(b"tt  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeTwi, fourcc(b"tw  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeUkranian, fourcc(b"uk  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeUrdu, fourcc(b"ur  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeUzbek, fourcc(b"uz  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeVietnamese, fourcc(b"vi  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeVolapuk, fourcc(b"vo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeWolof, fourcc(b"wo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeXhosa, fourcc(b"xh  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeYoruba, fourcc(b"yo  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeChinese, fourcc(b"zh  "))
        self.assertEqual(DVDPlayback.kDVDLanguageCodeZulu, fourcc(b"zu  "))

        self.assertEqual(DVDPlayback.kDVDAudioExtensionCodeNotSpecified, 0)
        self.assertEqual(DVDPlayback.kDVDAudioExtensionCodeNormalCaptions, 1)
        self.assertEqual(DVDPlayback.kDVDAudioExtensionCodeNVisualImpaired, 2)
        self.assertEqual(DVDPlayback.kDVDAudioExtensionCodeDirectorsComment1, 3)
        self.assertEqual(DVDPlayback.kDVDAudioExtensionCodeDirectorsComment2, 4)

        self.assertEqual(DVDPlayback.kDVDSubpictureExtensionCodeNotSpecified, 0)
        self.assertEqual(DVDPlayback.kDVDSubpictureExtensionCodeCaptionNormalSize, 1)
        self.assertEqual(DVDPlayback.kDVDSubpictureExtensionCodeCaptionBiggerSize, 2)
        self.assertEqual(DVDPlayback.kDVDSubpictureExtensionCodeCaption4Children, 3)
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionCodeClosedCaptionNormalSize, 5
        )
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionCodeClosedCaptionBiggerSize, 6
        )
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionCodeClosedCaption4Children, 7
        )
        self.assertEqual(DVDPlayback.kDVDSubpictureExtensionCodeForcedCaption, 9)
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionDirectorsCommentNormalSize, 13
        )
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionDirectorsCommentBiggerSize, 14
        )
        self.assertEqual(
            DVDPlayback.kDVDSubpictureExtensionDirectorsComment4Children, 15
        )

        self.assertEqual(DVDPlayback.kDVDRegionCodeUninitialized, 0xFF)
        self.assertEqual(DVDPlayback.kDVDRegionCode1, 0xFE)
        self.assertEqual(DVDPlayback.kDVDRegionCode2, 0xFD)
        self.assertEqual(DVDPlayback.kDVDRegionCode3, 0xFB)
        self.assertEqual(DVDPlayback.kDVDRegionCode4, 0xF7)
        self.assertEqual(DVDPlayback.kDVDRegionCode5, 0xEF)
        self.assertEqual(DVDPlayback.kDVDRegionCode6, 0xDF)
        self.assertEqual(DVDPlayback.kDVDRegionCode7, 0xBF)
        self.assertEqual(DVDPlayback.kDVDRegionCode8, 0x7F)

        self.assertEqual(DVDPlayback.kDVDFPDomain, 0)
        self.assertEqual(DVDPlayback.kDVDVMGMDomain, 1)
        self.assertEqual(DVDPlayback.kDVDVTSMDomain, 2)
        self.assertEqual(DVDPlayback.kDVDTTDomain, 3)
        self.assertEqual(DVDPlayback.kDVDSTOPDomain, 4)
        self.assertEqual(DVDPlayback.kDVDAMGMDomain, 5)
        self.assertEqual(DVDPlayback.kDVDTTGRDomain, 6)

        self.assertEqual(DVDPlayback.kDVDUOPTimePlaySearch, 0x00000001)
        self.assertEqual(DVDPlayback.kDVDUOPPTTPlaySearch, 0x00000002)
        self.assertEqual(DVDPlayback.kDVDUOPTitlePlay, 0x00000004)
        self.assertEqual(DVDPlayback.kDVDUOPStop, 0x00000008)
        self.assertEqual(DVDPlayback.kDVDUOPGoUp, 0x00000010)
        self.assertEqual(DVDPlayback.kDVDUOPTimePTTSearch, 0x00000020)
        self.assertEqual(DVDPlayback.kDVDUOPPrevTopPGSearch, 0x00000040)
        self.assertEqual(DVDPlayback.kDVDUOPNextPGSearch, 0x00000080)
        self.assertEqual(DVDPlayback.kDVDUOPForwardScan, 0x00000100)
        self.assertEqual(DVDPlayback.kDVDUOPBackwardScan, 0x00000200)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallTitle, 0x00000400)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallRoot, 0x00000800)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallSubPicture, 0x00001000)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallAudio, 0x00002000)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallAngle, 0x00004000)
        self.assertEqual(DVDPlayback.kDVDUOPMenuCallPTT, 0x00008000)
        self.assertEqual(DVDPlayback.kDVDUOPResume, 0x00010000)
        self.assertEqual(DVDPlayback.kDVDUOPButton, 0x00020000)
        self.assertEqual(DVDPlayback.kDVDUOPStillOff, 0x00040000)
        self.assertEqual(DVDPlayback.kDVDUOPPauseOn, 0x00080000)
        self.assertEqual(DVDPlayback.kDVDUOPAudioStreamChange, 0x00100000)
        self.assertEqual(DVDPlayback.kDVDUOPSubPictureStreamChange, 0x00200000)
        self.assertEqual(DVDPlayback.kDVDUOPAngleChange, 0x00400000)
        self.assertEqual(DVDPlayback.kDVDUOPKaraokeModeChange, 0x00800000)
        self.assertEqual(DVDPlayback.kDVDUOPVideoModeChange, 0x01000000)
        self.assertEqual(DVDPlayback.kDVDUOPScanOff, 0x02000000)
        self.assertEqual(DVDPlayback.kDVDUOPPauseOff, 0x04000000)

        self.assertEqual(DVDPlayback.kDVDEventTitle, 1)
        self.assertEqual(DVDPlayback.kDVDEventPTT, 2)
        self.assertEqual(DVDPlayback.kDVDEventValidUOP, 3)
        self.assertEqual(DVDPlayback.kDVDEventAngle, 4)
        self.assertEqual(DVDPlayback.kDVDEventAudioStream, 5)
        self.assertEqual(DVDPlayback.kDVDEventSubpictureStream, 6)
        self.assertEqual(DVDPlayback.kDVDEventDisplayMode, 7)
        self.assertEqual(DVDPlayback.kDVDEventDomain, 8)
        self.assertEqual(DVDPlayback.kDVDEventBitrate, 9)
        self.assertEqual(DVDPlayback.kDVDEventStill, 10)
        self.assertEqual(DVDPlayback.kDVDEventPlayback, 11)
        self.assertEqual(DVDPlayback.kDVDEventVideoStandard, 12)
        self.assertEqual(DVDPlayback.kDVDEventStreams, 13)
        self.assertEqual(DVDPlayback.kDVDEventScanSpeed, 14)
        self.assertEqual(DVDPlayback.kDVDEventMenuCalled, 15)
        self.assertEqual(DVDPlayback.kDVDEventParental, 16)
        self.assertEqual(DVDPlayback.kDVDEventPGC, 17)
        self.assertEqual(DVDPlayback.kDVDEventGPRM, 18)
        self.assertEqual(DVDPlayback.kDVDEventRegionMismatch, 19)
        self.assertEqual(DVDPlayback.kDVDEventTitleTime, 20)
        self.assertEqual(DVDPlayback.kDVDEventSubpictureStreamNumbers, 21)
        self.assertEqual(DVDPlayback.kDVDEventAudioStreamNumbers, 22)
        self.assertEqual(DVDPlayback.kDVDEventAngleNumbers, 23)
        self.assertEqual(DVDPlayback.kDVDEventError, 24)
        self.assertEqual(DVDPlayback.kDVDEventCCInfo, 25)
        self.assertEqual(DVDPlayback.kDVDEventChapterTime, 26)

    def testFunctions(self):
        DVDPlayback.DVDInitialize
        DVDPlayback.DVDDispose

        self.assertArgIsIn(DVDPlayback.DVDIsValidMediaRef, 0)
        self.assertArgIsOut(DVDPlayback.DVDIsValidMediaRef, 1)

        self.assertArgIsOut(DVDPlayback.DVDIsValidMediaURL, 1)

        self.assertArgIsOut(DVDPlayback.DVDHasMedia, 0)

        self.assertArgIsIn(DVDPlayback.DVDOpenMediaFile, 0)

        DVDPlayback.DVDOpenMediaFileWithURL
        DVDPlayback.DVDCloseMediaFile

        self.assertArgIsIn(DVDPlayback.DVDOpenMediaVolume, 0)

        DVDPlayback.DVDOpenMediaVolumeWithURL
        DVDPlayback.DVDCloseMediaVolume

        self.assertFalse(hasattr(DVDPlayback, "DVDIsSupportedDevice"))
        self.assertFalse(hasattr(DVDPlayback, "DVDSwitchToDevice"))
        self.assertFalse(hasattr(DVDPlayback, "DVDSetVideoDevice"))
        self.assertFalse(hasattr(DVDPlayback, "DVDGetVideoDevice"))

        self.assertArgIsOut(DVDPlayback.DVDIsSupportedDisplay, 1)

        self.assertArgIsOut(DVDPlayback.DVDSwitchToDisplay, 1)

        DVDPlayback.DVDSetVideoDisplay

        self.assertArgIsOut(DVDPlayback.DVDGetVideoDisplay, 0)

        self.assertFalse(hasattr(DVDPlayback, "DVDSetVideoPort"))
        self.assertFalse(hasattr(DVDPlayback, "DVDGetVideoPort"))

        DVDPlayback.DVDSetVideoWindowID

        self.assertArgIsOut(DVDPlayback.DVDGetVideoWindowID, 0)

        self.assertFalse(hasattr(DVDPlayback, "DVDSetVideoBounds"))
        self.assertFalse(hasattr(DVDPlayback, "DVDGetVideoBounds"))
        self.assertFalse(hasattr(DVDPlayback, "DVDGetVideoKeyColor"))

        self.assertArgIsOut(DVDPlayback.DVDGetNativeVideoSize, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetNativeVideoSize, 1)

        self.assertArgIsOut(DVDPlayback.DVDGetAspectRatio, 0)

        DVDPlayback.DVDSetAspectRatio

        self.assertArgIsOut(DVDPlayback.DVDGetFormatStandard, 0)

        DVDPlayback.DVDSetVideoWindowRef

        self.assertArgIsOut(DVDPlayback.DVDGetVideoWindowRef, 0)

        self.assertArgIsIn(DVDPlayback.DVDSetVideoCGBounds, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetVideoCGBounds, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormat, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormat, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormat, 2)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormat, 3)

        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormatByStream, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormatByStream, 2)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormatByStream, 3)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioStreamFormatByStream, 4)

        self.assertArgIsOut(DVDPlayback.DVDGetAudioOutputModeCapabilities, 0)

        DVDPlayback.DVDSetAudioOutputMode

        self.assertArgIsOut(DVDPlayback.DVDGetAudioOutputMode, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetSPDIFDataOutDeviceCount, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetSPDIFDataOutDeviceCFName, 1)

        DVDPlayback.DVDSetSPDIFDataOutDevice

        self.assertArgIsOut(DVDPlayback.DVDGetSPDIFDataOutDevice, 0)

        DVDPlayback.DVDSetTime

        self.assertArgIsOut(DVDPlayback.DVDGetTime, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetTime, 2)

        self.assertArgIsOut(DVDPlayback.DVDGetState, 0)

        DVDPlayback.DVDIdle
        DVDPlayback.DVDUpdateVideo

        self.assertArgIsOut(DVDPlayback.DVDIsPlaying, 0)

        self.assertArgIsOut(DVDPlayback.DVDIsPaused, 0)

        DVDPlayback.DVDPlay
        DVDPlayback.DVDPause
        DVDPlayback.DVDResume
        DVDPlayback.DVDStop
        DVDPlayback.DVDScan

        self.assertArgIsOut(DVDPlayback.DVDGetScanRate, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetScanRate, 1)

        DVDPlayback.DVDStepFrame

        self.assertArgIsOut(DVDPlayback.DVDIsMuted, 0)

        DVDPlayback.DVDMute
        DVDPlayback.DVDSetAudioVolume

        self.assertArgIsOut(DVDPlayback.DVDGetAudioVolume, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetAudioVolumeInfo, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioVolumeInfo, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioVolumeInfo, 2)

        self.assertArgIsOut(DVDPlayback.DVDHasMenu, 1)

        self.assertArgIsOut(DVDPlayback.DVDIsOnMenu, 0)
        self.assertArgIsOut(DVDPlayback.DVDIsOnMenu, 1)

        DVDPlayback.DVDGoToMenu
        DVDPlayback.DVDReturnToTitle
        DVDPlayback.DVDGoBackOneLevel
        DVDPlayback.DVDDoUserNavigation

        self.assertFalse(hasattr(DVDPlayback, "DVDDoMenuClick"))
        self.assertFalse(hasattr(DVDPlayback, "DVDDoMenuMouseOver"))

        DVDPlayback.DVDDoButtonActivate

        self.assertArgIsOut(DVDPlayback.DVDGetButtoninfo, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetButtoninfo, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetButtoninfo, 2)
        self.assertArgIsOut(DVDPlayback.DVDGetButtoninfo, 3)
        self.assertArgIsOut(DVDPlayback.DVDGetButtoninfo, 4)

        self.assertArgIsOut(DVDPlayback.DVDGetButtonPosition, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetButtonPosition, 2)

        self.assertArgIsIn(DVDPlayback.DVDDoMenuCGClick, 0)
        self.assertArgIsOut(DVDPlayback.DVDDoMenuCGClick, 1)

        self.assertArgIsIn(DVDPlayback.DVDDoMenuCGMouseOver, 0)
        self.assertArgIsOut(DVDPlayback.DVDDoMenuCGMouseOver, 1)

        DVDPlayback.DVDGetMediaUniqueID

        self.assertFalse(hasattr(DVDPlayback, "DVDGetMediaVolumeName"))

        self.assertArgIsOut(DVDPlayback.DVDGetMediaVolumeCFName, 0)

        DVDPlayback.DVDSetTitle

        self.assertArgIsOut(DVDPlayback.DVDGetTitle, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetNumTitles, 0)

        self.assertArgIsOut(DVDPlayback.DVDHasPreviousChapter, 0)

        self.assertArgIsOut(DVDPlayback.DVDHasNextChapter, 0)

        DVDPlayback.DVDSetChapter

        self.assertArgIsOut(DVDPlayback.DVDGetChapter, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetNumChapters, 1)

        DVDPlayback.DVDPreviousChapter
        DVDPlayback.DVDNextChapter
        DVDPlayback.DVDSetAngle

        self.assertArgIsOut(DVDPlayback.DVDGetAngle, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetNumAngles, 0)

        DVDPlayback.DVDDisplaySubPicture

        self.assertArgIsOut(DVDPlayback.DVDIsDisplayingSubPicture, 0)

        DVDPlayback.DVDSetSubPictureStream

        self.assertArgIsOut(DVDPlayback.DVDGetSubPictureStream, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetNumSubPictureStreams, 0)

        DVDPlayback.DVDSetAudioStream

        self.assertArgIsOut(DVDPlayback.DVDGetAudioStream, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetNumAudioStreams, 0)

        DVDPlayback.DVDSetDefaultSubPictureLanguageCode

        self.assertArgIsOut(DVDPlayback.DVDGetSubPictureLanguageCode, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetSubPictureLanguageCode, 1)

        self.assertArgIsOut(DVDPlayback.DVDGetSubPictureLanguageCodeByStream, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetSubPictureLanguageCodeByStream, 2)

        DVDPlayback.DVDSetDefaultAudioLanguageCode

        self.assertArgIsOut(DVDPlayback.DVDGetAudioLanguageCode, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioLanguageCode, 1)

        self.assertArgIsOut(DVDPlayback.DVDGetAudioLanguageCodeByStream, 1)
        self.assertArgIsOut(DVDPlayback.DVDGetAudioLanguageCodeByStream, 2)

        DVDPlayback.DVDSetDefaultMenuLanguageCode

        self.assertArgIsOut(DVDPlayback.DVDGetMenuLanguageCode, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetBookmark, 0)
        self.assertArgSizeInArg(DVDPlayback.DVDGetBookmark, 0, 1)
        self.assertArgIsInOut(DVDPlayback.DVDGetBookmark, 1)

        self.assertArgIsIn(DVDPlayback.DVDGotoBookmark, 0)
        self.assertArgSizeInArg(DVDPlayback.DVDGotoBookmark, 0, 1)

        self.assertArgIsOut(DVDPlayback.DVDGetLastPlayBookmark, 0)
        self.assertArgSizeInArg(DVDPlayback.DVDGetLastPlayBookmark, 0, 1)
        self.assertArgIsInOut(DVDPlayback.DVDGetLastPlayBookmark, 1)

        self.assertArgIsIn(DVDPlayback.DVDSetLastPlayBookmark, 0)

        DVDPlayback.DVDClearLastPlayBookmark

        self.assertArgIsOut(DVDPlayback.DVDGetDiscRegionCode, 0)

        self.assertArgIsOut(DVDPlayback.DVDGetDriveRegionCode, 0)
        self.assertArgIsOut(DVDPlayback.DVDGetDriveRegionCode, 1)

        DVDPlayback.DVDSetDriveRegionCode
        DVDPlayback.DVDEnableWebAccess

        self.assertArgIsOut(DVDPlayback.DVDGetGPRMValue, 1)

        self.assertArgIsFunction(
            DVDPlayback.DVDSetFatalErrorCallBack,
            0,
            DVDFatalErrCallBackFunctionPtr,
            True,
        )

        self.assertArgIsFunction(
            DVDPlayback.DVDRegisterEventCallBack, 0, DVDEventCallBackFunctionPtr, True
        )
        self.assertArgIsIn(DVDPlayback.DVDRegisterEventCallBack, 1)

        DVDPlayback.DVDUnregisterEventCallBack
        DVDPlayback.DVDIsRegisteredEventCallBack

        DVDPlayback.DVDSetTimeEventRate

        self.assertArgIsOut(DVDPlayback.DVDGetTimeEventRate, 0)

        DVDPlayback.DVDSleep
        DVDPlayback.DVDWakeUp
