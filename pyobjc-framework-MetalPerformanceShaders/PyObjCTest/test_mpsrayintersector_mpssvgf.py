from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSSVGF(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSTemporalWeighting)
        self.assertEqual(MetalPerformanceShaders.MPSTemporalWeightingAverage, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSTemporalWeightingExponentialMovingAverage, 1
        )
