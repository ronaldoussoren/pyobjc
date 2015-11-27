import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCControllerButtonInput (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCControllerButtonInput, objc.objc_class)

        @min_os_level("10.9")
        def testMethods(self):
            self.assertResultIsBlock(GameController.GCControllerButtonInput.valueChangedHandler, b"v@f" + objc._C_NSBOOL)
            self.assertArgIsBlock(GameController.GCControllerButtonInput.setValueChangedHandler_, 0, b"v@f" + objc._C_NSBOOL)

            self.assertResultIsBOOL(GameController.GCControllerButtonInput.isPressed)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertResultIsBlock(GameController.GCControllerButtonInput.pressedChangedHandler, b"v@f" + objc._C_NSBOOL)
            self.assertArgIsBlock(GameController.GCControllerButtonInput.setPressedChangedHandler_, 0, b"v@f" + objc._C_NSBOOL)

if __name__ == "__main__":
    main()
