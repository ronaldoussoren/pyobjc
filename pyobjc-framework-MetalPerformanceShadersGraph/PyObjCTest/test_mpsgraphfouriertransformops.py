from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphFourierTransformOps(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphFFTScalingMode)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphFFTScalingModeNone, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphFFTScalingModeSize, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphFFTScalingModeUnitary, 2)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphFFTDescriptor.inverse
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphFFTDescriptor.setInverse_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphFFTDescriptor.roundToOddHermitean
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphFFTDescriptor.setRoundToOddHermitean_,
            0,
        )
