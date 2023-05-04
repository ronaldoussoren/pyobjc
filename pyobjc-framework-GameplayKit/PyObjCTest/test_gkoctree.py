from PyObjCTools.TestSupport import TestCase, min_os_level
import GameplayKit

from objc import simd


class TestGKOctree(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgHasType(
            GameplayKit.GKOctree.octreeWithBoundingBox_minimumCellSize_,
            0,
            GameplayKit.GKBox.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKOctree.initWithBoundingBox_minimumCellSize_,
            0,
            GameplayKit.GKBox.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKOctree.addElement_withBox_, 1, GameplayKit.GKBox.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKOctree.elementsInBox_, 0, GameplayKit.GKBox.__typestr__
        )

        self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_)
        self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_withNode_)

        self.assertArgHasType(
            GameplayKit.GKOctree.addElement_withPoint_,
            1,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKOctree.elementsAtPoint_, 0, simd.vector_float3.__typestr__
        )
