
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpeechSynthesizerHelper (NSObject):
    def speechSynthesizer_didFinishSpeaking_(self, ss, b): pass
    def speechSynthesizer_willSpeakWord_ofString_(self, ss, w, s): pass
    def speechSynthesizer_willSpeakPhoneme_(self, ss, i): pass
    def speechSynthesizer_didEncounterErrorAtIndex_ofString_message_(self, ss, i, s, m): pass

class TestNSSpeechSynthesizer (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSVoiceName, unicode)
        self.assertIsInstance(NSVoiceIdentifier, unicode)
        self.assertIsInstance(NSVoiceAge, unicode)
        self.assertIsInstance(NSVoiceGender, unicode)
        self.assertIsInstance(NSVoiceDemoText, unicode)

        self.assertIsInstance(NSVoiceGenderNeuter, unicode)
        self.assertIsInstance(NSVoiceGenderMale, unicode)
        self.assertIsInstance(NSVoiceGenderFemale, unicode)
        self.assertIsInstance(NSVoiceLanguage, unicode)


    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(NSSpeechImmediateBoundary,  0)
        self.assertEqual(NSSpeechWordBoundary, 1)
        self.assertEqual(NSSpeechSentenceBoundary, 2)

        self.assertIsInstance(NSVoiceLocaleIdentifier, unicode)
        self.assertIsInstance(NSVoiceSupportedCharacters, unicode)
        self.assertIsInstance(NSVoiceIndividuallySpokenCharacters, unicode)


        self.assertIsInstance( NSSpeechStatusProperty, unicode)
        self.assertIsInstance( NSSpeechErrorsProperty, unicode)
        self.assertIsInstance( NSSpeechInputModeProperty, unicode)
        self.assertIsInstance( NSSpeechCharacterModeProperty, unicode)
        self.assertIsInstance( NSSpeechNumberModeProperty, unicode)
        self.assertIsInstance( NSSpeechRateProperty, unicode)
        self.assertIsInstance( NSSpeechPitchBaseProperty, unicode)
        self.assertIsInstance( NSSpeechPitchModProperty, unicode)
        self.assertIsInstance( NSSpeechVolumeProperty, unicode)
        self.assertIsInstance( NSSpeechSynthesizerInfoProperty, unicode)
        self.assertIsInstance( NSSpeechRecentSyncProperty, unicode)
        self.assertIsInstance( NSSpeechPhonemeSymbolsProperty, unicode)
        self.assertIsInstance( NSSpeechCurrentVoiceProperty, unicode)
        self.assertIsInstance( NSSpeechCommandDelimiterProperty, unicode)
        self.assertIsInstance( NSSpeechResetProperty, unicode)
        self.assertIsInstance( NSSpeechOutputToFileURLProperty, unicode)

        self.assertIsInstance( NSSpeechModeText, unicode)
        self.assertIsInstance( NSSpeechModePhoneme, unicode)

        self.assertIsInstance( NSSpeechModeNormal, unicode)
        self.assertIsInstance( NSSpeechModeLiteral, unicode)

        self.assertIsInstance( NSSpeechStatusOutputBusy, unicode)
        self.assertIsInstance( NSSpeechStatusOutputPaused, unicode)
        self.assertIsInstance( NSSpeechStatusNumberOfCharactersLeft, unicode)
        self.assertIsInstance( NSSpeechStatusPhonemeCode, unicode)

        self.assertIsInstance( NSSpeechErrorCount, unicode)
        self.assertIsInstance( NSSpeechErrorOldestCode, unicode)
        self.assertIsInstance( NSSpeechErrorOldestCharacterOffset, unicode)
        self.assertIsInstance( NSSpeechErrorNewestCode, unicode)
        self.assertIsInstance( NSSpeechErrorNewestCharacterOffset, unicode)

        self.assertIsInstance( NSSpeechSynthesizerInfoIdentifier, unicode)
        self.assertIsInstance( NSSpeechSynthesizerInfoVersion, unicode)

        self.assertIsInstance( NSSpeechPhonemeInfoOpcode, unicode)
        self.assertIsInstance( NSSpeechPhonemeInfoSymbol, unicode)
        self.assertIsInstance( NSSpeechPhonemeInfoExample, unicode)
        self.assertIsInstance( NSSpeechPhonemeInfoHiliteStart, unicode)
        self.assertIsInstance( NSSpeechPhonemeInfoHiliteEnd, unicode)

        self.assertIsInstance( NSSpeechCommandPrefix, unicode)
        self.assertIsInstance( NSSpeechCommandSuffix, unicode)

        self.assertIsInstance( NSSpeechDictionaryLocaleIdentifier, unicode)
        self.assertIsInstance( NSSpeechDictionaryModificationDate, unicode)
        self.assertIsInstance( NSSpeechDictionaryPronunciations, unicode)
        self.assertIsInstance( NSSpeechDictionaryAbbreviations, unicode)
        self.assertIsInstance( NSSpeechDictionaryEntrySpelling, unicode)
        self.assertIsInstance( NSSpeechDictionaryEntryPhonemes, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSSpeechSynthesizer.startSpeakingString_)
        self.assertResultIsBOOL(NSSpeechSynthesizer.startSpeakingString_toURL_)
        self.assertResultIsBOOL(NSSpeechSynthesizer.isSpeaking)
        self.assertResultIsBOOL(NSSpeechSynthesizer.setVoice_)
        self.assertResultIsBOOL(NSSpeechSynthesizer.usesFeedbackWindow)
        self.assertArgIsBOOL(NSSpeechSynthesizer.setUsesFeedbackWindow_, 0)
        self.assertResultIsBOOL(NSSpeechSynthesizer.setObject_forProperty_error_)
        self.assertArgIsOut(NSSpeechSynthesizer.setObject_forProperty_error_, 2)
        self.assertArgIsOut(NSSpeechSynthesizer.objectForProperty_error_, 1)
        self.assertResultIsBOOL(NSSpeechSynthesizer.isAnyApplicationSpeaking)

    def testProtocol(self):
        self.assertArgIsBOOL(TestNSSpeechSynthesizerHelper.speechSynthesizer_didFinishSpeaking_, 1)
        self.assertArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakWord_ofString_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakPhoneme_, 1, objc._C_SHT)

    @min_os_level('10.5')
    def testProtocol10_5(self):
        self.assertArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_didEncounterErrorAtIndex_ofString_message_, 1, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
