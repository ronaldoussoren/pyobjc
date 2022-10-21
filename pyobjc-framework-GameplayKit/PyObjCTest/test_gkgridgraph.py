from PyObjCTools.TestSupport import TestCase

import GameplayKit

from objc import simd


class TestGKGridGraph(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKGridGraph.diagonalsAllowed)

        self.assertResultHasType(
            GameplayKit.GKGridGraph.gridOrigin, simd.vector_int2.__typestr__
        )

        # SIMD types
        self.assertArgHasType(
            GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_,
            0,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_,
            3,
        )
        self.assertArgHasType(
            GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_,
            0,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_,
            3,
        )

        self.assertArgHasType(
            GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_,
            0,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGridGraph.graphFromGridStartingAt_width_height_diagonalsAllowed_,
            3,
        )
        self.assertArgHasType(
            GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_,
            0,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGridGraph.initFromGridStartingAt_width_height_diagonalsAllowed_,
            3,
        )

        self.assertArgHasType(
            GameplayKit.GKGridGraph.nodeAtGridPosition_, 0, simd.vector_int2.__typestr__
        )
