from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKGraph(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKGraph.connectNodeToLowestCostNode_bidirectional_, 1
        )
