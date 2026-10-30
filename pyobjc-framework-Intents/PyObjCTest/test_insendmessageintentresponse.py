from PyObjCTools.TestSupport import TestCase
import Intents


class TestINSendMessageIntentResponse(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INSendMessageIntentResponseCode)
        self.assertEqual(Intents.INSendMessageIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INSendMessageIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INSendMessageIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INSendMessageIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INSendMessageIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INSendMessageIntentResponseCodeFailureRequiringAppLaunch, 5
        )
        self.assertEqual(
            Intents.INSendMessageIntentResponseCodeFailureMessageServiceNotAvailable, 6
        )
        self.assertEqual(
            Intents.INSendMessageIntentResponseCodeFailureRequiringInAppAuthentication,
            7,
        )
