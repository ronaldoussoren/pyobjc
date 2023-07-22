from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import ModelIO
from objc import simd


class TestMDLTransformStackHelper(ModelIO.NSObject):
    def float4x4AtTime_(self, a):
        return 1

    def double4x4AtTime_(self, a):
        return 1


class TestMDLTransformStack(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLTransformOpRotationOrder)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderXYZ, 1)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderXZY, 2)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderYXZ, 3)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderYZX, 4)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderZXY, 5)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderZYX, 6)

    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("MDLTransformOp")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMDLTransformStackHelper.float4x4AtTime_,
            simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            TestMDLTransformStackHelper.double4x4AtTime_,
            simd.simd_double4x4.__typestr__,
        )

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultHasType(
            ModelIO.MDLTransformStack.float4x4AtTime_, simd.simd_float4x4.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransformStack.double4x4AtTime_,
            simd.simd_double4x4.__typestr__,
        )
