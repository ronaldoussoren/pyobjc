from PyObjCTools.TestSupport import TestCase
import objc
import GameController


class TestGCGamepadSnapshot(TestCase):
    def test_classes(self):
        self.assertIsInstance(GameController.GCGamepadSnapshot, objc.objc_class)

    def test_structs(self):
        self.assertEqual(GameController.GCGamepadSnapShotDataV100.__struct_pack__, 1)

        v = GameController.GCGamepadSnapShotDataV100()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.size, int)
        self.assertIsInstance(v.dpadX, float)
        self.assertIsInstance(v.dpadY, float)
        self.assertIsInstance(v.buttonA, float)
        self.assertIsInstance(v.buttonB, float)
        self.assertIsInstance(v.buttonX, float)
        self.assertIsInstance(v.buttonY, float)
        self.assertIsInstance(v.leftShoulder, float)
        self.assertIsInstance(v.rightShoulder, float)
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        self.assertResultIsBOOL(GameController.GCGamepadSnapShotDataV100FromNSData)
        self.assertArgIsOut(GameController.GCGamepadSnapShotDataV100FromNSData, 0)
        self.assertArgIsIn(GameController.NSDataFromGCGamepadSnapShotDataV100, 0)
