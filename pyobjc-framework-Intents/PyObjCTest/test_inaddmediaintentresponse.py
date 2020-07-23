from PyObjCTools.TestSupport import TestCase
import Intents


class TestINAddMediaIntentResponse(TestCase):
    def testConstants(self):
        self.assertEqual(Intents.INAddMediaIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INAddMediaIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INAddMediaIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INAddMediaIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INAddMediaIntentResponseCodeHandleInApp, 4)
        self.assertEqual(Intents.INAddMediaIntentResponseCodeFailure, 5)
        self.assertEqual(
            Intents.INAddMediaIntentResponseCodeFailureRequiringAppLaunch, 6
        )
