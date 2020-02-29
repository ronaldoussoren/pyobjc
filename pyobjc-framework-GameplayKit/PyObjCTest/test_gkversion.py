import sys

from PyObjCTools.TestSupport import *

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKVersion(TestCase):
        def testConstants(self):
            self.assertEqual(GameplayKit.GK_VERSION, 80_000_000)


if __name__ == "__main__":
    main()
