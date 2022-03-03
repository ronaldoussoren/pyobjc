from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNConvolutionHelper(MetalPerformanceShaders.NSObject):
    def dataType(self):
        return 1

    def weights(self):
        return 1

    def biasTerms(self):
        return 1

    def load(self):
        return 1

    def weightsQuantizationType(self):
        return 1

    def updateWithGradientState_sourceState_(self, a, b):
        return 1

    def weightsLayout(self):
        return 1

    def kernelWeightsDataType(self):
        return 1

    # def rangesForUInt8Kernel(self): return 1


class TestMPSNeuralNetwork_MPSCNNConvolution(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNConvolutionGradientOption)
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNConvolutionWeightsLayout)
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNWeightsQuantizationType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSCNNConvolutionWeightsLayoutOHWI, 0)

        self.assertEqual(MetalPerformanceShaders.MPSCNNWeightsQuantizationTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCNNWeightsQuantizationTypeLinear, 1)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNWeightsQuantizationTypeLookupTable, 2
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSCNNConvolutionGradientOptionGradientWithData, 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNConvolutionGradientOptionGradientWithWeightsAndBias,
            2,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNConvolutionGradientOptionAll,
            MetalPerformanceShaders.MPSCNNConvolutionGradientOptionGradientWithData
            | MetalPerformanceShaders.MPSCNNConvolutionGradientOptionGradientWithWeightsAndBias,
        )

    def test_protocols(self):
        objc.protocolNamed("MPSCNNConvolutionDataSource")

    def test_methods(self):
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.dataType, b"I"
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.weights, b"^v"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.weights
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.biasTerms, b"^f"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.biasTerms
        )
        self.assertResultIsBOOL(TestMPSNeuralNetwork_MPSCNNConvolutionHelper.load)

        # self.assertResultHasType(TestMPSNeuralNetwork_MPSCNNConvolutionHelper.dataType, ...) # Vector type!
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.weightsQuantizationType, b"I"
        )
        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.updateWithGradientState_sourceState_
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.weightsLayout, b"I"
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNConvolutionHelper.kernelWeightsDataType, b"I"
        )

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.supportsSecureCoding
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            0,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            1,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            1,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            2,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            2,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolutionDescriptor.setBatchNormalizationParametersForInferenceWithMean_variance_gamma_beta_epsilon_,  # noqa: B950
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolution.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            2,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolution.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            2,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNConvolution.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNConvolution.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNFullyConnected.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            2,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNFullyConnected.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            3,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNFullyConnected.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNFullyConnected.initWithDevice_convolutionDescriptor_kernelWeights_biasTerms_flags_,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolution.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnected.initWithDevice_convolutionData_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

    @min_os_level("10.13.4")
    def test_methods10_13_4(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNConvolutionGradient.serializeWeightsAndBiases
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNConvolutionTranspose.exportWeightsAndBiasesWithCommandBuffer_resultStateCanBeTemporary_,
            1,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNConvolutionTranspose.encodeToCommandBuffer_sourceImage_convolutionGradientState_destinationState_destinationStateIsTemporary_,  # noqa: B950
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNConvolutionTranspose.encodeBatchToCommandBuffer_sourceImages_convolutionGradientStates_destinationStates_destinationStateIsTemporary_,  # noqa: B950
            4,
        )
