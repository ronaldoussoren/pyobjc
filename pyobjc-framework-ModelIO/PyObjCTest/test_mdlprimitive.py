from PyObjCTools.TestSupport import TestCase
import objc
import ModelIO


class TestMDLPrimitiveHelper(ModelIO.NSObject):
    def primitiveType(self):
        return 1

    def setPrimitiveType_(self, v):
        pass


class TestMDLPrimitive(TestCase):
    def testConstants(self):
        self.assertEqual(ModelIO.MDLPrimitiveTypeCube, 0)
        self.assertEqual(ModelIO.MDLPrimitiveTypeSphere, 1)
        self.assertEqual(ModelIO.MDLPrimitiveTypeCone, 2)
        self.assertEqual(ModelIO.MDLPrimitiveTypeCapsule, 3)
        self.assertEqual(ModelIO.MDLPrimitiveTypeCylinder, 4)
        self.assertEqual(ModelIO.MDLPrimitiveTypeNone, 5)

    def test_protocol_methods(self):
        # XXX
        self.assertResultHasType(TestMDLPrimitiveHelper.primitiveType, objc._C_ID)
        self.assertArgHasType(TestMDLPrimitiveHelper.setPrimitiveType_, 0, objc._C_ID)
