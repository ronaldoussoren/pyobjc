from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageMorphology(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageDilate.initWithDevice_kernelWidth_kernelHeight_values_,
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImageDilate.initWithDevice_kernelWidth_kernelHeight_values_,
            3,
        )
