from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSInstanceAccelerationStructure(TestCase):
    def test_structs(self):
        # XXX: Union
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSPackedFloat3")

        # XXX: Vector
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSAxisAlignedBoundingBox")
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSRayOriginDirection")
        self.assertNotHasAttr(MetalPerformanceShaders, "MPSRayPackedOriginDirection")

        # XXX: Union
        self.assertNotHasAttr(
            MetalPerformanceShaders, "MPSRayOriginMinDistanceDirectionMaxDistance"
        )
        self.assertNotHasAttr(
            MetalPerformanceShaders, "MPSRayOriginMaskDirectionMaxDistance"
        )

        v = MetalPerformanceShaders.MPSIntersectionDistance()
        self.assertIsInstance(v.distance, float)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertPickleRoundTrips(v)

        # XXX: Vector
        self.assertNotHasAttr(
            MetalPerformanceShaders, "MPSIntersectionDistancePrimitiveIndexCoordinates"
        )

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexInstanceIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertPickleRoundTrips(v)

        # XXX: Vector
        self.assertNotHasAttr(
            MetalPerformanceShaders,
            "MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates",
        )

        v = MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndex()
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.bufferIndex, int)
        self.assertPickleRoundTrips(v)

        # XXX: Vector
        self.assertNotHasAttr(
            MetalPerformanceShaders,
            "MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates",
        )

        v = (
            MetalPerformanceShaders.MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex()
        )
        self.assertIsInstance(v.distance, float)
        self.assertIsInstance(v.primitiveIndex, int)
        self.assertIsInstance(v.instanceIndex, int)
        self.assertPickleRoundTrips(v)

        # XXX: Vector
        self.assertNotHasAttr(
            MetalPerformanceShaders,
            "MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates",
        )
