import AVFoundation
import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
    expectedFailure,
)

AVSpeechSynthesizerBufferCallback = b"v@"


class TestAVSpeechSynthesisHelper(AVFoundation.NSObject):
    def speechSynthesizer_willSpeakRangeOfSpeechString_utterance_(
        self, a, b, c
    ):  # noqa: B950
        pass


class TestAVSpeechSynthesis(TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVSpeechBoundaryImmediate, 0)
        self.assertEqual(AVFoundation.AVSpeechBoundaryWord, 1)

        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityDefault, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityEnhanced, 2)

        self.assertEqual(
            AVFoundation.AVSpeechSynthesisVoiceGenderUnspecified, 0
        )  # noqa: B950
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceGenderMale, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceGenderFemale, 2)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(
            AVFoundation.AVSpeechUtteranceMinimumSpeechRate, float
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVSpeechUtteranceMaximumSpeechRate, float
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVSpeechUtteranceDefaultSpeechRate, float
        )  # noqa: B950

        self.assertIsInstance(
            AVFoundation.AVSpeechSynthesisVoiceIdentifierAlex, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVSpeechSynthesisIPANotationAttribute, str
        )  # noqa: B950

    def testMethods(self):
        self.assertArgHasType(
            TestAVSpeechSynthesisHelper.speechSynthesizer_willSpeakRangeOfSpeechString_utterance_,  # noqa: B950
            1,
            AVFoundation.NSRange.__typestr__,
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.isSpeaking)
        self.assertResultIsBOOL(AVFoundation.AVSpeechSynthesizer.isPaused)
        self.assertResultIsBOOL(
            AVFoundation.AVSpeechSynthesizer.stopSpeakingAtBoundary_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVSpeechSynthesizer.pauseSpeakingAtBoundary_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVSpeechSynthesizer.continueSpeaking
        )  # noqa: B950

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AVFoundation.AVSpeechSynthesizer.writeUtterance_toBufferCallback_,
            1,
            AVSpeechSynthesizerBufferCallback,
        )

    @expectedFailure
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSpeechSynthesizer.prefersAssistiveTechnologySettings
        )
        self.assertArgIsBOOL(
            AVFoundation.AVSpeechSynthesizer.setPrefersAssistiveTechnologySettings_, 0
        )

    @expectedFailure
    @min_sdk_level("10.14")
    def testProtocols(self):
        objc.protocolNamed("AVSpeechSynthesizerDelegate")
