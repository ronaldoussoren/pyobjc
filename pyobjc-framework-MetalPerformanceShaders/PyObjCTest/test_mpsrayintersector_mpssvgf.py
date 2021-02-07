from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSSVGF(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSTemporalWeightingAverage, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSTemporalWeightingExponentialMovingAverage, 1
        )
