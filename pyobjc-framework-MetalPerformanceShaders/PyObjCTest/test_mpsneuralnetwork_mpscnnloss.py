from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNLoss(TestCase):
    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNYOLOLossDescriptor.rescore
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNYOLOLossDescriptor.setRescore_, 0
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradient.computeLabelGradients
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradient.setComputeLabelGradients_, 0
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNForwardLoss.encodeBatchToCommandBuffer_sourceImages_labels_weights_destinationStates_destinationStateIsTemporary_,  # noqa: B950
            5,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNLossDescriptor.reduceAcrossBatch
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNLossDescriptor.setReduceAcrossBatch_, 0
        )

        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNLoss.reduceAcrossBatch)

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNYOLOLossDescriptor.reduceAcrossBatch
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNYOLOLossDescriptor.setReduceAcrossBatch_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNYOLOLoss.reduceAcrossBatch
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNForwardLoss.reduceAcrossBatch
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradient.reduceAcrossBatch
        )
