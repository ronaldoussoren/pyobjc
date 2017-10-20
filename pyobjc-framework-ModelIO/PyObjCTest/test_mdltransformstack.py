from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLTransformStack (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderXYZ, 1)
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderXZY, 2)
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderYXZ, 3)
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderYZX, 4)
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderZXY, 5)
            self.assertEqual(ModelIO.MDLTransformOpRotationOrderZYX, 6)

        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('MDLTransformOp')

            # XXX: Protocol contains matrix types, needs more work


if __name__ == "__main__":
    main()
