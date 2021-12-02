from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCGamepadSnapshot(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCGamepadSnapshot, objc.objc_class)

    @min_os_level("10.9")
    def testStructs(self):
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

    @min_os_level("10.9")
    def testFunctions(self):
        self.assertResultIsBOOL(GameController.GCGamepadSnapShotDataV100FromNSData)
        self.assertArgIsOut(GameController.GCGamepadSnapShotDataV100FromNSData, 0)
        self.assertArgIsIn(GameController.NSDataFromGCGamepadSnapShotDataV100, 0)
