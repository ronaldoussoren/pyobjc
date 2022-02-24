from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCRNNLayer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSRNNBidirectionalCombineMode)
        self.assertIsEnumType(MetalPerformanceShaders.MPSRNNMatrixId)
        self.assertIsEnumType(MetalPerformanceShaders.MPSRNNSequenceDirection)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSRNNSequenceDirectionForward, 0)
        self.assertEqual(MetalPerformanceShaders.MPSRNNSequenceDirectionBackward, 1)

        self.assertEqual(MetalPerformanceShaders.MPSRNNBidirectionalCombineModeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSRNNBidirectionalCombineModeAdd, 1)
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNBidirectionalCombineModeConcatenate, 2
        )

        self.assertEqual(MetalPerformanceShaders.MPSRNNBidirectionalCombineModeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSRNNBidirectionalCombineModeAdd, 1)
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNBidirectionalCombineModeConcatenate, 2
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdSingleGateInputWeights, 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdSingleGateRecurrentWeights, 1
        )
        self.assertEqual(MetalPerformanceShaders.MPSRNNMatrixIdSingleGateBiasTerms, 2)
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMInputGateInputWeights, 3
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMInputGateRecurrentWeights, 4
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMInputGateMemoryWeights, 5
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMInputGateBiasTerms, 6
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMForgetGateInputWeights, 7
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMForgetGateRecurrentWeights, 8
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMForgetGateMemoryWeights, 9
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMForgetGateBiasTerms, 10
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMMemoryGateInputWeights, 11
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMMemoryGateRecurrentWeights, 12
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMMemoryGateMemoryWeights, 13
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMMemoryGateBiasTerms, 14
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMOutputGateInputWeights, 15
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMOutputGateRecurrentWeights, 16
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMOutputGateMemoryWeights, 17
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdLSTMOutputGateBiasTerms, 18
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUInputGateInputWeights, 19
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUInputGateRecurrentWeights, 20
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUInputGateBiasTerms, 21
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRURecurrentGateInputWeights, 22
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRURecurrentGateRecurrentWeights, 23
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRURecurrentGateBiasTerms, 24
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUOutputGateInputWeights, 25
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUOutputGateRecurrentWeights, 26
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUOutputGateInputGateWeights, 27
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRNNMatrixIdGRUOutputGateBiasTerms, 28
        )

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNDescriptor.useLayerInputUnitTransformMode
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNDescriptor.setUseLayerInputUnitTransformMode_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNDescriptor.useFloat32Weights
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNDescriptor.setUseFloat32Weights_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSGRUDescriptor.flipOutputGates
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSGRUDescriptor.setFlipOutputGates_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSLSTMDescriptor.memoryWeightsAreDiagonal
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSLSTMDescriptor.setMemoryWeightsAreDiagonal_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNImageInferenceLayer.recurrentOutputIsTemporary
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNImageInferenceLayer.setRecurrentOutputIsTemporary_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNImageInferenceLayer.storeAllIntermediateStates
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNImageInferenceLayer.setStoreAllIntermediateStates_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixInferenceLayer.recurrentOutputIsTemporary
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixInferenceLayer.setRecurrentOutputIsTemporary_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixInferenceLayer.storeAllIntermediateStates
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixInferenceLayer.setStoreAllIntermediateStates_,
            0,
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.storeAllIntermediateStates
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.setStoreAllIntermediateStates_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.recurrentOutputIsTemporary
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.setRecurrentOutputIsTemporary_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.trainingStateIsTemporary
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.setTrainingStateIsTemporary_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.accumulateWeightGradients
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.setAccumulateWeightGradients_,
            0,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSRNNMatrixTrainingLayer.encodeCopyWeightsToCommandBuffer_weights_matrixId_matrix_copyFromWeightsToMatrix_matrixOffset_,  # noqa: B950
            4,
        )
