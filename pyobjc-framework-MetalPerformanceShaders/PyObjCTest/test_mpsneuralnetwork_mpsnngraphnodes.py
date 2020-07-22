from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MetalPerformanceShaders

MPSGradientNodeBlock = b"v@@@@"


class TestMPSNNGraphNodesHelper(MetalPerformanceShaders.NSObject):
    def trainingStyle(self):
        return 1

    def setTrainingStyle_(self, a):
        pass


class TestMPSNNGraphNodes(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MPSHandle")
        objc.protocolNamed("MPSNNTrainableNode")
        objc.protocolNamed("MPSNNGramMatrixCallback")
        objc.protocolNamed("MPSNNLossCallback")

    def test_methods(self):
        self.assertResultHasType(
            TestMPSNNGraphNodesHelper.trainingStyle, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMPSNNGraphNodesHelper.setTrainingStyle_, 0, objc._C_NSUInteger
        )

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSNNImageNode.exportFromGraph)
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNImageNode.setExportFromGraph_, 0
        )

        self.assertResultIsBOOL(MetalPerformanceShaders.MPSNNStateNode.exportFromGraph)
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNStateNode.setExportFromGraph_, 0
        )

        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSNNFilterNode.trainingGraphWithSourceGradient_nodeHandler_,
            1,
            MPSGradientNodeBlock,
        )

        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.nodeWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            3,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
            b"n^f",
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSCNNBinaryFullyConnectedNode.initWithSource_weights_outputBiasTerms_outputScaleTerms_inputBiasTerms_inputScaleTerms_type_flags_,  # noqa: B950
            5,
        )

    @min_os_level("10.13.4")
    def test_methods10_13_4(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNImageNode.synchronizeResource
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNImageNode.setSynchronizeResource_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNStateNode.synchronizeResource
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNStateNode.setSynchronizeResource_, 0
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNArithmeticGradientNode.nodeWithSourceGradient_sourceImage_gradientState_isSecondarySourceFilter_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNArithmeticGradientNode.initWithSourceGradient_sourceImage_gradientState_isSecondarySourceFilter_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNArithmeticGradientNode.initWithGradientImages_forwardFilter_isSecondarySourceFilter_,
            2,
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNArithmeticGradientNode.isSecondarySourceFilter
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNUpsamplingBilinearNode.nodeWithSource_integerScaleFactorX_integerScaleFactorY_alignCorners_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNUpsamplingBilinearNode.initWithSource_integerScaleFactorX_integerScaleFactorY_alignCorners_,  # noqa: B950
            3,
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNUpsamplingBilinearNode.alignCorners
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSNNImageNode.stopGradient)
        self.assertArgIsBOOL(MetalPerformanceShaders.MPSNNImageNode.setStopGradient_, 0)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.isLabelsGradientFilter
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.nodeWithSourceGradient_sourceImage_labels_weights_gradientState_lossDescriptor_isLabelsGradientFilter_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.nodeWithSourceGradient_sourceImage_labels_gradientState_lossDescriptor_isLabelsGradientFilter_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.nodeWithSources_gradientState_lossDescriptor_isLabelsGradientFilter_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.initWithSourceGradient_sourceImage_labels_weights_gradientState_lossDescriptor_isLabelsGradientFilter_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.initWithSourceGradient_sourceImage_labels_gradientState_lossDescriptor_isLabelsGradientFilter_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.initWithSources_gradientState_lossDescriptor_isLabelsGradientFilter_,
            3,
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNForwardLossNode.reduceAcrossBatch
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNLossGradientNode.reduceAcrossBatch
        )
