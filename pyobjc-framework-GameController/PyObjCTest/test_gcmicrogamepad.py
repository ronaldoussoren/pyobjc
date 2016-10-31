import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCMicroGamepad (TestCase):
        @expectedFailureIf(os_release() == '10.11')
        @min_os_level("10.11")
        def testClasses(self):
            self.assertIsInstance(GameController.GCMicroGamepad, objc.objc_class)

        @expectedFailureIf(os_release() == '10.11')
        @min_os_level("10.11")
        def testMethods(self):
            self.assertResultIsBlock(GameController.GCMicroGamepad.valueChangedHandler, b'v@@')
            self.assertArgIsBlock(GameController.GCMicroGamepad.setValueChangedHandler_, 0, b'v@@')

            self.assertResultIsBOOL(GameController.GCMicroGamepad.reportsAbsoluteDpadValues)
            self.assertArgIsBOOL(GameController.GCMicroGamepad.setReportsAbsoluteDpadValues_, 0)

            self.assertResultIsBOOL(GameController.GCMicroGamepad.allowsRotation)
            self.assertArgIsBOOL(GameController.GCMicroGamepad.setAllowsRotation_, 0)

if __name__ == "__main__":
    main()
