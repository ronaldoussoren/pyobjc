from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MetalPerformanceShaders


class TestMPSCore_MPSCoreTypes(TestCase):
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
        self.assertEqual(MetalPerformanceShaders.MPSDataTypeSignedBit, 0x20000000)
        self.assertEqual(
            MetalPerformanceShaders.MPSDataTypeIntBit,
            MetalPerformanceShaders.MPSDataTypeSignedBit,
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

    def test_structs(self):
        v = MetalPerformanceShaders.MPSOffset()
        self.assertIsInstance(v.x, int)
        self.assertIsInstance(v.y, int)
        self.assertIsInstance(v.z, int)

        v = MetalPerformanceShaders.MPSOrigin()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)

        v = MetalPerformanceShaders.MPSSize()
        self.assertIsInstance(v.width, float)
        self.assertIsInstance(v.height, float)
        self.assertIsInstance(v.depth, float)

        v = MetalPerformanceShaders.MPSDimensionSlice()
        self.assertIsInstance(v.start, int)
        self.assertIsInstance(v.length, int)

        v = MetalPerformanceShaders.MPSRegion()
        self.assertIsInstance(v.origin, MetalPerformanceShaders.MPSOrigin)
        self.assertIsInstance(v.size, MetalPerformanceShaders.MPSSize)

        v = MetalPerformanceShaders.MPSScaleTransform()
        self.assertIsInstance(v.scaleX, float)
        self.assertIsInstance(v.scaleY, float)
        self.assertIsInstance(v.translateX, float)
        self.assertIsInstance(v.translateY, float)

        v = MetalPerformanceShaders.MPSImageCoordinate()
        self.assertIsInstance(v.x, int)
        self.assertIsInstance(v.y, int)
        self.assertIsInstance(v.channel, int)

        v = MetalPerformanceShaders.MPSImageRegion()
        self.assertIsInstance(v.offset, MetalPerformanceShaders.MPSImageCoordinate)
        self.assertIsInstance(v.size, MetalPerformanceShaders.MPSImageCoordinate)

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertIsInstance(
            MetalPerformanceShaders.MPSRectNoClip, MetalPerformanceShaders.MTLRegion
        )

    def test_protocols(self):
        objc.protocolNamed("MPSDeviceProvider")
