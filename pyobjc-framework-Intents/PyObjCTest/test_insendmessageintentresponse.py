from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINSendMessageIntentResponse(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
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
