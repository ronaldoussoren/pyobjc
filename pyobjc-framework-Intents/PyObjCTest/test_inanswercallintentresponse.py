from PyObjCTools.TestSupport import TestCase
import Intents


class TestINAnswerCallIntentResponse(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INAnswerCallIntentResponseCode)

    def testConstants(self):
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeContinueInApp, 2)
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeInProgress, 3)
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeSuccess, 4)
        self.assertEqual(Intents.INAnswerCallIntentResponseCodeFailure, 5)
        self.assertEqual(
            Intents.INAnswerCallIntentResponseCodeFailureRequiringAppLaunch, 6
        )
