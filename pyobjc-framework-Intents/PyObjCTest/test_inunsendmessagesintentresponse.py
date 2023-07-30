from PyObjCTools.TestSupport import TestCase
import Intents


class TestINUnsendMessagesIntentResponse(TestCase):
    def testConstants(self):
        self.assertIsEnumType(Intents.INUnsendMessagesIntentResponseCode)
        self.assertEqual(Intents.INUnsendMessagesIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INUnsendMessagesIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INUnsendMessagesIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INUnsendMessagesIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INUnsendMessagesIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureRequiringAppLaunch, 5
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureMessageNotFound, 6
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailurePastUnsendTimeLimit, 7
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureMessageTypeUnsupported, 8
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureUnsupportedOnService, 9
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureMessageServiceNotAvailable,
            10,
        )
        self.assertEqual(
            Intents.INUnsendMessagesIntentResponseCodeFailureRequiringInAppAuthentication,
            11,
        )
