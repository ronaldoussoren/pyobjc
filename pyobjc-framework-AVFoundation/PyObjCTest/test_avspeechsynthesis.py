import AVFoundation
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
    expectedFailure,
)

AVSpeechSynthesizerBufferCallback = b"v@"
AVSpeechSynthesizerMarkerCallback = b"v@"


class TestAVSpeechSynthesisHelper(AVFoundation.NSObject):
    def speechSynthesizer_willSpeakRangeOfSpeechString_utterance_(
        self, a, b, c
    ):  # noqa: B950
        pass


class TestAVSpeechSynthesis(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVSpeechBoundary)
        self.assertIsEnumType(AVFoundation.AVSpeechSynthesisVoiceGender)
        self.assertIsEnumType(AVFoundation.AVSpeechSynthesisVoiceQuality)
        self.assertIsEnumType(AVFoundation.AVSpeechSynthesisMarkerMark)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVSpeechBoundaryImmediate, 0)
        self.assertEqual(AVFoundation.AVSpeechBoundaryWord, 1)

        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityDefault, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityEnhanced, 2)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceQualityPremium, 3)

        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceGenderUnspecified, 0)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceGenderMale, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceGenderFemale, 2)

        self.assertEqual(AVFoundation.AVSpeechSynthesisMarkerMarkPhoneme, 0)
        self.assertEqual(AVFoundation.AVSpeechSynthesisMarkerMarkWord, 1)
        self.assertEqual(AVFoundation.AVSpeechSynthesisMarkerMarkSentence, 2)
        self.assertEqual(AVFoundation.AVSpeechSynthesisMarkerMarkParagraph, 3)
        self.assertEqual(AVFoundation.AVSpeechSynthesisMarkerMarkBookmark, 4)

        self.assertIsEnumType(
            AVFoundation.AVSpeechSynthesisPersonalVoiceAuthorizationStatus
        )
        self.assertEqual(
            AVFoundation.AVSpeechSynthesisPersonalVoiceAuthorizationStatusNotDetermined,
            0,
        )
        self.assertEqual(
            AVFoundation.AVSpeechSynthesisPersonalVoiceAuthorizationStatusDenied, 1
        )
        self.assertEqual(
            AVFoundation.AVSpeechSynthesisPersonalVoiceAuthorizationStatusUnsupported, 2
        )
        self.assertEqual(
            AVFoundation.AVSpeechSynthesisPersonalVoiceAuthorizationStatusAuthorized, 3
        )

        self.assertIsEnumType(AVFoundation.AVSpeechSynthesisVoiceTraits)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceTraitNone, 0)
        self.assertEqual(AVFoundation.AVSpeechSynthesisVoiceTraitIsNoveltyVoice, 1 << 0)
        self.assertEqual(
            AVFoundation.AVSpeechSynthesisVoiceTraitIsPersonalVoice, 1 << 1
        )

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

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(
            AVFoundation.AVSpeechSynthesisAvailableVoicesDidChangeNotification, str
        )

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
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSpeechSynthesizer.prefersAssistiveTechnologySettings
        )
        self.assertArgIsBOOL(
            AVFoundation.AVSpeechSynthesizer.setPrefersAssistiveTechnologySettings_, 0
        )

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVSpeechSynthesizer.writeUtterance_toBufferCallback_toMarkerCallback_,
            1,
            AVSpeechSynthesizerBufferCallback,
        )
        self.assertArgIsBlock(
            AVFoundation.AVSpeechSynthesizer.writeUtterance_toBufferCallback_toMarkerCallback_,
            2,
            AVSpeechSynthesizerMarkerCallback,
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVSpeechSynthesizer.requestPersonalVoiceAuthorizationWithCompletionHandler_,
            0,
            b"vq",
        )

    @min_sdk_level("10.14")
    def testProtocols(self):
        self.assertProtocolExists("AVSpeechSynthesizerDelegate")
