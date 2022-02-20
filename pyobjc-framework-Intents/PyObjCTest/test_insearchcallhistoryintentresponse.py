from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINSearchCallHistoryIntentResponse(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INSearchCallHistoryIntentResponseCode)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeContinueInApp, 2)
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeFailure, 3)
        self.assertEqual(
            Intents.INSearchCallHistoryIntentResponseCodeFailureRequiringAppLaunch, 4
        )
        self.assertEqual(
            Intents.INSearchCallHistoryIntentResponseCodeFailureAppConfigurationRequired,
            5,
        )
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeInProgress, 6)
        self.assertEqual(Intents.INSearchCallHistoryIntentResponseCodeSuccess, 7)
