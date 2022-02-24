from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNMath(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSNNComparisonType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeEqual, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeNotEqual, 1)
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeLess, 2)
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeLessOrEqual, 3)
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeGreater, 4)
        self.assertEqual(MetalPerformanceShaders.MPSNNComparisonTypeGreaterOrEqual, 5)

    @min_os_level("10.13.4")
    def test_methods10_13_4(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSCNNArithmeticGradient.isSecondarySourceFilter
        )
        # self.assertArgIsBOOL(
        # MetalPerformanceShaders.MPSCNNArithmeticGradient.initWithDevice_isSecondarySourceFilter_,
        # 1,
        # )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNAddGradient.initWithDevice_isSecondarySourceFilter_,
            1,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNSubtractGradient.initWithDevice_isSecondarySourceFilter_,
            1,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNMultiplyGradient.initWithDevice_isSecondarySourceFilter_,
            1,
        )
