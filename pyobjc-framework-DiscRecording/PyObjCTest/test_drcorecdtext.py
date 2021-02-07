import CoreFoundation
import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRCoreCDText(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRCDTextBlockRef)

    def testConstants(self):
        self.assertEqual(
            DiscRecording.kDRCDTextEncodingISOLatin1Modified,
            CoreFoundation.kCFStringEncodingISOLatin1,
        )
        self.assertEqual(
            DiscRecording.kDRCDTextEncodingASCII, CoreFoundation.kCFStringEncodingASCII
        )

        self.assertEqual(DiscRecording.kDRCDTextGenreCodeUnknown, 0x0001)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeAdultContemporary, 0x0002)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeAlternativeRock, 0x0003)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeChildrens, 0x0004)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeClassical, 0x0005)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeContemporaryChristian, 0x0006)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeCountry, 0x0007)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeDance, 0x0008)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeEasyListening, 0x0009)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeErotic, 0x000A)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeFolk, 0x000B)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeGospel, 0x000C)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeHipHop, 0x000D)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeJazz, 0x000E)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeLatin, 0x000F)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeMusical, 0x0010)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeNewAge, 0x0011)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeOpera, 0x0012)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeOperetta, 0x0013)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodePop, 0x0014)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeRap, 0x0015)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeReggae, 0x0016)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeRock, 0x0017)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeRhythmAndBlues, 0x0018)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeSoundEffects, 0x0019)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeSoundtrack, 0x001A)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeSpokenWord, 0x001B)
        self.assertEqual(DiscRecording.kDRCDTextGenreCodeWorldMusic, 0x001C)

        self.assertIsInstance(DiscRecording.kDRCDTextLanguageKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextCharacterCodeKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextCFStringEncodingKey, str)
        self.assertIsInstance(
            DiscRecording.kDRCDTextCopyrightAssertedForSpecialMessagesKey, str
        )
        self.assertIsInstance(DiscRecording.kDRCDTextCopyrightAssertedForNamesKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextCopyrightAssertedForTitlesKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextTitleKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextPerformerKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextSongwriterKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextComposerKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextArrangerKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextSpecialMessageKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextDiscIdentKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextGenreKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextGenreCodeKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextClosedKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextMCNISRCKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextTOCKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextTOC2Key, str)
        self.assertIsInstance(DiscRecording.kDRCDTextSizeKey, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(
            DiscRecording.DRCDTextBlockCreateArrayFromPackList
        )

        self.assertIsInstance(DiscRecording.DRCDTextBlockGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRCDTextBlockCreate)

        DiscRecording.DRCDTextBlockGetProperties
        DiscRecording.DRCDTextBlockGetTrackDictionaries
        DiscRecording.DRCDTextBlockSetTrackDictionaries
        DiscRecording.DRCDTextBlockGetValue
        DiscRecording.DRCDTextBlockSetValue
        DiscRecording.DRCDTextBlockFlatten
