
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpeechSynthesizerHelper (NSObject):
    def speechSynthesizer_didFinishSpeaking_(self, ss, b): pass
    def speechSynthesizer_willSpeakWord_ofString_(self, ss, w, s): pass
    def speechSynthesizer_willSpeakPhoneme_(self, ss, i): pass
    def speechSynthesizer_didEncounterErrorAtIndex_ofString_message_(self, ss, i, s, m): pass

class TestNSSpeechSynthesizer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSVoiceName, unicode)
        self.failUnlessIsInstance(NSVoiceIdentifier, unicode)
        self.failUnlessIsInstance(NSVoiceAge, unicode)
        self.failUnlessIsInstance(NSVoiceGender, unicode)
        self.failUnlessIsInstance(NSVoiceDemoText, unicode)

        self.failUnlessIsInstance(NSVoiceGenderNeuter, unicode)
        self.failUnlessIsInstance(NSVoiceGenderMale, unicode)
        self.failUnlessIsInstance(NSVoiceGenderFemale, unicode)
        self.failUnlessIsInstance(NSVoiceLanguage, unicode)


    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(NSSpeechImmediateBoundary,  0)
        self.failUnlessEqual(NSSpeechWordBoundary, 1)
        self.failUnlessEqual(NSSpeechSentenceBoundary, 2)

        self.failUnlessIsInstance(NSVoiceLocaleIdentifier, unicode)
        self.failUnlessIsInstance(NSVoiceSupportedCharacters, unicode)
        self.failUnlessIsInstance(NSVoiceIndividuallySpokenCharacters, unicode)


        self.failUnlessIsInstance( NSSpeechStatusProperty, unicode)
        self.failUnlessIsInstance( NSSpeechErrorsProperty, unicode)
        self.failUnlessIsInstance( NSSpeechInputModeProperty, unicode)
        self.failUnlessIsInstance( NSSpeechCharacterModeProperty, unicode)
        self.failUnlessIsInstance( NSSpeechNumberModeProperty, unicode)
        self.failUnlessIsInstance( NSSpeechRateProperty, unicode)
        self.failUnlessIsInstance( NSSpeechPitchBaseProperty, unicode)
        self.failUnlessIsInstance( NSSpeechPitchModProperty, unicode)
        self.failUnlessIsInstance( NSSpeechVolumeProperty, unicode)
        self.failUnlessIsInstance( NSSpeechSynthesizerInfoProperty, unicode)
        self.failUnlessIsInstance( NSSpeechRecentSyncProperty, unicode)
        self.failUnlessIsInstance( NSSpeechPhonemeSymbolsProperty, unicode)
        self.failUnlessIsInstance( NSSpeechCurrentVoiceProperty, unicode)
        self.failUnlessIsInstance( NSSpeechCommandDelimiterProperty, unicode)
        self.failUnlessIsInstance( NSSpeechResetProperty, unicode)
        self.failUnlessIsInstance( NSSpeechOutputToFileURLProperty, unicode)

        self.failUnlessIsInstance( NSSpeechModeText, unicode)
        self.failUnlessIsInstance( NSSpeechModePhoneme, unicode)

        self.failUnlessIsInstance( NSSpeechModeNormal, unicode)
        self.failUnlessIsInstance( NSSpeechModeLiteral, unicode)

        self.failUnlessIsInstance( NSSpeechStatusOutputBusy, unicode)
        self.failUnlessIsInstance( NSSpeechStatusOutputPaused, unicode)
        self.failUnlessIsInstance( NSSpeechStatusNumberOfCharactersLeft, unicode)
        self.failUnlessIsInstance( NSSpeechStatusPhonemeCode, unicode)

        self.failUnlessIsInstance( NSSpeechErrorCount, unicode)
        self.failUnlessIsInstance( NSSpeechErrorOldestCode, unicode)
        self.failUnlessIsInstance( NSSpeechErrorOldestCharacterOffset, unicode)
        self.failUnlessIsInstance( NSSpeechErrorNewestCode, unicode)
        self.failUnlessIsInstance( NSSpeechErrorNewestCharacterOffset, unicode)

        self.failUnlessIsInstance( NSSpeechSynthesizerInfoIdentifier, unicode)
        self.failUnlessIsInstance( NSSpeechSynthesizerInfoVersion, unicode)

        self.failUnlessIsInstance( NSSpeechPhonemeInfoOpcode, unicode)
        self.failUnlessIsInstance( NSSpeechPhonemeInfoSymbol, unicode)
        self.failUnlessIsInstance( NSSpeechPhonemeInfoExample, unicode)
        self.failUnlessIsInstance( NSSpeechPhonemeInfoHiliteStart, unicode)
        self.failUnlessIsInstance( NSSpeechPhonemeInfoHiliteEnd, unicode)

        self.failUnlessIsInstance( NSSpeechCommandPrefix, unicode)
        self.failUnlessIsInstance( NSSpeechCommandSuffix, unicode)

        self.failUnlessIsInstance( NSSpeechDictionaryLocaleIdentifier, unicode)
        self.failUnlessIsInstance( NSSpeechDictionaryModificationDate, unicode)
        self.failUnlessIsInstance( NSSpeechDictionaryPronunciations, unicode)
        self.failUnlessIsInstance( NSSpeechDictionaryAbbreviations, unicode)
        self.failUnlessIsInstance( NSSpeechDictionaryEntrySpelling, unicode)
        self.failUnlessIsInstance( NSSpeechDictionaryEntryPhonemes, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.startSpeakingString_)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.startSpeakingString_toURL_)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.isSpeaking)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.setVoice_)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.usesFeedbackWindow)
        self.failUnlessArgIsBOOL(NSSpeechSynthesizer.setUsesFeedbackWindow_, 0)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.setObject_forProperty_error_)
        self.failUnlessArgIsOut(NSSpeechSynthesizer.setObject_forProperty_error_, 2)
        self.failUnlessArgIsOut(NSSpeechSynthesizer.objectForProperty_error_, 1)
        self.failUnlessResultIsBOOL(NSSpeechSynthesizer.isAnyApplicationSpeaking)

    def testProtocol(self):
        self.failUnlessArgIsBOOL(TestNSSpeechSynthesizerHelper.speechSynthesizer_didFinishSpeaking_, 1)
        self.failUnlessArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakWord_ofString_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_willSpeakPhoneme_, 1, objc._C_SHT)

    @min_os_level('10.5')
    def testProtocol10_5(self):
        self.failUnlessArgHasType(TestNSSpeechSynthesizerHelper.speechSynthesizer_didEncounterErrorAtIndex_ofString_message_, 1, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
