from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLTransformHelper (ModelIO.NSObject):
        def matrix(self): return 1
        def setMatrix_(self, v): return 1

        def resetsTransform(self): return 1
        def setResetsTransform_(self, v): return 1

        def minimumTime(self): return 1
        def setMinimumTime_(self, v): return 1

        def maximumTime(self): return 1
        def setMaximumTime_(self, v): return 1

        def setLocalTransform_forTime_(self, t, tm): pass
        def setLocalTransform_(self, t): pass
        def localTransformAtTime_(self, t): return 1
        def globalTransformWithObject_atTime_(self, o, t): return 1

    class TestMDLTransform (TestCase):
        def testMethods(self):
            #self.assertResultHasType(ModelIO.TestMDLTransformHelper.matrix, ...) # SIMD
            #self.assertResultHasType(ModelIO.TestMDLTransformHelper.setMatrix_, 0, ...) # SIMD

            self.assertResultIsBOOL(ModelIO.TestMDLTransformHelper.resetsTransform)
            self.assertArgIsBOOL(ModelIO.TestMDLTransformHelper.setResetsTransform_, 0)

            self.assertResultHasType(ModelIO.TestMDLTransformHelper.minimumTime, objc._C_DBL)
            self.assertArgHasType(ModelIO.TestMDLTransformHelper.setMinimumTime_, 0, objc._C_DBL)

            self.assertResultHasType(ModelIO.TestMDLTransformHelper.maximumTime, objc._C_DBL)
            self.assertArgHasType(ModelIO.TestMDLTransformHelper.setMaximumTime_, 0, objc._C_DBL)

            #self.assertArgHasType(ModelIO.TestMDLTransformHelper.setLocalTransform_forTime_, 0, ...) # SIMD
            self.assertArgHasType(ModelIO.TestMDLTransformHelper.setLocalTransform_forTime_, 1, objc._C_DBL)

            #self.assertArgHasType(ModelIO.TestMDLTransformHelper.setLocalTransform_, 0, ...) # SIMD

            #self.assertResultHasType(ModelIO.TestMDLTransformHelper.localTransformAtTime_, ...) # SIMD
            self.assertArgHasType(ModelIO.TestMDLTransformHelper.localTransformAtTime_, 0, objc._C_DBL)

            #self.assertResultHasType(ModelIO.TestMDLTransformHelper.globalTransformWithObject_atTime_, ...) # SIMD
            #self.assertArgHasType(ModelIO.TestMDLTransformHelper.globalTransformWithObject_atTime_, 1, objc._C_DBL)

            #self.assertArgIsHasType(ModelIO.MDLTransform.initWithMatrix_resetsTransform_, 0, ...) # SIMD
            #self.assertArgIsBOOL(ModelIO.MDLTransform.initWithMatrix_resetsTransform_, 1)

        @min_os_level('10.12')
        def testMethods10_12(self):
            self.assertArgIsBOOL(ModelIO.MDLTransform.initWithTransformComponent_resetsTransform_, 1)

        def testProtocolObjects(self):
            objc.protocolNamed('MDLTransformComponent')

if __name__ == "__main__":
    main()
