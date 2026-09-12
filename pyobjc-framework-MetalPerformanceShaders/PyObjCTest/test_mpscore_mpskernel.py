from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSCore_MPSKernel(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSKernel.copyWithZone_device_
        )
