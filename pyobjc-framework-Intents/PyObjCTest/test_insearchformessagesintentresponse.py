from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINSearchForMessagesIntentResponse(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INSearchForMessagesIntentResponseCode)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INSearchForMessagesIntentResponseCodeFailureRequiringAppLaunch, 5
        )
        self.assertEqual(
            Intents.INSearchForMessagesIntentResponseCodeFailureMessageServiceNotAvailable,
            6,
        )
        self.assertEqual(
            Intents.INSearchForMessagesIntentResponseCodeFailureMessageTooManyResults, 7
        )
