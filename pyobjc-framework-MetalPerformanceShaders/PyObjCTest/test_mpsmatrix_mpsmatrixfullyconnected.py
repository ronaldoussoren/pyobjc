from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixFullyConnected(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixFullyConnected.copyWithZone_device_
        )
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixFullyConnectedGradient.copyWithZone_device_
        )
