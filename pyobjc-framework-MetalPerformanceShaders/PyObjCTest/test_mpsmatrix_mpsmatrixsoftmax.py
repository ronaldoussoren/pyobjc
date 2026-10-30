from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixSoftMax(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixSoftMax.copyWithZone_device_
        )
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixSoftMaxGradient.copyWithZone_device_
        )
