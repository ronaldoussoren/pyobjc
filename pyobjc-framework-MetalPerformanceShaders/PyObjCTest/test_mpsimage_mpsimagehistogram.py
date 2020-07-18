from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageHistogram(TestCase):
    def test_structs(self):
        # Vector types:
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSImageHistogramInfo")
        # v = MetalPerformanceShaders.MPSImageHistogramInfo()
        # self.assertIsInstance(v.numberOfHistogramEntries, int)
        # self.assertIsInstance(v.histogramForAlpha, bool)
        # self.assertIsInstance(v.minPixelValue, objc.vector_float4)
        # self.assertIsInstance(v.maxPixelValue, objc.vector_float4)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSImageHistogram.zeroHistogram)
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSImageHistogram.setZeroHistogram_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogram.initWithDevice_histogramInfo_, 1
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSImageNormalizedHistogram.zeroHistogram
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSImageNormalizedHistogram.setZeroHistogram_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageNormalizedHistogram.initWithDevice_histogramInfo_,
            1,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramEqualization.initWithDevice_histogramInfo_,
            1,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramSpecification.initWithDevice_histogramInfo_,
            1,
        )
