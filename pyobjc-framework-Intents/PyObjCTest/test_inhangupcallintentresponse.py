from PyObjCTools.TestSupport import TestCase
import Intents


class TestINHangUpCallIntentResponse(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INHangUpCallIntentResponseCode)
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INHangUpCallIntentResponseCodeFailureRequiringAppLaunch, 5
        )
        self.assertEqual(Intents.INHangUpCallIntentResponseCodeFailureNoCallToHangUp, 6)
