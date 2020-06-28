from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMCLInferenceGraph(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MCLInferenceGraph.addInputs_)
        self.assertResultIsBOOL(
            MLCompute.MCLInferenceGraph.addInputs_lossLabels_lossLabelWeights_
        )
        self.assertResultIsBOOL(MLCompute.MCLInferenceGraph.addOutputs_)
        self.assertResultIsBOOL(MLCompute.MCLInferenceGraph.compileWithOptions_device_)
        self.assertResultIsBOOL(MLCompute.MCLInferenceGraph.linkWithGraphs_)

        self.assertResultIsBOOL(
            MLCompute.MCLInferenceGraph.executeWithInputsData_batchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MCLInferenceGraph.executeWithInputsData_batchSize_options_completionHandler_,
            3,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MCLInferenceGraph.executeWithInputsData_outputsData_batchSize_options_completionHandler_
        )
        self.assertArgIsBlock(
            MLCompute.MCLInferenceGraph.executeWithInputsData_outputsData_batchSize_options_completionHandler_,
            4,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MCLInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MCLInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_batchSize_options_completionHandler_,  # noqa: B950
            5,
            b"v@@d",
        )

        self.assertResultIsBOOL(
            MLCompute.MCLInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_  # noqa: B950
        )
        self.assertArgIsBlock(
            MLCompute.MCLInferenceGraph.executeWithInputsData_lossLabelsData_lossLabelWeightsData_outputsData_batchSize_options_completionHandler_,  # noqa: B950
            6,
            b"v@@d",
        )
