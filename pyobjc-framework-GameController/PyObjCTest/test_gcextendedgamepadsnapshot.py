import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCExtendedGamepadSnapshot (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCExtendedGamepadSnapshot, objc.objc_class)

        @min_os_level("10.9")
        def testFunctions(self):
            self.assertResultIsBOOL(GameController.GCExtendedGamepadSnapShotDataV100FromNSData)
            self.assertArgIsOut(GameController.GCExtendedGamepadSnapShotDataV100FromNSData, 0)

            self.assertArgIsOut(GameController.GCExtendedGamepadSnapShotDataV100FromNSData, 0)

        @min_os_level("10.9")
        def test_structs(self):
            self.assertEqual(GameController.GCExtendedGamepadSnapShotDataV100.__struct_pack__, 1)

            v = GameController.GCExtendedGamepadSnapShotDataV100()
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
            self.assertIsInstance(v.leftThumbstickX, float)
            self.assertIsInstance(v.leftThumbstickY, float)
            self.assertIsInstance(v.rightThumbstickX, float)
            self.assertIsInstance(v.rightThumbstickY, float)
            self.assertIsInstance(v.leftTrigger, float)
            self.assertIsInstance(v.rightTrigger, float)

if __name__ == "__main__":
    main()
