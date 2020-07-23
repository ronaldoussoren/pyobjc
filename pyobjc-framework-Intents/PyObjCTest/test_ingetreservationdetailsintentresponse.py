from PyObjCTools.TestSupport import TestCase
import Intents


class TestINGetReservationDetailsIntentResponse(TestCase):
    def testConstants(self):
        self.assertEqual(
            Intents.INGetReservationDetailsIntentResponseCodeUnspecified, 0
        )
        self.assertEqual(Intents.INGetReservationDetailsIntentResponseCodeReady, 1)
        self.assertEqual(Intents.INGetReservationDetailsIntentResponseCodeInProgress, 2)
        self.assertEqual(Intents.INGetReservationDetailsIntentResponseCodeSuccess, 3)
        self.assertEqual(Intents.INGetReservationDetailsIntentResponseCodeFailure, 4)
        self.assertEqual(
            Intents.INGetReservationDetailsIntentResponseCodeFailureRequiringAppLaunch,
            5,
        )
