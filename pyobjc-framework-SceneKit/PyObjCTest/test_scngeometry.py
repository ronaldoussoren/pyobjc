from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNGeometry(TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeTriangles, 0)
        self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeTriangleStrip, 1)
        self.assertEqual(SceneKit.SCNGeometryPrimitiveTypeLine, 2)
        self.assertEqual(SceneKit.SCNGeometryPrimitiveTypePoint, 3)
        self.assertEqual(SceneKit.SCNGeometryPrimitiveTypePolygon, 4)

        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticVertex, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticNormal, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticColor, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticTexcoord, str)

        self.assertEqual(SceneKit.SCNTessellationSmoothingModeNone, 0)
        self.assertEqual(SceneKit.SCNTessellationSmoothingModePNTriangles, 1)
        self.assertEqual(SceneKit.SCNTessellationSmoothingModePhong, 2)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticVertexCrease, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticEdgeCrease, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticBoneWeights, str)
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticBoneIndices, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(SceneKit.SCNGeometrySourceSemanticTangent, str)

    def testMethods(self):
        self.assertArgIsBOOL(
            SceneKit.SCNGeometrySource.geometrySourceWithData_semantic_vectorCount_floatComponents_componentsPerVector_bytesPerComponent_dataOffset_dataStride_,  # noqa: B950
            3,
        )

        self.assertArgIsIn(
            SceneKit.SCNGeometrySource.geometrySourceWithVertices_count_, 0
        )
        self.assertArgSizeInArg(
            SceneKit.SCNGeometrySource.geometrySourceWithVertices_count_, 0, 1
        )

        self.assertArgIsIn(
            SceneKit.SCNGeometrySource.geometrySourceWithNormals_count_, 0
        )
        self.assertArgSizeInArg(
            SceneKit.SCNGeometrySource.geometrySourceWithNormals_count_, 0, 1
        )

        self.assertArgIsIn(
            SceneKit.SCNGeometrySource.geometrySourceWithTextureCoordinates_count_, 0
        )
        self.assertArgSizeInArg(
            SceneKit.SCNGeometrySource.geometrySourceWithTextureCoordinates_count_, 0, 1
        )

        self.assertResultIsBOOL(SceneKit.SCNGeometrySource.floatComponents)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNGeometry.wantsAdaptiveSubdivision)
        self.assertArgIsBOOL(SceneKit.SCNGeometry.setWantsAdaptiveSubdivision_, 0)

        self.assertResultIsBOOL(SceneKit.SCNGeometryTessellator.isAdaptive)
        self.assertArgIsBOOL(SceneKit.SCNGeometryTessellator.setAdaptive_, 0)

        self.assertResultIsBOOL(SceneKit.SCNGeometryTessellator.isScreenSpace)
        self.assertArgIsBOOL(SceneKit.SCNGeometryTessellator.setScreenSpace_, 0)
