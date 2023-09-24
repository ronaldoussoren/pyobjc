from PyObjCTools.TestSupport import TestCase
import ModelIO
from objc import simd


class TestMDLCamera(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLCameraProjection)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLCameraProjectionPerspective, 0)
        self.assertEqual(ModelIO.MDLCameraProjectionOrthographic, 1)

    def testMethods(self):
        self.assertResultHasType(
            ModelIO.MDLCamera.projectionMatrix, simd.simd_float4x4.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLCamera.frameBoundingBox_setNearAndFar_,
            0,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertArgIsBOOL(ModelIO.MDLCamera.frameBoundingBox_setNearAndFar_, 1)

        self.assertArgHasType(
            ModelIO.MDLCamera.lookAt_, 0, simd.vector_float3.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLCamera.lookAt_from_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.lookAt_from_, 1, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.rayTo_forViewPort_, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.rayTo_forViewPort_, 0, simd.vector_int2.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.rayTo_forViewPort_, 1, simd.vector_int2.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLCamera.bokehKernelWithSize_, 0, simd.vector_int2.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.sensorEnlargement, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.setSensorEnlargement_, 0, simd.vector_float2.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.sensorShift, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.setSensorShift_, 0, simd.vector_float2.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.flash, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.setFlash_, 0, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.exposureCompression, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.setExposureCompression_, 0, simd.vector_float2.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLCamera.exposure, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLCamera.setExposure_, 0, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLStereoscopicCamera.leftViewMatrix,
            simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLStereoscopicCamera.rightViewMatrix,
            simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLStereoscopicCamera.leftProjectionMatrix,
            simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLStereoscopicCamera.rightProjectionMatrix,
            simd.simd_float4x4.__typestr__,
        )
