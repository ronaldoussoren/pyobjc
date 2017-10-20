from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKNoise (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(GameplayKit.GKNoise.remapValuesToTerracesWithPeaks_terracesInverted_, 1)


if __name__ == "__main__":
    main()
