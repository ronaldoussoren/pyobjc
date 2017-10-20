from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKVersion (TestCase):
        def testConstants(self):
            self.assertEqual(GameplayKit.GK_VERSION, 80000000)


if __name__ == "__main__":
    main()
