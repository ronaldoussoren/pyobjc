from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNDArray_MPSNDArrayKernel(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSNDArrayMultiaryBase.copyWithZone_device_
        )
