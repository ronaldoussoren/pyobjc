from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import MetalPerformanceShaders


class TestMPSCore_MPSCoreTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSAliasingStrategy)
        self.assertIsEnumType(MetalPerformanceShaders.MPSDataType)
        self.assertIsEnumType(MetalPerformanceShaders.MPSImageEdgeMode)
        self.assertIsEnumType(MetalPerformanceShaders.MPSImageFeatureChannelFormat)
        self.assertIsEnumType(MetalPerformanceShaders.MPSKernelOptions)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSKernelOptionsNone, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSKernelOptionsSkipAPIValidation, 1 << 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSKernelOptionsAllowReducedPrecision, 1 << 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSKernelOptionsDisableInternalTiling, 1 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSKernelOptionsInsertDebugGroups, 1 << 3
        )
        self.assertEqual(MetalPerformanceShaders.MPSKernelOptionsVerbose, 1 << 4)

        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeZero, 0)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeClamp, 1)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeMirror, 2)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeMirrorWithEdge, 3)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeConstant, 4)

        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatUnorm8, 1)
        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatUnorm16, 2)
        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatFloat16, 3)
        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatFloat32, 4)
        self.assertEqual(
            MetalPerformanceShaders.MPSImageFeatureChannelFormat_reserved0, 5
        )
        self.assertEqual(MetalPerformanceShaders.MPSImageFeatureChannelFormatCount, 6)

        self.assertEqual(MetalPerformanceShaders.MPSDataTypeInvalid, 0)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeFloatBit, 0x10000000)
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeFloat32,
            MetalPerformanceShaders.MPSDataTypeFloatBit | 32,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeFloat16,
            MetalPerformanceShaders.MPSDataTypeFloatBit | 16,
        )

        self.assertEqual(MetalPerformanceShaders.MPSDataTypeComplexBit, 0x01000000)
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeComplexFloat32,
            MetalPerformanceShaders.MPSDataTypeFloatBit
            | MetalPerformanceShaders.MPSDataTypeComplexBit
            | 64,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeComplexFloat16,
            MetalPerformanceShaders.MPSDataTypeFloatBit
            | MetalPerformanceShaders.MPSDataTypeComplexBit
            | 32,
        )

        self.assertEqual(MetalPerformanceShaders.MPSDataTypeSignedBit, 0x20000000)
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeIntBit,
            MetalPerformanceShaders.MPSDataTypeSignedBit,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt2,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 2,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt4,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 4,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt8,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 8,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt16,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 16,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt32,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 32,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeInt64,
            MetalPerformanceShaders.MPSDataTypeSignedBit | 64,
        )
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt2, 2)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt4, 4)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt8, 8)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt16, 16)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt32, 32)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeUInt64, 64)
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeNormalizedBit, 0x40000000)
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeUnorm1,
            MetalPerformanceShaders.MPSDataTypeNormalizedBit | 1,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeUnorm8,
            MetalPerformanceShaders.MPSDataTypeNormalizedBit | 8,
        )

        self.assertEqual(MetalPerformanceShaders.MPSAliasingStrategyDefault, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSAliasingStrategyDontCare,
            MetalPerformanceShaders.MPSAliasingStrategyDefault,
        )
        self.assertEqual(MetalPerformanceShaders.MPSAliasingStrategyShallAlias, 1 << 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSAliasingStrategyShallNotAlias, 1 << 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAliasingStrategyAliasingReserved,
            MetalPerformanceShaders.MPSAliasingStrategyShallAlias
            | MetalPerformanceShaders.MPSAliasingStrategyShallNotAlias,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAliasingStrategyPreferTemporaryMemory, 1 << 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAliasingStrategyPreferNonTemporaryMemory, 1 << 3
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeAlternateEncodingBit, 0x80000000
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeBool,
            MetalPerformanceShaders.MPSDataTypeAlternateEncodingBit | 8,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeBFloat16,
            MetalPerformanceShaders.MPSDataTypeAlternateEncodingBit
            | MetalPerformanceShaders.MPSDataTypeFloat16,
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSFloatDataTypeBit)
        self.assertEqual(MetalPerformanceShaders.MPSFloatDataTypeSignBit, 0x00800000)
        self.assertEqual(
            MetalPerformanceShaders.MPSFloatDataTypeExponentBit, 0x007C0000
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFloatDataTypeMantissaBit, 0x0003FC00
        )

        self.assertIsEnumType(MetalPerformanceShaders.MPSFloatDataTypeShift)
        self.assertEqual(MetalPerformanceShaders.MPSFloatDataTypeSignShift, 23)
        self.assertEqual(MetalPerformanceShaders.MPSFloatDataTypeExponentShift, 18)
        self.assertEqual(MetalPerformanceShaders.MPSFloatDataTypeMantissaShift, 10)

    def test_structs(self):
        v = MetalPerformanceShaders.MPSOffset()
        self.assertIsInstance(v.x, int)
        self.assertIsInstance(v.y, int)
        self.assertIsInstance(v.z, int)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSOrigin()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSSize()
        self.assertIsInstance(v.width, float)
        self.assertIsInstance(v.height, float)
        self.assertIsInstance(v.depth, float)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSDimensionSlice()
        self.assertIsInstance(v.start, int)
        self.assertIsInstance(v.length, int)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSRegion()
        self.assertIsInstance(v.origin, MetalPerformanceShaders.MPSOrigin)
        self.assertIsInstance(v.size, MetalPerformanceShaders.MPSSize)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSScaleTransform()
        self.assertIsInstance(v.scaleX, float)
        self.assertIsInstance(v.scaleY, float)
        self.assertIsInstance(v.translateX, float)
        self.assertIsInstance(v.translateY, float)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSImageCoordinate()
        self.assertIsInstance(v.x, int)
        self.assertIsInstance(v.y, int)
        self.assertIsInstance(v.channel, int)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSImageRegion()
        self.assertIsInstance(v.offset, MetalPerformanceShaders.MPSImageCoordinate)
        self.assertIsInstance(v.size, MetalPerformanceShaders.MPSImageCoordinate)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertIsInstance(
            MetalPerformanceShaders.MPSRectNoClip, MetalPerformanceShaders.MTLRegion
        )

    @min_sdk_level("14.4")
    def test_functions14_4(self):
        MetalPerformanceShaders.MPSDataTypeBitsCount

    def test_protocols(self):
        self.assertProtocolExists("MPSDeviceProvider")
