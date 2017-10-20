from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKObstacleGraph (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKObstacleGraph.isConnectionLockedFromNode_toNode_)


if __name__ == "__main__":
    main()
