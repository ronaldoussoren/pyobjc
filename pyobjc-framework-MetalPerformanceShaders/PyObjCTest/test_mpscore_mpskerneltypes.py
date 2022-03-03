from PyObjCTools.TestSupport import TestCase, min_sdk_level

import MetalPerformanceShaders


class TestMPSCore_MPSKernelTypes(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSDeviceCapsNull, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsReadableArrayOfTextures, 1 << 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsWritableArrayOfTextures, 1 << 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsReadWriteTextures, 1 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsSimdgroupBarrier, 1 << 3
        )
        self.assertEqual(MetalPerformanceShaders.MPSDeviceSupportsQuadShuffle, 1 << 4)
        self.assertEqual(MetalPerformanceShaders.MPSDeviceSupportsSimdShuffle, 1 << 5)
        self.assertEqual(MetalPerformanceShaders.MPSDeviceSupportsSimdReduction, 1 << 6)
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsFloat32Filtering, 1 << 7
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsNorm16BicubicFiltering, 1 << 8
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDeviceSupportsFloat16BicubicFiltering, 1 << 9
        )
        self.assertEqual(MetalPerformanceShaders.MPSDeviceIsAppleDevice, 1 << 10)

        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexDestIndex, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexSrc0Index, 0)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexSrc1Index, 1)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexSrc2Index, 2)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexSrc3Index, 3)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexSrc4Index, 4)
        self.assertEqual(MetalPerformanceShaders.MPSCustomKernelIndexUserDataIndex, 30)

        self.assertEqual(MetalPerformanceShaders.MPSImageType2d, 0)
        self.assertEqual(MetalPerformanceShaders.MPSImageType2d_array, 1)
        self.assertEqual(MetalPerformanceShaders.MPSImageTypeArray2d, 2)
        self.assertEqual(MetalPerformanceShaders.MPSImageTypeArray2d_array, 3)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_ArrayMask, 1)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_BatchMask, 2)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_typeMask, 3)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_noAlpha, 4)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_texelFormatMask, 0x38)
        self.assertEqual(MetalPerformanceShaders.MPSImageType_texelFormatShift, 3)
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType_texelFormatStandard,
            0 << MetalPerformanceShaders.MPSImageType_texelFormatShift,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType_texelFormatUnorm8,
            1 << MetalPerformanceShaders.MPSImageType_texelFormatShift,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType_texelFormatFloat16,
            2 << MetalPerformanceShaders.MPSImageType_texelFormatShift,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType_texelFormatBFloat16,
            3 << MetalPerformanceShaders.MPSImageType_texelFormatShift,
        )
        self.assertEqual(MetalPerformanceShaders.MPSImageType_bitCount, 6)
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType_mask,
            (1 << MetalPerformanceShaders.MPSImageType_bitCount) - 1,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType2d_noAlpha,
            MetalPerformanceShaders.MPSImageType2d
            | MetalPerformanceShaders.MPSImageType_noAlpha,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageType2d_array_noAlpha,
            MetalPerformanceShaders.MPSImageType2d_array
            | MetalPerformanceShaders.MPSImageType_noAlpha,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageTypeArray2d_noAlpha,
            MetalPerformanceShaders.MPSImageType2d
            | MetalPerformanceShaders.MPSImageType_BatchMask
            | MetalPerformanceShaders.MPSImageType_noAlpha,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSImageTypeArray2d_array_noAlpha,
            MetalPerformanceShaders.MPSImageType2d_array
            | MetalPerformanceShaders.MPSImageType_BatchMask
            | MetalPerformanceShaders.MPSImageType_noAlpha,
        )

        self.assertEqual(MetalPerformanceShaders.MPSFunctionConstantNone, -1)

    def test_structs(self):
        v = MetalPerformanceShaders.MPSMatrixOffset()
        self.assertIsInstance(v.rowOffset, int)
        self.assertIsInstance(v.columnOffset, int)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSIntegerDivisionParams()
        self.assertIsInstance(v.divisor, int)
        self.assertIsInstance(v.recip, int)
        self.assertIsInstance(v.addend, int)
        self.assertIsInstance(v.shift, int)
        self.assertPickleRoundTrips(v)

        # self.fail("MPSCustomKernelSourceInfo")  # Vector types
        # self.fail("MPSCustomKernelInfo")  # Vector types
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSCustomKernelSourceInfo")
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSCustomKernelInfo")

        v = MetalPerformanceShaders.MPSCustomKernelArgumentCount()
        self.assertIsInstance(v.destinationTextureCount, int)
        self.assertIsInstance(v.sourceTextureCount, int)
        self.assertIsInstance(v.broadcastTextureCount, int)
        self.assertPickleRoundTrips(v)

    @min_sdk_level("10.13.4")
    def test_inline_functions(self):
        MetalPerformanceShaders.MPSFindIntegerDivisionParams
        MetalPerformanceShaders.MPSGetCustomKernelMaxBatchSize
        MetalPerformanceShaders.MPSGetCustomKernelBatchedDestinationIndex
        MetalPerformanceShaders.MPSGetCustomKernelBatchedSourceIndex
        MetalPerformanceShaders.MPSGetCustomKernelBroadcastSourceIndex
