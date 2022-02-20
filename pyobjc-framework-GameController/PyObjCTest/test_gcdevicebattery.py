from PyObjCTools.TestSupport import TestCase
import GameController


class TestGCDeviceBattery(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameController.GCDeviceBatteryState)

    def test_constants(self):
        self.assertEqual(GameController.GCDeviceBatteryStateUnknown, -1)
        self.assertEqual(GameController.GCDeviceBatteryStateDischarging, 0)
        self.assertEqual(GameController.GCDeviceBatteryStateCharging, 1)
        self.assertEqual(GameController.GCDeviceBatteryStateFull, 2)
