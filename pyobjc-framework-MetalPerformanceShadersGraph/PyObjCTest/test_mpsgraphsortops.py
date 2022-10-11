from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphSortOps(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sortWithTensor_axis_descending_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sortWithTensor_axisTensor_descending_name_,
            2,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.argSortWithTensor_axis_descending_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.argSortWithTensor_axisTensor_descending_name_,
            2,
        )
