from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVSpeechSynthesisHelper (AVFoundation.NSObject):
    def speechSynthesizer_willSpeakRangeOfSpeechString_utterance_(self, a, b, c): pass

class TestAVSpeechSynthesis (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVSpeechBoundaryImmediate, 0)
        self.assertEqual(AVFoundation.AVSpeechBoundaryWord, 1)

        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityDefault, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityEnhanced, 2)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(AVFoundation.AVSpeechUtteranceMinimumSpeechRate, float)
        self.assertIsInstance(AVFoundation.AVSpeechUtteranceMaximumSpeechRate, float)
        self.assertIsInstance(AVFoundation.AVSpeechUtteranceDefaultSpeechRate, float)

        self.assertIsInstance(AVFoundation.AVSpeechSynthesisVoiceIdentifierAlex, unicode)
        self.assertIsInstance(AVFoundation.AVSpeechSynthesisIPANotationAttribute, unicode)

    def testMethods(self):
        self.assertArgHasType(TestAVSpeechSynthesisHelper.speechSynthesizer_willSpeakRangeOfSpeechString_utterance_, 1, AVFoundation.NSRange.__typestr__)

    @min_os_level('10.14')
    def testMethods10_14(self):
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.isSpeaking)
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.isPaused)
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.stopSpeakingAtBoundary_)
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.pauseSpeakingAtBoundary_)
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.continueSpeaking)

    @expectedFailure
    @min_sdk_level('10.14')
    def testProtocols(self):
        objc.protocolNamed('AVSpeechSynthesizerDelegate')

if __name__ == "__main__":
    main()
