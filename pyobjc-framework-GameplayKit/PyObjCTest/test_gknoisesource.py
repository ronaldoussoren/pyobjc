from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKNoiseSource (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKVoronoiNoiseSource.isDistanceEnabled)
            self.assertArgIsBOOL(GameplayKit.GKVoronoiNoiseSource.setDistanceEnabled_, 0)


if __name__ == "__main__":
    main()
