from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNKernel(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNKernel.isBackwards)
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNKernel.isStateModified)

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNKernel.encodeToCommandBuffer_sourceImage_destinationState_destinationStateIsTemporary_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNKernel.encodeBatchToCommandBuffer_sourceImages_destinationStates_destinationStateIsTemporary_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNBinaryKernel.isBackwards)
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNBinaryKernel.isStateModified
        )

    @min_os_level("10.13.4")
    def test_methods10_13_4(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNKernel.isResultStateReusedAcrossBatch
        )
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNKernel.appendBatchBarrier)

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNBinaryKernel.encodeToCommandBuffer_primaryImage_secondaryImage_destinationState_destinationStateIsTemporary_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNBinaryKernel.encodeBatchToCommandBuffer_primaryImages_secondaryImages_destinationStates_destinationStateIsTemporary_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNBinaryKernel.isResultStateReusedAcrossBatch
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNBinaryKernel.appendBatchBarrier
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.isBackwards
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.isStateModified
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.encodeToCommandBuffer_sourceImages_destinationState_destinationStateIsTemporary_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.encodeBatchToCommandBuffer_sourceImages_destinationStates_destinationStateIsTemporary_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.isResultStateReusedAcrossBatch
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiaryKernel.appendBatchBarrier
        )
