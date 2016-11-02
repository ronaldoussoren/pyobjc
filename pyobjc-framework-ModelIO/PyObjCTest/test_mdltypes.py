from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLTypes (TestCase):
        def testConstants(self):
            self.assertIsInstance(ModelIO.kUTTypeAlembic, unicode)
            self.assertIsInstance(ModelIO.kUTType3dObject, unicode)
            self.assertIsInstance(ModelIO.kUTTypePolygon, unicode)
            self.assertIsInstance(ModelIO.kUTTypeStereolithography, unicode)

            self.assertEqual(ModelIO.MDLIndexBitDepthInvalid, 0)
            self.assertEqual(ModelIO.MDLIndexBitDepthUInt8, 8)
            self.assertEqual(ModelIO.MDLIndexBitDepthUint8, 8)
            self.assertEqual(ModelIO.MDLIndexBitDepthUInt16, 16)
            self.assertEqual(ModelIO.MDLIndexBitDepthUint16, 16)
            self.assertEqual(ModelIO.MDLIndexBitDepthUInt32, 32)
            self.assertEqual(ModelIO.MDLIndexBitDepthUint32, 32)

            self.assertEqual(ModelIO.MDLGeometryTypePoints, 0)
            self.assertEqual(ModelIO.MDLGeometryTypeLines, 1)
            self.assertEqual(ModelIO.MDLGeometryTypeTriangles, 2)
            self.assertEqual(ModelIO.MDLGeometryTypeTriangleStrips, 3)
            self.assertEqual(ModelIO.MDLGeometryTypeQuads, 4)
            self.assertEqual(ModelIO.MDLGeometryTypeVariableTopology, 5)

            self.assertEqual(ModelIO.MDLProbePlacementUniformGrid, 0)
            self.assertEqual(ModelIO.MDLProbePlacementIrradianceDistribution, 1)

        @min_os_level('10.12')
        def testConstants10_12(self):
            self.assertIsInstance(ModelIO.kUTTypeUniversalSceneDescription, unicode)

        def testProtocolObjects(self):
            objc.protocolNamed('MDLNamed')
            objc.protocolNamed('MDLComponent')
            objc.protocolNamed('MDLObjectContainerComponent')

        @expectedFailure
        def testStructs(self):
            self.fail("MDLAxisAlignedBoundingBox is SIMD type")

if __name__ == "__main__":
    main()
