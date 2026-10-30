from PyObjCTools.TestSupport import TestCase
import GameController


class TestGCDeviceBattery(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameController.GCDeviceBatteryState)
        self.assertEqual(GameController.GCDeviceBatteryStateUnknown, -1)
        self.assertEqual(GameController.GCDeviceBatteryStateDischarging, 0)
        self.assertEqual(GameController.GCDeviceBatteryStateCharging, 1)
        self.assertEqual(GameController.GCDeviceBatteryStateFull, 2)
