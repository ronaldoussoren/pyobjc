import DiscRecording
import Foundation
from PyObjCTools.TestSupport import TestCase


class TestDRCDText(TestCase):
    def testConstants(self):
        self.assertEqual(
            DiscRecording.DRCDTextEncodingISOLatin1Modified,
            Foundation.NSISOLatin1StringEncoding,
        )
        self.assertEqual(
            DiscRecording.DRCDTextEncodingASCII, Foundation.NSASCIIStringEncoding
        )

        self.assertEqual(DiscRecording.DRCDTextGenreCodeUnknown, 0x0001)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeAdultContemporary, 0x0002)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeAlternativeRock, 0x0003)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeChildrens, 0x0004)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeClassical, 0x0005)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeContemporaryChristian, 0x0006)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeCountry, 0x0007)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeDance, 0x0008)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeEasyListening, 0x0009)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeErotic, 0x000A)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeFolk, 0x000B)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeGospel, 0x000C)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeHipHop, 0x000D)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeJazz, 0x000E)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeLatin, 0x000F)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeMusical, 0x0010)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeNewAge, 0x0011)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeOpera, 0x0012)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeOperetta, 0x0013)
        self.assertEqual(DiscRecording.DRCDTextGenreCodePop, 0x0014)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeRap, 0x0015)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeReggae, 0x0016)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeRock, 0x0017)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeRhythmAndBlues, 0x0018)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeSoundEffects, 0x0019)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeSoundtrack, 0x001A)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeSpokenWord, 0x001B)
        self.assertEqual(DiscRecording.DRCDTextGenreCodeWorldMusic, 0x001C)

        self.assertIsInstance(DiscRecording.DRCDTextLanguageKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextCharacterCodeKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextNSStringEncodingKey, str)
        self.assertIsInstance(
            DiscRecording.DRCDTextCopyrightAssertedForSpecialMessagesKey, str
        )
        self.assertIsInstance(DiscRecording.DRCDTextCopyrightAssertedForNamesKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextCopyrightAssertedForTitlesKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextTitleKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextPerformerKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextSongwriterKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextComposerKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextArrangerKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextSpecialMessageKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextDiscIdentKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextGenreKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextGenreCodeKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextClosedKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextMCNISRCKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextTOCKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextTOC2Key, str)
        self.assertIsInstance(DiscRecording.DRCDTextSizeKey, str)
