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

        v = Metal.MTLPackedFloatQuaternion()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)
        self.assertIsInstance(v.w, float)

        v = Metal.MTLPackedFloat4x3()
        self.assertHasAttr(v, "columns")

        v = Metal.MTLAccelerationStructureInstanceDescriptor()
        self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.accelerationStructureIndex, int)

        v = Metal.MTLComponentTransform()
        self.assertIsInstance(v.scale, Metal.MTLPackedFloat3)
        self.assertIsInstance(v.shear, Metal.MTLPackedFloat3)
        self.assertIsInstance(v.pivot, Metal.MTLPackedFloat3)
        self.assertIsInstance(v.rotation, Metal.MTLPackedFloatQuaternion)
        self.assertIsInstance(v.translation, Metal.MTLPackedFloat3)

    @min_os_level("12.0")
    def test_functions(self):
        v = Metal.MTLPackedFloat3Make(1, 2, 3)
        self.assertIsInstance(v, Metal.MTLPackedFloat3)
        self.assertEqual(v, [(1.0, 2.0, 3.0)])

    @min_os_level("15.0")
    def test_functions15_0(self):
        v = Metal.MTLPackedFloatQuaternionMake(1, 2, 3, 4)
        self.assertIsInstance(v, Metal.MTLPackedFloatQuaternion)
        self.assertEqual(v.x, 1.0)
        self.assertEqual(v.y, 2.0)
        self.assertEqual(v.z, 3.0)
        self.assertEqual(v.w, 4.0)
