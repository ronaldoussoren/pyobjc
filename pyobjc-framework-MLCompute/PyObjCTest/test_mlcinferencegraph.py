from PyObjCTools.TestSupport import TestCase, min_os_level

import MLCompute


class TestMLCInferenceGraph(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCInferenceGraph.addInputs_)
        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.addInputs_lossLabels_lossLabelWeights_
        )
        self.assertResultIsBOOL(MLCompute.MLCInferenceGraph.addOutputs_)
        self.assertResultIsBOOL(MLCompute.MLCInferenceGraph.compileWithOptions_device_)
        self.assertResultIsBOOL(MLCompute.MLCInferenceGraph.linkWithGraphs_)

        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.executeWithInputsData_batchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCInferenceGraph.executeWithInputsData_batchSize_options_completionHandler_,
            3,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.executeWithInputsData_outputsData_batchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MLCInferenceGraph.executeWithInputsData_outputsData_batchSize_options_completionHandler_,
            4,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MLCInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_,  # noqa: B950
            5,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MLCInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_,  # noqa: B950
            6,
            b"v@@d",
        )

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertResultIsBOOL(
            MLCompute.MLCInferenceGraph.compileWithOptions_device_inputTensors_inputTensorsData_
        )
