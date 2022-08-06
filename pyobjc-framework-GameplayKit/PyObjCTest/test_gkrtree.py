from PyObjCTools.TestSupport import TestCase

import GameplayKit
from objc import simd


class TestGKAgent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameplayKit.GKRTreeSplitStrategy)

    def testConstants(self):
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyHalve, 0)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyLinear, 1)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyQuadratic, 2)
        self.assertEqual(GameplayKit.GKRTreeSplitStrategyReduceOverlap, 3)

    def test_methods(self):
        self.assertArgHasTree(
            GameplayKit.GKRTree.addElement_boundingRectMin_boundingRectMax_splitStrategy_,
            2,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasTree(
            GameplayKit.GKRTree.addElement_boundingRectMin_boundingRectMax_splitStrategy_,
            3,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasTree(
            GameplayKit.GKRTree.removeElement_boundingRectMin_boundingRectMax_,
            2,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasTree(
            GameplayKit.GKRTree.removeElement_boundingRectMin_boundingRectMax_,
            3,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasTree(
            GameplayKit.GKRTree.elementsInBoundingRectMin_rectMax_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasTree(
            GameplayKit.GKRTree.elementsInBoundingRectMin_rectMax_,
            1,
            simd.vector_float2.__typestr__,
        )
