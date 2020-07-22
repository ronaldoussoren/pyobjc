from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageConvolution(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageConvolution.initWithDevice_kernelWidth_kernelHeight_weights_,
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImageConvolution.initWithDevice_kernelWidth_kernelHeight_weights_,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImagePyramid.initWithDevice_kernelWidth_kernelHeight_weights_,
            3,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImagePyramid.initWithDevice_kernelWidth_kernelHeight_weights_,
            3,
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageCanny.initWithDevice_linearToGrayScaleTransform_sigma_,
            1,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageCanny.initWithDevice_linearToGrayScaleTransform_sigma_,
            1,
            3,
        )

        self.assertResultIsFixedSize(
            MetalPerformanceShaders.MPSImageCanny.colorTransform, 3
        )

        self.assertResultIsBOOL(MetalPerformanceShaders.MPSImageCanny.useFastMode)
        self.assertArgIsBOOL(MetalPerformanceShaders.MPSImageCanny.setUseFastMode_, 0)
