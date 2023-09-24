from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders

MPSAccelerationStructureCompletionHandler = b"v@"


class TestMPSRayIntersector_MPSAccelerationStructure(TestCase):
    def test_structs(self):
        self.assertEqual(
            MetalPerformanceShaders.MPSAxisAlignedBoundingBox.__typestr__,
            b"{_MPSAxisAlignedBoundingBox=<3f><3f>}",
        )
        v = MetalPerformanceShaders.MPSAxisAlignedBoundingBox()
        self.assertIs(v.min, None)
        self.assertIs(v.max, None)

        self.assertEqual(
            MetalPerformanceShaders.MPSRayOriginDirection.__typestr__,
            b"{MPSRayOriginDirection=<3f><3f>}",
        )
        v = MetalPerformanceShaders.MPSRayOriginDirection()
        self.assertIs(v.origin, None)
        self.assertIs(v.direction, None)

        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexCoordinates.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexCoordinates=fI<2f>}",
        )
        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexCoordinates()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIs(v.coordinates, None)

        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates=fII<2f>}",
        )
        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates()
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertIs(v.coordinates, None)

        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates=fII<2f>}",
        )
        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates()
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertIs(v.coordinates, None)

        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates=fIII<2f>}",
        )
        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates()
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertIs(v.coordinates, None)

    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSAccelerationStructureStatus)
        self.assertIsEnumType(MetalPerformanceShaders.MPSAccelerationStructureUsage)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureUsageNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureUsageRefit, 1)
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsageFrequentRebuild, 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsagePreferGPUBuild, 4
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsagePreferCPUBuild, 8
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureStatusUnbuilt, 0
        )
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureStatusBuilt, 1)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSAccelerationStructure.rebuildWithCompletionHandler_,
            0,
            MPSAccelerationStructureCompletionHandler,
        )

        self.assertResultHasType(
            MetalPerformanceShaders.MPSAccelerationStructure.boundingBox,
            MetalPerformanceShaders.MPSAxisAlignedBoundingBox.__typestr__,
        )
