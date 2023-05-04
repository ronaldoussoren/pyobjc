import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTLAccelerationStructureTypes(TestCase):
    def test_structs(self):
        v = Metal.MTLPackedFloat3()
        self.assertEqual(v.elements, None)

        v = Metal.MTLPackedFloat3([1, 2, 3])
        self.assertEqual(v.elements, [1, 2, 3])
        # self.assertEqual(v.x, 1)
        # self.assertEqual(v.y, 2)
        # self.assertEqual(v.z, 3)

        v = Metal.MTLPackedFloat4x3()
        self.assertHasAttr(v, "columns")

        v = Metal.MTLAccelerationStructureInstanceDescriptor()
        self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.accelerationStructureIndex, int)

    @min_os_level("12.0")
    def test_functions(self):
        v = Metal.MTLPackedFloat3Make(1, 2, 3)
        self.assertIsInstance(v, Metal.MTLPackedFloat3)
        self.assertEqual(v, [(1.0, 2.0, 3.0)])
