from PyObjCTools.TestSupport import TestCase, min_sdk_level

import GameController


class TestGCPhysicalInputSource(TestCase):
    def test_constants(self):
        self.assertIsEnumType(GameController.GCPhysicalInputSourceDirection)
        self.assertEqual(GameController.GCPhysicalInputSourceDirectionNotApplicable, 0)
        self.assertEqual(GameController.GCPhysicalInputSourceDirectionUp, 1 << 0)
        self.assertEqual(GameController.GCPhysicalInputSourceDirectionRight, 1 << 1)
        self.assertEqual(GameController.GCPhysicalInputSourceDirectionDown, 1 << 2)
        self.assertEqual(GameController.GCPhysicalInputSourceDirectionLeft, 1 << 3)

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("GCPhysicalInputSource")
