import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSpeechSynthesizerHelper(AppKit.NSObject):
    def speechSynthesizer_didFinishSpeaking_(self, ss, b):
        pass

    def speechSynthesizer_willSpeakWord_ofString_(self, ss, w, s):
        pass

    def speechSynthesizer_willSpeakPhoneme_(self, ss, i):
        pass

    def speechSynthesizer_didEncounterErrorAtIndex_ofString_message_(self, ss, i, s, m):
        pass


class TestNSSpeechSynthesizer(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSVoiceName, str)
        self.assertIsInstance(AppKit.NSVoiceIdentifier, str)
        self.assertIsInstance(AppKit.NSVoiceAge, str)
        self.assertIsInstance(AppKit.NSVoiceGender, str)
        self.assertIsInstance(AppKit.NSVoiceDemoText, str)

        self.assertIsInstance(AppKit.NSVoiceGenderNeuter, str)
        self.assertIsInstance(AppKit.NSVoiceGenderMale, str)
        self.assertIsInstance(AppKit.NSVoiceGenderFemale, str)
        self.assertIsInstance(AppKit.NSVoiceLanguage, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSSpeechImmediateBoundary, 0)
        self.assertEqual(AppKit.NSSpeechWordBoundary, 1)
        self.assertEqual(AppKit.NSSpeechSentenceBoundary, 2)

        self.assertIsInstance(AppKit.NSVoiceLocaleIdentifier, str)
        self.assertIsInstance(AppKit.NSVoiceSupportedCharacters, str)
        self.assertIsInstance(AppKit.NSVoiceIndividuallySpokenCharacters, str)

        self.assertIsInstance(AppKit.NSSpeechStatusProperty, str)
        self.assertIsInstance(AppKit.NSSpeechErrorsProperty, str)
        self.assertIsInstance(AppKit.NSSpeechInputModeProperty, str)
        self.assertIsInstance(AppKit.NSSpeechCharacterModeProperty, str)
        self.assertIsInstance(AppKit.NSSpeechNumberModeProperty, str)
        self.assertIsInstance(AppKit.NSSpeechRateProperty, str)
        self.assertIsInstance(AppKit.NSSpeechPitchBaseProperty, str)
        self.assertIsInstance(AppKit.NSSpeechPitchModProperty, str)
        self.assertIsInstance(AppKit.NSSpeechVolumeProperty, str)
        self.assertIsInstance(AppKit.NSSpeechSynthesizerInfoProperty, str)
        self.assertIsInstance(AppKit.NSSpeechRecentSyncProperty, str)
        self.assertIsInstance(AppKit.NSSpeechPhonemeSymbolsProperty, str)
        self.assertIsInstance(AppKit.NSSpeechCurrentVoiceProperty, str)
        self.assertIsInstance(AppKit.NSSpeechCommandDelimiterProperty, str)
        self.assertIsInstance(AppKit.NSSpeechResetProperty, str)
        self.assertIsInstance(AppKit.NSSpeechOutputToFileURLProperty, str)

        self.assertIsInstance(AppKit.NSSpeechModeText, str)
        self.assertIsInstance(AppKit.NSSpeechModePhoneme, str)

        self.assertIsInstance(AppKit.NSSpeechModeNormal, str)
        self.assertIsInstance(AppKit.NSSpeechModeLiteral, str)

        self.assertIsInstance(AppKit.NSSpeechStatusOutputBusy, str)
        self.assertIsInstance(AppKit.NSSpeechStatusOutputPaused, str)
        self.assertIsInstance(AppKit.NSSpeechStatusNumberOfCharactersLeft, str)
        self.assertIsInstance(AppKit.NSSpeechStatusPhonemeCode, str)

        self.assertIsInstance(AppKit.NSSpeechErrorCount, str)
        self.assertIsInstance(AppKit.NSSpeechErrorOldestCode, str)
        self.assertIsInstance(AppKit.NSSpeechErrorOldestCharacterOffset, str)
        self.assertIsInstance(AppKit.NSSpeechErrorNewestCode, str)
        self.assertIsInstance(AppKit.NSSpeechErrorNewestCharacterOffset, str)

        self.assertIsInstance(AppKit.NSSpeechSynthesizerInfoIdentifier, str)
        self.assertIsInstance(AppKit.NSSpeechSynthesizerInfoVersion, str)

        self.assertIsInstance(AppKit.NSSpeechPhonemeInfoOpcode, str)
        self.assertIsInstance(AppKit.NSSpeechPhonemeInfoSymbol, str)
        self.assertIsInstance(AppKit.NSSpeechPhonemeInfoExample, str)
        self.assertIsInstance(AppKit.NSSpeechPhonemeInfoHiliteStart, str)
        self.assertIsInstance(AppKit.NSSpeechPhonemeInfoHiliteEnd, str)

        self.assertIsInstance(AppKit.NSSpeechCommandPrefix, str)
        self.assertIsInstance(AppKit.NSSpeechCommandSuffix, str)

        self.assertIsInstance(AppKit.NSSpeechDictionaryLocaleIdentifier, str)
        self.assertIsInstance(AppKit.NSSpeechDictionaryModificationDate, str)
        self.assertIsInstance(AppKit.NSSpeechDictionaryPronunciations, str)
        self.assertIsInstance(AppKit.NSSpeechDictionaryAbbreviations, str)
        self.assertIsInstance(AppKit.NSSpeechDictionaryEntrySpelling, str)
        self.assertIsInstance(AppKit.NSSpeechDictionaryEntryPhonemes, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.startSpeakingString_)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.startSpeakingString_toURL_)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.isSpeaking)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.setVoice_)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.usesFeedbackWindow)
        self.assertArgIsBOOL(AppKit.NSSpeechSynthesizer.setUsesFeedbackWindow_, 0)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.setObject_forProperty_error_)
        self.assertArgIsOut(AppKit.NSSpeechSynthesizer.setObject_forProperty_error_, 2)
        self.assertArgIsOut(AppKit.NSSpeechSynthesizer.objectForProperty_error_, 1)
        self.assertResultIsBOOL(AppKit.NSSpeechSynthesizer.isAnyApplicationSpeaking)

    def testProtocol(self):
        self.assertArgIsBOOL(
            TestNSSpeechSynthesizerHelper.speechSynthesizer_didFinishSpeaking_, 1
        )
        self.assertArgHasType(
            TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakWord_ofString_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakPhoneme_,
            1,
            objc._C_SHT,
        )

    @min_os_level("10.5")
    def testProtocol10_5(self):
        self.assertArgHasType(
            TestNSSpeechSynthesizerHelper.speechSynthesizer_didEncounterErrorAtIndex_ofString_message_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )

    @min_sdk_level("10.9")
    def testProtocol10_9(self):
        objc.protocolNamed("NSSpeechSynthesizerDelegate")
