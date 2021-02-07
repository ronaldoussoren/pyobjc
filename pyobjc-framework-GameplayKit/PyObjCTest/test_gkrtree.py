from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKAgent(TestCase):
    def testConstants(self):
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyHalve, 0)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyLinear, 1)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyQuadratic, 2)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyReduceOverlap, 3)
