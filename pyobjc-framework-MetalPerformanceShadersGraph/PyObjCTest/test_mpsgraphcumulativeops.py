from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphCumulativeOps(TestCase):
    @min_os_level("13.0")
    def test_methods11_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeSumWithTensor_axis_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeSumWithTensor_axis_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeSumWithTensor_axisTensor_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeSumWithTensor_axisTensor_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeProductWithTensor_axis_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeProductWithTensor_axis_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeProductWithTensor_axisTensor_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeProductWithTensor_axisTensor_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMinimumWithTensor_axis_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMinimumWithTensor_axis_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMinimumWithTensor_axisTensor_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMinimumWithTensor_axisTensor_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMaximumWithTensor_axis_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMaximumWithTensor_axis_exclusive_reverse_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMaximumWithTensor_axisTensor_exclusive_reverse_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.cumulativeMaximumWithTensor_axisTensor_exclusive_reverse_name_,
            3,
        )
