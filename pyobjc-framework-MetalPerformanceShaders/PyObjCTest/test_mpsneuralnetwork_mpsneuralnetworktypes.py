from PyObjCTools.TestSupport import TestCase
import objc
import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSNeuralNetworkTypesHelper(
    MetalPerformanceShaders.NSObject
):
    def paddingMethod(self):
        return 1

    def sourceWidth(self):
        return 1

    def sourceHeight(self):
        return 1


class TestMPSNeuralNetwork_MPSNeuralNetworkTypes(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNBatchNormalizationFlags)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsDefault, 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsCalculateStatisticsAutomatic,
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsDefault,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsCalculateStatisticsAlways,
            1,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsCalculateStatisticsNever,
            2,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBatchNormalizationFlagsCalculateStatisticsMask,
            3,
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNBinaryConvolutionFlags)
        self.assertEqual(MetalPerformanceShaders.MPSCNNBinaryConvolutionFlagsNone, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionFlagsUseBetaScaling, 1 << 0
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNBinaryConvolutionType)
        self.assertEqual(
            MetalPerformanceShaders.MPSCNNBinaryConvolutionTypeBinaryWeights, 0
        )
        self.assertEqual(MetalPerformanceShaders.MPSCNNBinaryConvolutionTypeXNOR, 1)
        self.assertEqual(MetalPerformanceShaders.MPSCNNBinaryConvolutionTypeAND, 2)

        self.assertIsEnumType(MetalPerformanceShaders.MPSCNNConvolutionFlags)
        self.assertEqual(MetalPerformanceShaders.MPSCNNConvolutionFlagsNone, 0)

        self.assertIsEnumType(
            MetalPerformanceShaders.MPSNNConvolutionAccumulatorPrecisionOption
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNConvolutionAccumulatorPrecisionOptionHalf, 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNConvolutionAccumulatorPrecisionOptionFloat,
            1 << 0,
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSNNPaddingMethod)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodAlignCentered, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodAlignTopLeft, 1)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodAlignBottomRight, 2)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodAlign_reserved, 3)
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAlignMask,
            MetalPerformanceShaders.MPSNNPaddingMethodAlign_reserved,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToTopLeft, 0 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToTopRight, 1 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToBottomLeft, 2 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToBottomRight, 3 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToMask,
            MetalPerformanceShaders.MPSNNPaddingMethodAddRemainderToBottomRight,
        )
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodSizeValidOnly, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodSizeSame, 1 << 4)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodSizeFull, 2 << 4)
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodSize_reserved, 3 << 4
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodCustomWhitelistForNodeFusion,
            1 << 13,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodCustomAllowForNodeFusion,
            1 << 13,
        )
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodCustom, 1 << 14)
        self.assertEqual(MetalPerformanceShaders.MPSNNPaddingMethodSizeMask, 0x7F0)
        self.assertEqual(
            MetalPerformanceShaders.MPSNNPaddingMethodExcludeEdges, 1 << 15
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSNNTrainingStyle)
        self.assertEqual(MetalPerformanceShaders.MPSNNTrainingStyleUpdateDeviceNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNNTrainingStyleUpdateDeviceCPU, 1)
        self.assertEqual(MetalPerformanceShaders.MPSNNTrainingStyleUpdateDeviceGPU, 2)

    def test_protocols(self):
        self.assertProtocolExists("MPSNNPadding", MetalPerformanceShaders)
        self.assertProtocolExists("MPSImageSizeEncodingState", MetalPerformanceShaders)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNeuralNetworkTypesHelper.paddingMethod,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNeuralNetworkTypesHelper.sourceWidth,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNeuralNetworkTypesHelper.sourceHeight,
            objc._C_NSUInteger,
        )
