
from PyObjCTools.TestSupport import *
from AppKit import *

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



if __name__ == "__main__":
    main()
