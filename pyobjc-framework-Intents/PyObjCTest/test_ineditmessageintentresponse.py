from PyObjCTools.TestSupport import TestCase
import Intents


class INEditMessageIntentResponse(TestCase):
    def testConstants(self):
        self.assertIsEnumType(Intents.INEditMessageIntentResponseCode)
        self.assertEqual(Intents.INEditMessageIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INEditMessageIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INEditMessageIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INEditMessageIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INEditMessageIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureRequiringAppLaunch, 5
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureMessageNotFound, 6
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailurePastEditTimeLimit, 7
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureMessageTypeUnsupported, 8
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureUnsupportedOnService, 9
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureMessageServiceNotAvailable, 10
        )
        self.assertEqual(
            Intents.INEditMessageIntentResponseCodeFailureRequiringInAppAuthentication,
            11,
        )
