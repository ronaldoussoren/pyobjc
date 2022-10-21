from PyObjCTools.TestSupport import TestCase, min_os_level
import ModelIO
from objc import simd


class TestMDLMesh(TestCase):
    def testMethods(self):
        self.assertArgHasType(
            ModelIO.MDLMesh.newBoxWithDimensions_segments_geometryType_inwardNormals_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.newBoxWithDimensions_segments_geometryType_inwardNormals_allocator_,
            1,
            simd.vector_uint3.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newBoxWithDimensions_segments_geometryType_inwardNormals_allocator_,
            3,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.newEllipsoidWithRadii_radialSegments_verticalSegments_geometryType_inwardNormals_hemisphere_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newEllipsoidWithRadii_radialSegments_verticalSegments_geometryType_inwardNormals_hemisphere_allocator_,
            4,
        )  # noqa: B950

        self.assertArgHasType(
            ModelIO.MDLMesh.newCylinderWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newCylinderWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_,
            5,
        )  # noqa: B950

        self.assertArgHasType(
            ModelIO.MDLMesh.newEllipticalConeWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newEllipticalConeWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_,
            5,
        )  # noqa: B950

        self.assertArgHasType(
            ModelIO.MDLMesh.newPlaneWithDimensions_segments_geometryType_allocator_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.newPlaneWithDimensions_segments_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )

        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newIcosahedronWithRadius_inwardNormals_allocator_, 1
        )

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateAmbientOcclusionTextureWithSize_raysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_
        )  # noqa: B950
        self.assertArgHasType(
            ModelIO.MDLMesh.generateAmbientOcclusionTextureWithSize_raysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_,
            0,
            simd.vector_int2.__typestr__,
        )  # noqa: B950

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateAmbientOcclusionVertexColorsWithRaysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_
        )  # noqa: B950

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateAmbientOcclusionVertexColorsWithRaysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_
        )  # noqa: B950

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateLightMapTextureWithTextureSize_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_
        )  # noqa: B950
        self.assertArgHasType(
            ModelIO.MDLMesh.generateLightMapTextureWithTextureSize_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_,
            0,
            simd.vector_int2.__typestr__,
        )  # noqa: B950

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateLightMapTextureWithQuality_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_
        )  # noqa: B950

        self.assertResultIsBOOL(
            ModelIO.MDLMesh.generateLightMapVertexColorsWithLightsToConsider_objectsToConsider_vertexAttributeNamed_
        )

        self.assertResultHasType(
            ModelIO.MDLMesh.boundingBox, ModelIO.MDLAxisAlignedBoundingBox.__typestr__
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgHasType(
            ModelIO.MDLMesh.initBoxWithExtent_segments_inwardNormals_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initBoxWithExtent_segments_inwardNormals_geometryType_allocator_,
            1,
            simd.vector_uint3.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initBoxWithExtent_segments_inwardNormals_geometryType_allocator_,
            2,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.initSphereWithExtent_segments_inwardNormals_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initSphereWithExtent_segments_inwardNormals_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initSphereWithExtent_segments_inwardNormals_geometryType_allocator_,
            2,
        )

        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initHemisphereWithExtent_segments_inwardNormals_cap_geometryType_allocator_,
            2,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initHemisphereWithExtent_segments_inwardNormals_cap_geometryType_allocator_,
            3,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_,
            2,
        )  # noqa: B950
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_,
            3,
        )  # noqa: B950
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_,
            4,
        )  # noqa: B950

        self.assertArgHasType(
            ModelIO.MDLMesh.initCapsuleWithExtent_cylinderSegments_hemisphereSegments_inwardNormals_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initCapsuleWithExtent_cylinderSegments_hemisphereSegments_inwardNormals_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initCapsuleWithExtent_cylinderSegments_hemisphereSegments_inwardNormals_geometryType_allocator_,
            3,
        )  # noqa: B950

        self.assertArgHasType(
            ModelIO.MDLMesh.initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_,
            3,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.initPlaneWithExtent_segments_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLMesh.initPlaneWithExtent_segments_geometryType_allocator_,
            1,
            simd.vector_uint2.__typestr__,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.initIcosahedronWithExtent_inwardNormals_geometryType_allocator_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.initIcosahedronWithExtent_inwardNormals_geometryType_allocator_,
            1,
        )

        self.assertArgHasType(
            ModelIO.MDLMesh.newCapsuleWithHeight_radii_radialSegments_verticalSegments_hemisphereSegments_geometryType_inwardNormals_allocator_,
            1,
            simd.vector_float2.__typestr__,
        )  # noqa: B950
        self.assertArgIsBOOL(
            ModelIO.MDLMesh.newCapsuleWithHeight_radii_radialSegments_verticalSegments_hemisphereSegments_geometryType_inwardNormals_allocator_,
            6,
        )  # noqa: B950

        pass

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(ModelIO.MDLMesh.makeVerticesUniqueAndReturnError_, 0)
