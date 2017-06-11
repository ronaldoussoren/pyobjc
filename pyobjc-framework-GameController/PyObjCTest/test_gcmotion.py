import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCMotion (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(GameController.GCMotion, objc.objc_class)

        @min_os_level("10.10")
        def test_structs(self):
            v = GameController.GCAcceleration()
            self.assertIsInstance(v.x, float)
            self.assertIsInstance(v.y, float)
            self.assertIsInstance(v.z, float)

            v = GameController.GCRotationRate()
            self.assertIsInstance(v.x, float)
            self.assertIsInstance(v.y, float)
            self.assertIsInstance(v.z, float)

            v = GameController.GCQuaternion()
            self.assertIsInstance(v.x, float)
            self.assertIsInstance(v.y, float)
            self.assertIsInstance(v.z, float)
            self.assertIsInstance(v.w, float)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBlock(GameController.GCMotion.valueChangedHandler, b"v@")
            self.assertArgIsBlock(GameController.GCMotion.setValueChangedHandler_, 0, b"v@")

        @min_os_level("10.13")
        def testMethods(self):
            self.assertResultIsBOOL(GameController.GCMotion.hasAttitudeAndRotationRate)

if __name__ == "__main__":
    main()
