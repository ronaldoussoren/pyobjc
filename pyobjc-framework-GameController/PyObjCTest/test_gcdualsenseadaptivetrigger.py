from PyObjCTools.TestSupport import TestCase
import GameController


class TestGCDualSenseAdaptiveTrigger(TestCase):
    def test_constants(self):
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeOff, 0)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeFeedback, 1)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeWeapon, 2)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeVibration, 3)

        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerStatusUnknown, -1)
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusFeedbackNoLoad, 0
        )
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusFeedbackLoadApplied, 1
        )
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerStatusWeaponReady, 2)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerStatusWeaponFiring, 3)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerStatusWeaponFired, 4)
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusVibrationNotVibrating, 5
        )
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusVibrationIsVibrating, 6
        )
