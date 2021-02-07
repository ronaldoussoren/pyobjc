from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNReshape(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNReshape.encodeToCommandBuffer_sourceImage_destinationState_destinationStateIsTemporary_reshapedWidth_reshapedHeight_reshapedFeatureChannels_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNReshape.encodeBatchToCommandBuffer_sourceImages_destinationStates_destinationStateIsTemporary_reshapedWidth_reshapedHeight_reshapedFeatureChannels_,  # noqa: B950
            3,
        )
