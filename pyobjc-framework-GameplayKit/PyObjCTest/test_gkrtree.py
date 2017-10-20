from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKAgent (TestCase):
        def testConstants(self):
            self.assertEqual(GameplayKit.GKRTreeSplitStrategyHalve, 0)
            self.assertEqual(GameplayKit.GKRTreeSplitStrategyLinear, 1)
            self.assertEqual(GameplayKit.GKRTreeSplitStrategyQuadratic, 2)
            self.assertEqual(GameplayKit.GKRTreeSplitStrategyReduceOverlap, 3)

if __name__ == "__main__":
    main()
