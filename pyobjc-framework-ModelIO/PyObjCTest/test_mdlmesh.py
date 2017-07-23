from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLMesh (TestCase):
        def testMethods(self):
            # XXX: Test failure due to ObjC not having a type code for
            # SIMD types.

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newBoxWithDimensions_segments_geometryType_inwardNormals_allocator_, 3)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newEllipsoidWithRadii_radialSegments_verticalSegments_geometryType_inwardNormals_hemisphere_allocator_, 4)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newCylinderWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_, 5)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newEllipticalConeWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_, 5)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newIcosahedronWithRadius_inwardNormals_allocator_, 1)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateAmbientOcclusionTextureWithSize_raysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateAmbientOcclusionTextureWithSize_raysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateAmbientOcclusionVertexColorsWithRaysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateAmbientOcclusionVertexColorsWithRaysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateLightMapTextureWithTextureSize_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_)

            #self.assertResultIsBOOL(ModelIO.MDLMesh.generateLightMapTextureWithQuality_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_)

            self.assertResultIsBOOL(ModelIO.MDLMesh.generateLightMapVertexColorsWithLightsToConsider_objectsToConsider_vertexAttributeNamed_)

        @min_os_level('10.12')
        def  testMethods10_12(self):
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initBoxWithExtent_segments_inwardNormals_geometryType_allocator_, 2)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initSphereWithExtent_segments_inwardNormals_geometryType_allocator_, 2)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initHemisphereWithExtent_segments_inwardNormals_cap_geometryType_allocator_, 2)
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initHemisphereWithExtent_segments_inwardNormals_cap_geometryType_allocator_, 3)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_, 2)
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_, 3)
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_, 4)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initCapsuleWithExtent_cylinderSegments_hemisphereSegments_inwardNormals_geometryType_allocator_, 3)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_, 2)
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_, 3)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.initIcosahedronWithExtent_inwardNormals_geometryType_allocator_, 1)

            #self.assertArgIsBOOL(ModelIO.MDLMesh.newCapsuleWithHeight_radii_radialSegments_verticalSegments_hemisphereSegments_geometryType_inwardNormals_allocator_, 5)

            pass

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsOut(ModelIO.MDLMesh.makeVerticesUniqueAndReturnError_, 0)

            # Vectors..
            #self.assertArgIsBOOL(ModelIO.MDLMesh.initMeshWithPrimitive_segments_inwardNormals_geometryType_allocator_, 2)
            #self.assertArgIsBOOL(ModelIO.MDLMesh.newMeshWithPrimitive_segments_inwardNormals_geometryType_allocator_, 2)

if __name__ == "__main__":
    main()
