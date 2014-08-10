import sys
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCGamePad (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(GameController.GCGamePad, objc.objc_class)

        @min_os_level("10.9")
        def testMethods(self):
            self.assertResultIsBlock(GameController.GCGamePad.valueChangedHandler, b"v@@")
            self.assertArgIsBlock(GameController.GCGamePad.setValueChangedHandler_, 0, b"v@@")

if __name__ == "__main__":
    main()
