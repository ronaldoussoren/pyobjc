from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphCore(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphPaddingMode)
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphPaddingStyle)
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphReductionMode)
        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayout
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphShapedType.isEqualTo_
        )

    def test_constants(self):
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutNCHW, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutNHWC, 1
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutOIHW, 2
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutHWIO, 3
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutCHW, 4
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutHWC, 5
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutHW, 6
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutNCDHW, 7
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutNDHWC, 8
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutOIDHW, 9
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphTensorNamedDataLayoutDHWIO, 10
        )

        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingStyleExplicit, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingStyleTF_VALID, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingStyleTF_SAME, 2)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPaddingStyleExplicitOffset, 3
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPaddingStyleONNX_SAME_LOWER, 4
        )

        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModeConstant, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModeReflect, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModeSymmetric, 2)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModeClampToEdge, 3)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModeZero, 4)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphPaddingModePeriodic, 5)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPaddingModeAntiPeriodic, 6
        )

        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphReductionModeMin, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphReductionModeMax, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphReductionModeSum, 2)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphReductionModeProduct, 3)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphReductionModeArgumentMin, 4
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphReductionModeArgumentMax, 5
        )
