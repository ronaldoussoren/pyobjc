from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import ModelIO
from objc import simd


class TestMDLTransformHelper(ModelIO.NSObject):
    def matrix(self):
        return 1

    def setMatrix_(self, v):
        return 1

    def resetsTransform(self):
        return 1

    def setResetsTransform_(self, v):
        return 1

    def minimumTime(self):
        return 1

    def setMinimumTime_(self, v):
        return 1

    def maximumTime(self):
        return 1

    def setMaximumTime_(self, v):
        return 1

    def setLocalTransform_forTime_(self, t, tm):
        pass

    def setLocalTransform_(self, t):
        pass

    def localTransformAtTime_(self, t):
        return 1

    def globalTransformWithObject_atTime_(self, o, t):
        return 1


class TestMDLTransform(TestCase):
    def testMethods(self):
        self.assertResultHasType(
            ModelIO.TestMDLTransformHelper.matrix, simd.simd_float4x4.__typestr__
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setMatrix_,
            0,
            simd.simd_float4x4.__typestr__,
        )

        self.assertResultIsBOOL(ModelIO.TestMDLTransformHelper.resetsTransform)
        self.assertArgIsBOOL(ModelIO.TestMDLTransformHelper.setResetsTransform_, 0)

        self.assertResultHasType(
            ModelIO.TestMDLTransformHelper.minimumTime, objc._C_DBL
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setMinimumTime_, 0, objc._C_DBL
        )

        self.assertResultHasType(
            ModelIO.TestMDLTransformHelper.maximumTime, objc._C_DBL
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setMaximumTime_, 0, objc._C_DBL
        )

        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setLocalTransform_forTime_,
            0,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setLocalTransform_forTime_, 1, objc._C_DBL
        )

        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.setLocalTransform_,
            0,
            simd.simd_float4x4.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.TestMDLTransformHelper.localTransformAtTime_,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.localTransformAtTime_, 0, objc._C_DBL
        )

        self.assertResultHasType(
            ModelIO.TestMDLTransformHelper.globalTransformWithObject_atTime_,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.TestMDLTransformHelper.globalTransformWithObject_atTime_,
            1,
            objc._C_DBL,
        )

        self.assertArgHasType(
            ModelIO.MDLTransform.initWithMatrix_, 0, simd.simd_float4x4.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLTransform.translationAtTime_, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.rotationAtTime_, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.shearAtTime_, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.scaleAtTime_, simd.vector_float3.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLTransform.setTranslation_forTime_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setRotation_forTime_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setShear_forTime_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setScale_forTime_, 0, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLTransform.rotationMatrixAtTime_, simd.simd_float4x4.__typestr__
        )

        self.assertResultHasType(
            ModelIO.MDLTransform.translation, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.rotation, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.shear, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            ModelIO.MDLTransform.scale, simd.vector_float3.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLTransform.setTranslation_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setRotation_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setShear_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setScale_, 0, simd.vector_float3.__typestr__
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgHasType(
            ModelIO.MDLTransform.initWithMatrix_resetsTransform_,
            0,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLTransform.setMatrix_forTime_, 0, simd.simd_float4x4.__typestr__
        )
        self.assertArgIsBOOL(ModelIO.MDLTransform.initWithMatrix_resetsTransform_, 1)
        self.assertArgIsBOOL(
            ModelIO.MDLTransform.initWithTransformComponent_resetsTransform_, 1
        )

    def testProtocolObjects(self):
        self.assertProtocolExists("MDLTransformComponent")
