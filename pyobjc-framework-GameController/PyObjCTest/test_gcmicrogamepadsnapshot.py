import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCMicroGamepadSnapshot (TestCase):
        @expectedFailureIf(os_release() == '10.11')
        @min_os_level("10.11")
        def testClasses(self):
            self.assertIsInstance(GameController.GCMicroGamepadSnapshot, objc.objc_class)

        @min_os_level("10.11")
        def testStructs(self):
            self.assertEqual(GameController.GCMicroGamepadSnapShotDataV100.__struct_pack__, 1)

            v = GameController.GCMicroGamepadSnapShotDataV100()
            self.assertIsInstance(v.version, int)
            self.assertIsInstance(v.size, int)
            self.assertIsInstance(v.dpadX, float)
            self.assertIsInstance(v.dpadY, float)
            self.assertIsInstance(v.buttonA, float)
            self.assertIsInstance(v.buttonX, float)

        @expectedFailureIf(os_release().rsplit('.', 1)[0] in ('10.9', '10.10', '10.11'))
        @min_os_level("10.9")
        def testFunctions(self):
            self.assertResultIsBOOL(GameController.GCMicroGamepadSnapShotDataV100FromNSData)
            self.assertArgIsOut(GameController.GCMicroGamepadSnapShotDataV100FromNSData, 0)
            self.assertArgIsIn(GameController.NSDataFromGCMicroGamepadSnapShotDataV100, 0)

if __name__ == "__main__":
    main()
