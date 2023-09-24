from PyObjCTools.TestSupport import TestCase, min_os_level
import ModelIO
from objc import simd


class TestMDLAnimatedValue(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLAnimatedValueInterpolation)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLAnimatedValueInterpolationConstant, 0)
        self.assertEqual(ModelIO.MDLAnimatedValueInterpolationLinear, 1)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(ModelIO.MDLAnimatedValue.isAnimated)

        self.assertArgIsOut(ModelIO.MDLAnimatedValue.getTimes_maxCount_, 0)
        self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.getTimes_maxCount_, 0, 1)
        self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.getTimes_maxCount_, 0)

        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.setFloatArray_count_atTime_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.setFloatArray_count_atTime_, 0, 1
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.setFloatArray_count_atTime_, 0
        )

        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.setDoubleArray_count_atTime_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.setDoubleArray_count_atTime_, 0, 1
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.setDoubleArray_count_atTime_, 0
        )

        self.assertArgIsOut(
            ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_atTime_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_atTime_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_atTime_, 0
        )

        self.assertArgIsOut(
            ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_atTime_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_atTime_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_atTime_, 0
        )

        self.assertArgIsOut(ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_, 0)
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedScalarArray.getFloatArray_maxCount_, 0
        )

        self.assertArgIsOut(ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_, 0)
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedScalarArray.getDoubleArray_maxCount_, 0
        )

        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_, 0
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithFloatArray_count_atTimes_count_, 2
        )

        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_, 0
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_, 0
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalarArray.resetWithDoubleArray_count_atTimes_count_, 2
        )

        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 0
        )

        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 0
        )

        self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.getFloatArray_maxCount_, 0, 1)
        self.assertArgSizeInResult(ModelIO.MDLAnimatedScalar.getFloatArray_maxCount_, 0)
        self.assertArgIsOut(ModelIO.MDLAnimatedScalar.getFloatArray_maxCount_, 0)

        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedScalar.getDoubleArray_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedScalar.getDoubleArray_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedScalar.getDoubleArray_maxCount_, 0)

    @min_os_level("10.13")
    def testMethodsVector(self):
        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.setFloat3Array_count_atTime_,
            0,
            b"n^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.setFloat3Array_count_atTime_, 0, 1
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.setFloat3Array_count_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.setDouble3Array_count_atTime_,
            0,
            b"n^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.setDouble3Array_count_atTime_, 0, 1
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.setDouble3Array_count_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_atTime_,
            0,
            b"o^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_atTime_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_atTime_, 0
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_atTime_,
            0,
            b"o^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_atTime_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_atTime_, 0
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.resetWithFloat3Array_count_atTimes_count_,
            0,
            b"n^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.resetWithFloat3Array_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.resetWithFloat3Array_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.resetWithFloat3Array_count_atTimes_count_, 0
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.resetWithFloat3Array_count_atTimes_count_, 2
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.resetWithDouble3Array_count_atTimes_count_,
            0,
            b"n^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.resetWithDouble3Array_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.resetWithDouble3Array_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.resetWithDouble3Array_count_atTimes_count_,
            0,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3Array.resetWithDouble3Array_count_atTimes_count_,
            2,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_,
            0,
            b"o^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector3Array.getFloat3Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_,
            0,
            b"o^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_, 0
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedVector3Array.getDouble3Array_maxCount_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.setFloatQuaternionArray_count_atTime_,
            0,
            b"n^" + simd.simd_quatf.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.setFloatQuaternionArray_count_atTime_,
            0,
            1,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.setFloatQuaternionArray_count_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.setDoubleQuaternionArray_count_atTime_,
            0,
            b"n^" + simd.simd_quatd.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.setDoubleQuaternionArray_count_atTime_,
            0,
            1,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.setDoubleQuaternionArray_count_atTime_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_atTime_,
            0,
            b"o^" + simd.simd_quatf.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_atTime_,
            0,
            1,
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_atTime_,
            0,
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_atTime_,
            0,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_atTime_,
            0,
            b"o^" + simd.simd_quatd.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_atTime_,
            0,
            1,
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_atTime_,
            0,
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_atTime_,
            0,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.resetWithFloatQuaternionArray_count_atTimes_count_,
            0,
            b"n^" + simd.simd_quatf.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.resetWithFloatQuaternionArray_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.resetWithFloatQuaternionArray_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.resetWithFloatQuaternionArray_count_atTimes_count_,
            0,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.resetWithFloatQuaternionArray_count_atTimes_count_,
            2,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.resetWithDoubleQuaternionArray_count_atTimes_count_,
            0,
            b"n^" + simd.simd_quatd.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.resetWithDoubleQuaternionArray_count_atTimes_count_,
            0,
            1,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.resetWithDoubleQuaternionArray_count_atTimes_count_,
            2,
            3,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.resetWithDoubleQuaternionArray_count_atTimes_count_,
            0,
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedQuaternionArray.resetWithDoubleQuaternionArray_count_atTimes_count_,
            2,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_,
            0,
            b"o^" + simd.simd_quatf.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_, 0
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedQuaternionArray.getFloatQuaternionArray_maxCount_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_,
            0,
            b"o^" + simd.simd_quatd.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_, 0
        )
        self.assertArgIsOut(
            ModelIO.MDLAnimatedQuaternionArray.getDoubleQuaternionArray_maxCount_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_,
            0,
            b"n^" + simd.vector_float2.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_,
            0,
            b"n^" + simd.vector_double2.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector2.getFloat2Array_maxCount_,
            0,
            b"o^" + simd.vector_float2.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.getFloat2Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector2.getFloat2Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector2.getFloat2Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector2.getDouble2Array_maxCount_,
            0,
            b"o^" + simd.vector_double2.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector2.getDouble2Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector2.getDouble2Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector2.getDouble2Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_,
            0,
            b"n^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_,
            0,
            b"n^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3.getFloat3Array_maxCount_,
            0,
            b"o^" + simd.vector_float3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.getFloat3Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3.getFloat3Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector3.getFloat3Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector3.getDouble3Array_maxCount_,
            0,
            b"o^" + simd.vector_double3.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector3.getDouble3Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector3.getDouble3Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector3.getDouble3Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_,
            0,
            b"n^" + simd.vector_float4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_,
            0,
            b"n^" + simd.vector_double4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector4.getFloat4Array_maxCount_,
            0,
            b"o^" + simd.vector_float4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.getFloat4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector4.getFloat4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector4.getFloat4Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedVector4.getDouble4Array_maxCount_,
            0,
            b"o^" + simd.vector_double4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedVector4.getDouble4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedVector4.getDouble4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedVector4.getDouble4Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.setFloat4x4_atTime_,
            0,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.setDouble4x4_atTime_,
            0,
            simd.simd_double4x4.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLAnimatedMatrix4x4.float4x4AtTime_,
            simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLAnimatedMatrix4x4.double4x4AtTime_,
            simd.simd_double4x4.__typestr__,
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.resetWithFloat4x4Array_atTimes_count_,
            0,
            b"n^" + simd.simd_float4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.resetWithFloat4x4Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.resetWithFloat4x4Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedMatrix4x4.resetWithFloat4x4Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.resetWithDouble4x4Array_atTimes_count_,
            0,
            b"n^" + simd.simd_double4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.resetWithDouble4x4Array_atTimes_count_, 0, 2
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.resetWithDouble4x4Array_atTimes_count_, 1, 2
        )
        self.assertArgIsIn(
            ModelIO.MDLAnimatedMatrix4x4.resetWithDouble4x4Array_atTimes_count_, 0
        )

        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.getFloat4x4Array_maxCount_,
            0,
            b"o^" + simd.simd_float4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.getFloat4x4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedMatrix4x4.getFloat4x4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedMatrix4x4.getFloat4x4Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLAnimatedMatrix4x4.getDouble4x4Array_maxCount_,
            0,
            b"o^" + simd.simd_double4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLAnimatedMatrix4x4.getDouble4x4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLAnimatedMatrix4x4.getDouble4x4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLAnimatedMatrix4x4.getDouble4x4Array_maxCount_, 0)
