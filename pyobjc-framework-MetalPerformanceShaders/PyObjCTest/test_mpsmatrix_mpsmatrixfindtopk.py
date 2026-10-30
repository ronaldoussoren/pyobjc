from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixFindTopK(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixFindTopK.copyWithZone_device_
        )
