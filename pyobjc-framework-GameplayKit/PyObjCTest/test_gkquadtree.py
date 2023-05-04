from PyObjCTools.TestSupport import TestCase, min_os_level

import GameplayKit
from objc import simd


class TestGKQuadtree(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultHasType(
            GameplayKit.GKQuadtreeNode.quad, GameplayKit.GKQuad.__typestr__
        )

        self.assertArgHasType(
            GameplayKit.GKQuadtree.quadtreeWithBoundingQuad_minimumCellSize_,
            0,
            GameplayKit.GKQuad.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKQuadtree.initWithBoundingQuad_minimumCellSize_,
            0,
            GameplayKit.GKQuad.__typestr__,
        )

        self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_)
        self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_withNode_)

        self.assertArgHasType(
            GameplayKit.GKQuadtree.addElement_withPoint_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKQuadtree.addElement_withQuad_,
            1,
            GameplayKit.GKQuad.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKQuadtree.elementsInQuad_, 0, GameplayKit.GKQuad.__typestr__
        )

        self.assertArgHasType(
            GameplayKit.GKQuadtree.elementsAtPoint_, 0, simd.vector_float2.__typestr__
        )
