import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLAccelerationStructureTypes(TestCase):
    def test_structs(self):
        self.assertNotHasAttr(Metal, "MTLPackedFloat3")
        self.assertNotHasAttr(Metal, "MTLPackedFloat4x3")
        self.assertNotHasAttr(Metal, "MTLAccelerationStructureInstanceDescriptor")

        # v = Metal.MTLPackedFloat3()
        # self.assertIsInstance(v.x, float)
        # self.assertIsInstance(v.y, float)
        # self.assertIsInstance(v.z, float)
        # self.asssertNotHasattr(v, "elements")

        # v = Metal.MTLPackedFloat4x3()
        # self.assertHasattr(v, "columns")

        # v = Metal.MTLAccelerationStructureInstanceDescriptor()
        # self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        # self.assertIsInstance(v.flags, int)
        # self.assertIsInstance(v.mask, int)
        # self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        # self.assertIsInstance(v.accelerationStructureIndex, int)
