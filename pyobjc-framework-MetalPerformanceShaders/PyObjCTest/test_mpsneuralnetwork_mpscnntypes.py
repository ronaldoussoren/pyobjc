from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNLossType)
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNReductionType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeMeanAbsoluteError, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeMeanSquaredError, 1)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeSoftMaxCrossEntropy, 2)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeSigmoidCrossEntropy, 3)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNLossTypeCategoricalCrossEntropy, 4
        )
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeHinge, 5)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeHuber, 6)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeCosineDistance, 7)
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeLog, 8)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNLossTypeKullbackLeiblerDivergence, 9
        )
        self.assertEqual(MetalPerformanceShaders.MPSCNNLossTypeCount, 10)

        self.assertEqual(MetalPerformanceShaders.MPSCNNReductionTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCNNReductionTypeSum, 1)
        self.assertEqual(MetalPerformanceShaders.MPSCNNReductionTypeMean, 2)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNReductionTypeSumByNonZeroWeights, 3
        )
        self.assertEqual(MetalPerformanceShaders.MPSCNNReductionTypeCount, 4)
