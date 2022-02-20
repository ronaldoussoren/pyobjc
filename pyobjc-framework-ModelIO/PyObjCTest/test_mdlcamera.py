from PyObjCTools.TestSupport import TestCase
import ModelIO


class TestMDLCamera(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLCameraProjection)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLCameraProjectionPerspective, 0)
        self.assertEqual(ModelIO.MDLCameraProjectionOrthographic, 1)

    def testMethods(self):
        self.assertArgIsBOOL(ModelIO.MDLCamera.frameBoundingBox_setNearAndFar_, 1)
