from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLPrimitiveHelper (ModelIO.NSObject):
        def primitiveType(self): return 1
        def setPrimitiveType_(self, v): pass

    class TestMDLPrimitive (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLPrimitiveTypeCube, 0)
            self.assertEqual(ModelIO.MDLPrimitiveTypeSphere, 1)
            self.assertEqual(ModelIO.MDLPrimitiveTypeCone, 2)
            self.assertEqual(ModelIO.MDLPrimitiveTypeCapsule, 3)
            self.assertEqual(ModelIO.MDLPrimitiveTypeCylinder, 4)
            self.assertEqual(ModelIO.MDLPrimitiveTypeNone, 5)

        #@min_sdk_level('10.13')
        #def testProtocols(self):
        #    objc.protocolNamed('MDLPrimitiveComponent')

        def testMethods(self):
            self.assertResultHasType(TestMDLPrimitiveHelper.primitiveType, objc._C_NSUInteger)
            self.assertArgHasType(TestMDLPrimitiveHelper.setPrimitiveType_, 0, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
