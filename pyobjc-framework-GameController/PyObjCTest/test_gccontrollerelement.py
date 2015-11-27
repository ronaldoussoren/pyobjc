import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCControllerElement (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCControllerElement, objc.objc_class)

        @min_os_level("10.9")
        def testMethods(self):
            self.assertResultIsBOOL(GameController.GCControllerElement.isAnalog)

if __name__ == "__main__":
    main()
