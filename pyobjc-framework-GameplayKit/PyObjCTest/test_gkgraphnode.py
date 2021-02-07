from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKGraphNode(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKGraphNode.addConnectionsToNodes_bidirectional_, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGraphNode.removeConnectionsToNodes_bidirectional_, 1
        )
