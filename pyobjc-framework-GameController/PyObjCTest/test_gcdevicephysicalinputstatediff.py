from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import GameController


class TestGCDevicePhysicalInputStateDiff(TestCase):
    def test_constants(self):
        self.assertIsEnumType(GameController.GCDevicePhysicalInputElementChange)
        self.assertEqual(GameController.GCDevicePhysicalInputElementUnknownChange, -1)
        self.assertEqual(GameController.GCDevicePhysicalInputElementNoChange, 0)
        self.assertEqual(GameController.GCDevicePhysicalInputElementChanged, 1)

    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCDevicePhysicalInputStateDiff")
