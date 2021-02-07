from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNUpsampling(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSCNNUpsampling.alignCorners)

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSCNNUpsamplingBilinear.initWithDevice_integerScaleFactorX_integerScaleFactorY_alignCorners_,
            3,
        )
