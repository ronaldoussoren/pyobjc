from PyObjCTools.TestSupport import TestCase
import Intents


class TestINShareFocusStatusIntentResponse(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INShareFocusStatusIntentResponseCode)

    def test_constants(self):
        self.assertEqual(Intents.INShareFocusStatusIntentResponseCodeUnspecified, 0)
        self.assertEqual(Intents.INShareFocusStatusIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INShareFocusStatusIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INShareFocusStatusIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INShareFocusStatusIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INShareFocusStatusIntentResponseCodeFailureRequiringAppLaunch, 5
        )
