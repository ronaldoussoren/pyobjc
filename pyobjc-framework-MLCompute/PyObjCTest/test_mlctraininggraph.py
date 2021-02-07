from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTrainingGraph(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.addInputs_lossLabels_)
        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.addInputs_lossLabels_lossLabelWeights_
        )
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.addOutputs_)
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.stopGradientForTensors_)
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.compileWithOptions_device_)
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.compileOptimizer_)
        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.linkWithGraphs_)

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_,  # noqa: B950
            5,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_,  # noqa: B950
            6,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeForwardWithBatchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeForwardWithBatchSize_options_completionHandler_,
            2,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeForwardWithBatchSize_options_outputsData_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeForwardWithBatchSize_options_outputsData_completionHandler_,
            3,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeGradientWithBatchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeGradientWithBatchSize_options_completionHandler_,
            2,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.executeGradientWithBatchSize_options_outputsData_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCTrainingGraph.executeGradientWithBatchSize_options_outputsData_completionHandler_,
            3,
            b"v@@d",
        )

        self.assertResultIsBOOL(MLCompute.MLCTrainingGraph.setTrainingTensorParameters_)

        self.assertResultIsBOOL(
            MLCompute.MLCTrainingGraph.bindOptimizerData_deviceData_withTensor_
        )
