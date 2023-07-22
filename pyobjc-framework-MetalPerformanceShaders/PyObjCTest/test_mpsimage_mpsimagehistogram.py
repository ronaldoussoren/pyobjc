from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders
from objc import simd


class TestMPSImage_MPSImageHistogram(TestCase):
    def test_structs(self):
        # Vector types:
        self.assertEqual(
            MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
            b"{MPSImageHistogramInfo=QZ<4f><4f>}",
        )
        v = MetalPerformanceShaders.MPSImageHistogramInfo()
        self.assertIsInstance(v.numberOfHistogramEntries, int)
        self.assertIsInstance(v.histogramForAlpha, bool)
        self.assertIs(v.minPixelValue, None)
        self.assertIs(v.maxPixelValue, None)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSImageHistogram.zeroHistogram)
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSImageHistogram.setZeroHistogram_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogram.initWithDevice_histogramInfo_, 1
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSImageHistogram.initWithDevice_histogramInfo_,
            1,
            b"n^" + MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )

        self.assertResultHasType(
            MetalPerformanceShaders.MPSImageHistogram.histogramInfo,
            MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )

        self.assertResultHasType(
            MetalPerformanceShaders.MPSImageHistogram.minPixelThresholdValue,
            simd.vector_float4.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSImageHistogram.setMinPixelThresholdValue_,
            0,
            simd.vector_float4.__typestr__,
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultHasType(
            MetalPerformanceShaders.MPSImageNormalizedHistogram.histogramInfo,
            MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )
        self.assertResultHasType(
            MetalPerformanceShaders.MPSImageHistogramEqualization.histogramInfo,
            MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )
        self.assertResultHasType(
            MetalPerformanceShaders.MPSImageHistogramSpecification.histogramInfo,
            MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
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
        self.assertArgHasType(
            MetalPerformanceShaders.MPSImageNormalizedHistogram.initWithDevice_histogramInfo_,
            1,
            b"n^" + MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramEqualization.initWithDevice_histogramInfo_,
            1,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramEqualization.initWithDevice_histogramInfo_,
            1,
            b"n^" + MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramSpecification.initWithDevice_histogramInfo_,
            1,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageHistogramSpecification.initWithDevice_histogramInfo_,
            1,
            b"n^" + MetalPerformanceShaders.MPSImageHistogramInfo.__typestr__,
        )
