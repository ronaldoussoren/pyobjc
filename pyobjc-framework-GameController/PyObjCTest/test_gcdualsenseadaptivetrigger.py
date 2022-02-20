from PyObjCTools.TestSupport import TestCase
import GameController


class TestGCDualSenseAdaptiveTrigger(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameController.GCDualSenseAdaptiveTriggerMode)
        self.assertIsEnumType(GameController.GCDualSenseAdaptiveTriggerStatus)

    def test_constants(self):
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerDiscretePositionCount, 10
        )

        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeOff, 0)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeFeedback, 1)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeWeapon, 2)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeVibration, 3)
        self.assertEqual(GameController.GCDualSenseAdaptiveTriggerModeSlopeFeedback, 4)

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
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusSlopeFeedbackReady, 7
        )
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusSlopeFeedbackApplyingLoad, 8
        )
        self.assertEqual(
            GameController.GCDualSenseAdaptiveTriggerStatusSlopeFeedbackFinished, 9
        )

    def test_structs(self):
        v = GameController.GCDualSenseAdaptiveTriggerPositionalAmplitudes()
        self.assertIs(v.values, None)

        v = GameController.GCDualSenseAdaptiveTriggerPositionalResistiveStrengths()
        self.assertIs(v.values, None)
