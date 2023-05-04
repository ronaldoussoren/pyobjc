from PyObjCTools.TestSupport import TestCase, min_os_level

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

    @min_os_level("10.12")
    def test_methods(self):
        self.assertArgHasType(
            GameplayKit.GKRTree.addElement_boundingRectMin_boundingRectMax_splitStrategy_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKRTree.addElement_boundingRectMin_boundingRectMax_splitStrategy_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKRTree.removeElement_boundingRectMin_boundingRectMax_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKRTree.removeElement_boundingRectMin_boundingRectMax_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKRTree.elementsInBoundingRectMin_rectMax_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKRTree.elementsInBoundingRectMin_rectMax_,
            1,
            simd.vector_float2.__typestr__,
        )
