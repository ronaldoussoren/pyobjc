from PyObjCTools.TestSupport import TestCase
import ModelIO


class TestMDLCamera(TestCase):
    def testConstants(self):
        self.assertEqual(ModelIO.MDLCameraProjectionPerspective, 0)
        self.assertEqual(ModelIO.MDLCameraProjectionOrthographic, 1)

    def testMethods(self):
        self.assertArgIsBOOL(ModelIO.MDLCamera.frameBoundingBox_setNearAndFar_, 1)
