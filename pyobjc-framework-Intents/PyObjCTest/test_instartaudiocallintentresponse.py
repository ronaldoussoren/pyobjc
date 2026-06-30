from PyObjCTools.TestSupport import TestCase
import Intents


class TestINStartAudioCallIntentResponse(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INStartAudioCallIntentResponseCode)
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
