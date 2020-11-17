import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTLAccelerationStructure(TestCase):
    def test_structs(self):
        # Vector types in fields
        self.assertFalse(hasattr(Metal, 'MTLAccelerationStructureInstanceDescriptor'))

        #v = Metal.MTLAccelerationStructureInstanceDescriptor()
        #self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        #self.assertIsInstance(v.options, int)
        #self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        #self.assertIsInstance(v.accelerationStructureIndex, int)

    def test_constants(self):

        self.assertEqual(Metal.MTLAccelerationStructureUsageNone, 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsageRefit, 1 << 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsagePreferFastBuild, 1 << 1)

        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionNone, 0)
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceOptionDisableTriangleCulling, 1 << 0
        )
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceOptionTriangleFrontFacingWindingCounterClockwise,
            1 << 1,
        )

        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionOpaque, 1 << 2)
        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionNonOpaque, 1 << 3)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(Metal.MTLAccelerationStructureGeometryDescriptor.opaque)
        self.assertArgIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.setOpaque_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.allowDuplicateIntersectionFunctionInvocation
        )
        self.assertArgIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.setAllowDuplicateIntersectionFunctionInvocation_,
            0
        )
