from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKObstacleGraph(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            GameplayKit.GKObstacleGraph.isConnectionLockedFromNode_toNode_
        )
