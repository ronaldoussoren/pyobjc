from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphPoolingOps(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.ceilMode
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setCeilMode_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.includeZeroPadToAverage
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setIncludeZeroPadToAverage_,
            0,
        )
