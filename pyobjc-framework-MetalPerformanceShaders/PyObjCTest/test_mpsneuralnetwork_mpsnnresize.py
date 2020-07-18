from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNResize(TestCase):
    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNResizeBilinear.alignCorners
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNResizeBilinear.initWithDevice_resizeWidth_resizeHeight_alignCorners_,
            3,
        )
