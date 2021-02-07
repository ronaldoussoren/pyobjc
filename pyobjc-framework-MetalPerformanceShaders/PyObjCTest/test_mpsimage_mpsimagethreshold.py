from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageThreshold(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageThresholdBinary.initWithDevice_thresholdValue_maximumValue_linearGrayColorTransform_,
            3,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageThresholdBinary.initWithDevice_thresholdValue_maximumValue_linearGrayColorTransform_,
            3,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageThresholdBinaryInverse.initWithDevice_thresholdValue_maximumValue_linearGrayColorTransform_,  # noqa: B950
            3,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageThresholdBinaryInverse.initWithDevice_thresholdValue_maximumValue_linearGrayColorTransform_,  # noqa: B950
            3,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageThresholdTruncate.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageThresholdTruncate.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageThresholdToZero.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageThresholdToZero.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
            3,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageThresholdToZeroInverse.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
        )
        self.assertArgIsFixedSize(
            MetalPerformanceShaders.MPSImageThresholdToZeroInverse.initWithDevice_thresholdValue_linearGrayColorTransform_,
            2,
            3,
        )
