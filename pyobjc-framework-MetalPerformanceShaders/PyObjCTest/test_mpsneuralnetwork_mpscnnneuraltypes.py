from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNNeuronTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNNeuronType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeReLU, 1)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeLinear, 2)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeSigmoid, 3)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeHardSigmoid, 4)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeTanH, 5)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeAbsolute, 6)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeSoftPlus, 7)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeSoftSign, 8)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeELU, 9)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypePReLU, 10)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeReLUN, 11)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypePower, 12)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeExponential, 13)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeLogarithm, 14)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeGeLU, 15)
        self.assertEqual(MetalPerformanceShaders.MPSCNNNeuronTypeCount, 16)
