from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSSVGF(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSTemporalWeighting)
        self.assertEqual(MetalPerformanceShaders.MPSTemporalWeightingAverage, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSTemporalWeightingExponentialMovingAverage, 1
        )

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSSVGF.copyWithZone_device_
        )
