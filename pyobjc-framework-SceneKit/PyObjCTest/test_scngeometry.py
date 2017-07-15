from PyObjCTools.TestSupport import *
import objc
import sys


if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:
    import SceneKit

    class TestSCNGeometry (TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeTriangles, 0)
            self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeTriangleStrip, 1)
            self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeLine, 2)
            self.assertEqual(SceneKit.SCNGeometryPrimitiveTypePoint, 3)
            self.assertEqual(SceneKit.SCNGeometryPrimitiveTypePolygon, 4)

            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticVertex, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticNormal, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticColor, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticTexcoord, unicode)

            self.assertEqual(SceneKit.SCNTessellationSmoothingModeNone, 0)
            self.assertEqual(SceneKit.SCNTessellationSmoothingModePNTriangles, 1)
            self.assertEqual(SceneKit.SCNTessellationSmoothingModePhong, 2)


        @min_os_level('10.10')
        def testConstants(self):
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticVertexCrease, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticEdgeCrease, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticBoneWeights, unicode)
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticBoneIndices, unicode)

        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticTangent, unicode)


        def testMethods(self):
            self.assertArgIsBOOL(SceneKit.SCNGeometrySource.geometrySourceWithData_semantic_vectorCount_floatComponents_componentsPerVector_bytesPerComponent_dataOffset_dataStride_, 3)

            self.assertArgIsIn(SceneKit.SCNGeometrySource.geometrySourceWithVertices_count_, 0)
            self.assertArgSizeInArg(SceneKit.SCNGeometrySource.geometrySourceWithVertices_count_, 0, 1)

            self.assertArgIsIn(SceneKit.SCNGeometrySource.geometrySourceWithNormals_count_, 0)
            self.assertArgSizeInArg(SceneKit.SCNGeometrySource.geometrySourceWithNormals_count_, 0, 1)

            self.assertArgIsIn(SceneKit.SCNGeometrySource.geometrySourceWithTextureCoordinates_count_, 0)
            self.assertArgSizeInArg(SceneKit.SCNGeometrySource.geometrySourceWithTextureCoordinates_count_, 0, 1)

            self.assertResultIsBOOL(SceneKit.SCNGeometrySource.floatComponents)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(SceneKit.SCNGeometry.wantsAdaptiveSubdivision)
            self.assertArgIsBOOL(SceneKit.SCNGeometry.setWantsAdaptiveSubdivision_, 0)

            self.assertResultIsBOOL(SceneKit.SCNGeometryTessellator.isAdaptive)
            self.assertArgIsBOOL(SceneKit.SCNGeometryTessellator.setAdaptive_, 0)

            self.assertResultIsBOOL(SceneKit.SCNGeometryTessellator.isScreenSpace)
            self.assertArgIsBOOL(SceneKit.SCNGeometryTessellator.setScreenSpace_, 0)

if __name__ == "__main__":
    main()
