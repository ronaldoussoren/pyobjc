from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphMatrixMultiplicationOps(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSDPADescriptor.isCausal
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSDPADescriptor.setIsCausal_, 0
        )
