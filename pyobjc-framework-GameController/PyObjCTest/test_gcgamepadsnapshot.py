import sys
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCGamepadSnapshot (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCGamepadSnapshotCController, objc.objc_class)

        @min_os_level("10.9")
        def testStructs(self):
            self.assertEqual(GameController.GCGamepadSnapShotDataV100.__struct_pack__, 1)

            v = GameController.GCGamepadSnapShotDataV100()
            self.assertIsInstance(v.version, int)
            self.assertIsInstance(v.size, int)
            self.assertIsInstance(v.dpadX, int)
            self.assertIsInstance(v.dpadY, int)
            self.assertIsInstance(v.buttonA, int)
            self.assertIsInstance(v.buttonB, int)
            self.assertIsInstance(v.buttonX, int)
            self.assertIsInstance(v.buttonY, int)
            self.assertIsInstance(v.leftShoulder, int)
            self.assertIsInstance(v.rightShoulder, int)

        @min_os_level("10.9")
        def testFunctions(self):
            self.assertResultIsBOOL(GameController.GCGamepadSnapShotDataV100FromNSData)
            self.assertArgIsOut(GameController.GCGamepadSnapShotDataV100FromNSData, 0)
            self.assertArgIsIn(GameController.NSDataFromGCGamepadSnapShotDataV100, 0)

if __name__ == "__main__":
    main()
