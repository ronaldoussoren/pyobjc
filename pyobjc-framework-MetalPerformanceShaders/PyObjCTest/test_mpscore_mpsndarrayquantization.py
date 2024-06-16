from PyObjCTools.TestSupport import TestCase, min_os_level
import MetalPerformanceShaders


class TestMPSCore_MPSNDArrayQuantization(TestCase):
    def test_enum(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSNDArrayQuantizationScheme)
        self.assertEqual(MetalPerformanceShaders.MPSNDArrayQuantizationTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSNDArrayQuantizationTypeAffine, 1)
        self.assertEqual(MetalPerformanceShaders.MPSNDArrayQuantizationTypeLUT, 2)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.hasZeroPoint
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.setHasZeroPoint_,
            0,
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.hasMinValue
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.setHasMinValue_,
            0,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.initWithDataType_hasZeroPoint_hasMinValue_,
            1,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayAffineQuantizationDescriptor.initWithDataType_hasZeroPoint_hasMinValue_,
            2,
        )
