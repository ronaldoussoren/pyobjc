from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNOptimzers(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSNNRegularizationType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSNNRegularizationTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNNRegularizationTypeL1, 1)
        self.assertEqual(MetalPerformanceShaders.MPSNNRegularizationTypeL2, 2)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerDescriptor.applyGradientClipping
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerDescriptor.setApplyGradientClipping_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizer.applyGradientClipping
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerStochasticGradientDescent.useNestrovMomentum
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerStochasticGradientDescent.useNesterovMomentum
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerStochasticGradientDescent.initWithDevice_momentumScale_useNestrovMomentum_optimizerDescriptor_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNOptimizerStochasticGradientDescent.initWithDevice_momentumScale_useNesterovMomentum_optimizerDescriptor_,  # noqa: B950
            2,
        )
