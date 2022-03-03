from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MetalPerformanceShaders

MPSNNGraphCompletionHandler = b"v@@"


class TestMPSNeuralNetwork_MPSNNGraph(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNGraph.initWithDevice_resultImage_resultImageIsNeeded_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNGraph.graphWithDevice_resultImage_resultImageIsNeeded_,
            2,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNGraph.outputStateIsTemporary
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNGraph.setOutputStateIsTemporary_, 0
        )

        self.assertResultIsBOOL(MetalPerformanceShaders.MPSNNGraph.resultImageIsNeeded)

        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSNNGraph.executeAsyncWithSourceImages_completionHandler_,
            1,
            MPSNNGraphCompletionHandler,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgHasType(
            MetalPerformanceShaders.MPSNNGraph.initWithDevice_resultImages_resultsAreNeeded_,
            2,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNNGraph.initWithDevice_resultImages_resultsAreNeeded_,
            2,
        )

        self.assertArgHasType(
            MetalPerformanceShaders.MPSNNGraph.graphWithDevice_resultImages_resultsAreNeeded_,
            2,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNNGraph.graphWithDevice_resultImages_resultsAreNeeded_,
            2,
        )
