from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLCamera (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLCameraProjectionPerspective, 0)
            self.assertEqual(ModelIO.MDLCameraProjectionOrthographic, 1)

        def testMethods(self):
            self.assertArgIsBOOL(ModelIO.MDLCamera.frameBoundingBox_setNearAndFar_, 1)

if __name__ == "__main__":
    main()
