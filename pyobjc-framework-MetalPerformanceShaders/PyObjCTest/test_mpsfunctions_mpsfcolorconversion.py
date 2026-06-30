from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import math
import MetalPerformanceShaders


class TestMPSFunctions_MPSFColorConversion(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSFColorConversionOptions)
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionSnorm8, 7
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionUnorm8, 8
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionSnorm16, 15
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionUnorm16, 16
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionFloat16, 11
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFConverisonOptionsPrecisionFloat32, 24
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFColorConversionOptionsPrecisionMask, 0x3F
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFColorConversionOptionsReturnGrayscaleAsRGB,
            0x100,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFColorConversionOptionsVerboseLogging, 0x200
        )

        self.assertIsInstance(
            MetalPerformanceShaders.MPSFunctions_AABB_Unbounded,
            MetalPerformanceShaders.MPSFunctions_AABB,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFunctions_AABB_Unbounded,
            (objc.simd.vector_float4(math.inf), objc.simd.vector_float4(-math.inf)),
        )

        self.assertIsInstance(
            MetalPerformanceShaders.MPSFunctions_AABB_SDR,
            MetalPerformanceShaders.MPSFunctions_AABB,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFunctions_AABB_SDR,
            (objc.simd.vector_float4(1), objc.simd.vector_float4(0)),
        )

    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsOut(
            MetalPerformanceShaders.MPSFColorConversion.initWithDevice_startColorSpace_endColorSpace_functionName_sourceRange_options_error_,
            6,
        )
        self.assertArgIsOut(
            MetalPerformanceShaders.MPSFColorConversion.initWithDevice_conversion_functionName_sourceRange_options_error_,
            5,
        )
