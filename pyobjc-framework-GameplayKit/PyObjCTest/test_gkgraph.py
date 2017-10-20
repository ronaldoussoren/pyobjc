from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKGraph (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(GameplayKit.GKGraph.connectNodeToLowestCostNode_bidirectional_, 1)

if __name__ == "__main__":
    main()
