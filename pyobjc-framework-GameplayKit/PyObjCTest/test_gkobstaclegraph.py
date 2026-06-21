from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKObstacleGraph(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            GameplayKit.GKObstacleGraph.isConnectionLockedFromNode_toNode_
        )
