from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSTemporalAA(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSTemporalAA.copyWithZone_device_
        )
