from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKGridGraph (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKGridGraph.diagonalsAllowed)

            # SIMD types
            #self.assertArgIsBOOL(GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_, 3)
            #self.assertArgIsBOOL(GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_, 3)

            #self.assertArgIsBOOL(GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_, 3)
            #self.assertArgIsBOOL(GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_, 3)


if __name__ == "__main__":
    main()
