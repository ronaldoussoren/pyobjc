from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import ModelIO


class TestMDLTransformStack(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLTransformOpRotationOrder)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderXYZ, 1)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderXZY, 2)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderYXZ, 3)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderYZX, 4)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderZXY, 5)
        self.assertEqual(ModelIO.MDLTransformOpRotationOrderZYX, 6)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("MDLTransformOp")

        # XXX: Protocol contains matrix types, needs more work
