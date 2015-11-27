import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCControllerDirectionPad (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCControllerDirectionPad, objc.objc_class)

        @min_os_level("10.9")
        def testMethods(self):
            self.assertResultIsBlock(GameController.GCControllerDirectionPad.valueChangedHandler, b"v@ff")
            self.assertArgIsBlock(GameController.GCControllerDirectionPad.setValueChangedHandler_, 0, b"v@ff")

if __name__ == "__main__":
    main()
