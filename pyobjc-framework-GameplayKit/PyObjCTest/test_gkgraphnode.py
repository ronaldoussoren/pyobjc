from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKGraphNode (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(GameplayKit.GKGraphNode.addConnectionsToNodes_bidirectional_, 1)
            self.assertArgIsBOOL(GameplayKit.GKGraphNode.removeConnectionsToNodes_bidirectional_, 1)

if __name__ == "__main__":
    main()
