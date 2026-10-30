from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixRandom(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSMatrixRandomDistribution)
        self.assertEqual(MetalPerformanceShaders.MPSMatrixRandomDistributionDefault, 1)
        self.assertEqual(MetalPerformanceShaders.MPSMatrixRandomDistributionUniform, 2)
        self.assertEqual(MetalPerformanceShaders.MPSMatrixRandomDistributionNormal, 3)
