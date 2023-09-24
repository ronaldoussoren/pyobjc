from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSInstanceAccelerationStructure(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSPackedFloat3()
        self.assertEqual(v.__typestr__, b"{_MPSPackedFloat3=fff}")
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)

        v = MetalPerformanceShaders.MPSAxisAlignedBoundingBox()
        self.assertEqual(v.__typestr__, b"{_MPSAxisAlignedBoundingBox=<3f><3f>}")
        self.assertEqual(v.max, None)
        self.assertEqual(v.min, None)

        v = MetalPerformanceShaders.MPSRayOriginMinDistanceDirectionMaxDistance()
        self.assertEqual(
            v.__typestr__,
            b"{MPSRayOriginMinDistanceDirectionMaxDistance={_MPSPackedFloat3=fff}f{_MPSPackedFloat3=fff}f}",
        )
        self.assertEqual(v.origin, MetalPerformanceShaders.MPSPackedFloat3())
        self.assertEqual(v.minDistance, 0.0)
        self.assertEqual(v.direction, MetalPerformanceShaders.MPSPackedFloat3())
        self.assertEqual(v.maxDistance, 0.0)

        v = MetalPerformanceShaders.MPSRayOriginMaskDirectionMaxDistance()
        self.assertEqual(
            v.__typestr__,
            b"{MPSRayOriginMaskDirectionMaxDistance={_MPSPackedFloat3=fff}I{_MPSPackedFloat3=fff}f}",
        )
        self.assertEqual(v.direction, MetalPerformanceShaders.MPSPackedFloat3())
        self.assertEqual(v.mask, 0)
        self.assertEqual(v.maxDistance, 0.0)
        self.assertEqual(v.origin, MetalPerformanceShaders.MPSPackedFloat3())

        v = MetalPerformanceShaders.MPSRayPackedOriginDirection()
        self.assertEqual(
            v.__typestr__,
            b"{MPSRayPackedOriginDirection={_MPSPackedFloat3=fff}{_MPSPackedFloat3=fff}}",
        )
        self.assertEqual(v.direction, MetalPerformanceShaders.MPSPackedFloat3())
        self.assertEqual(v.origin, MetalPerformanceShaders.MPSPackedFloat3())

        v = MetalPerformanceShaders.MPSIntersectionDistance()
        self.assertIsInstance(v.distance, float)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexCoordinates()
        self.assertEqual(
            v.__typestr__, b"{MPSIntersectionDistancePrimitiveIndexCoordinates=fI<2f>}"
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIs(v.coordinates, None)

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexInstanceIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertPickleRoundTrips(v)

        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates()
        )
        self.assertEqual(
            v.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates=fII<2f>}",
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertIs(v.coordinates, None)

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertPickleRoundTrips(v)

        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates()
        )
        self.assertEqual(
            v.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates=fII<2f>}",
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertIs(v.coordinates, None)

        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex()
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertPickleRoundTrips(v)

        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates()
        )
        self.assertEqual(
            v.__typestr__,
            b"{MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates=fIII<2f>}",
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertIs(v.coordinates, None)
