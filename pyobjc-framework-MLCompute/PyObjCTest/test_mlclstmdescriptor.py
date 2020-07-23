from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCLSTMDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCLSTMDescriptor.usesBiases)
        self.assertResultIsBOOL(MLCompute.MLCLSTMDescriptor.batchFirst)
        self.assertResultIsBOOL(MLCompute.MLCLSTMDescriptor.isBidirectional)
        self.assertResultIsBOOL(MLCompute.MLCLSTMDescriptor.returnsSequences)

        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_isBidirectional_dropout_,
            3,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_isBidirectional_dropout_,
            4,
        )

        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_isBidirectional_dropout_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_isBidirectional_dropout_,  # noqa: B950
            4,
        )

        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_,  # noqa: B950
            6,
        )

        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_resultMode_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_resultMode_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_resultMode_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCLSTMDescriptor.descriptorWithInputSize_hiddenSize_layerCount_usesBiases_batchFirst_isBidirectional_returnsSequences_dropout_resultMode_,  # noqa: B950
            6,
        )
