from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINStartAudioCallIntentResponse(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INStartAudioCallIntentResponseCode)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INStartAudioCallIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INStartAudioCallIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INStartAudioCallIntentResponseCodeContinueInApp, 2)
        self.assertEqual(Intents.INStartAudioCallIntentResponseCodeFailure, 3)
        self.assertEqual(
            Intents.INStartAudioCallIntentResponseCodeFailureRequiringAppLaunch, 4
        )
        self.assertEqual(
            Intents.INStartAudioCallIntentResponseCodeFailureAppConfigurationRequired, 5
        )
        self.assertEqual(
            Intents.INStartAudioCallIntentResponseCodeFailureCallingServiceNotAvailable,
            6,
        )
        self.assertEqual(
            Intents.INStartAudioCallIntentResponseCodeFailureContactNotSupportedByApp, 7
        )
        self.assertEqual(
            Intents.INStartAudioCallIntentResponseCodeFailureNoValidNumber, 8
        )
