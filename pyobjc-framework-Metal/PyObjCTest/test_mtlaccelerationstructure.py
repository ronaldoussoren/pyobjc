import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLAccelerationStructure(TestCase):
    def test_constants(self):

        self.assertEqual(Metal.MTLAccelerationStructureUsageNone, 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsageRefit, 1 << 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsagePreferFastBuild, 1 << 1)

        self.assertEqual(Metal.MTLAccelerationStructureGeometryFlagNone, 0)
        self.assertEqual(Metal.MTLAccelerationStructureGeometryFlagOpaque, 1 << 0)
        self.assertEqual(
            Metal.MTLAccelerationStructureGeometryFlagNoDuplicateIntersectionFunctionInvocation,
            1 << 1,
        )

        self.assertEqual(Metal.MTLAccelerationStructureInstanceFlagNone, 0)
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceFlagDisableTriangleCulling, 1 << 0
        )
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceFlagTriangleFrontFacingWindingCounterClockwise,
            1 << 1,
        )
        self.assertEqual(Metal.MTLAccelerationStructureInstanceFlagOpaque, 1 << 2)
        self.assertEqual(Metal.MTLAccelerationStructureInstanceFlagNonOpaque, 1 << 3)
