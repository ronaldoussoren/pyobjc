from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLAnimatedValue (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLAnimatedValueInterpolationConstant, 0)
            self.assertEqual(ModelIO.MDLAnimatedValueInterpolationLinear, 1)

            self.assertEqual(ModelIO.MDLDataPrecisionUndefined, 0)
            self.assertEqual(ModelIO.MDLDataPrecisionFloat, 1)
            self.assertEqual(ModelIO.MDLDataPrecisionDouble, 2)

        @min_os_level('10.13')
        def testMethods(self):
            self.assertResultIsBOOL(ModelIO.isAnimated)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.copyTimesInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.copyTimesInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedValue.copyTimesInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalarArray.setFloatArray_count_atTime_, 0, 1)
            self.assertArgIsIn(ModelIO.MDLAnimatedScalarArray.setFloatArray_count_atTime_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalarArray.setDoubleArray_count_atTime_, 0, 1)
            self.assertArgIsIn(ModelIO.MDLAnimatedScalarArray.setDoubleArray_count_atTime_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_atTime_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_atTime_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_atTime_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_atTime_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_atTime_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_atTime_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.resetWithFloatArray_count_atTimes_count_, 0, 1)
            self.assertArgIsIn(ModelIO.MDLAnimatedValue.resetWithFloatArray_count_atTimes_count_, 0)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.resetWithFloatArray_count_atTimes_count_, 2, 3)
            self.assertArgIsIn(ModelIO.MDLAnimatedValue.resetWithFloatArray_count_atTimes_count_, 2)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.resetWithDoubleArray_count_atTimes_count_, 0, 1)
            self.assertArgIsIn(ModelIO.MDLAnimatedValue.resetWithDoubleArray_count_atTimes_count_, 0)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.resetWithDoubleArray_count_atTimes_count_, 2, 3)
            self.assertArgIsIn(ModelIO.MDLAnimatedValue.resetWithDoubleArray_count_atTimes_count_, 2)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedValue.copyFloatArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedValue.copyDoubleArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedScalar.resetWithFloatArray_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedScalar.resetWithDoubleArray_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.copyFloatArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedScalar.copyFloatArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedScalar.copyFloatArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedScalar.copyDoubleArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedScalar.copyDoubleArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedScalar.copyDoubleArrayInto_maxCount_, 0)


            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector2.resetWithFloat2Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector2.resetWithDouble2Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.copyFloat2ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector2.copyFloat2ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector2.copyFloat2ArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector2.copyDouble2ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector2.copyDouble2ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector2.copyDouble2ArrayInto_maxCount_, 0)


            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector3.resetWithFloat3Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector3.resetWithDouble3Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.copyFloat3ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector3.copyFloat3ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector3.copyFloat3ArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector3.copyDouble3ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector3.copyDouble3ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector3.copyDouble3ArrayInto_maxCount_, 0)


            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector4.resetWithFloat4Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector4.resetWithDouble4Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.copyFloat4ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector4.copyFloat4ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector4.copyFloat4ArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4.copyDouble4ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector4.copyDouble4ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector4.copyDouble4ArrayInto_maxCount_, 0)


            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.resetWithFloat4x4Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.resetWithFloat4x4Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector4x4.resetWithFloat4x4Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.resetWithDouble4x4Array_atTimes_count_, 0, 2)
            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.resetWithDouble4x4Array_atTimes_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLAnimatedVector4x4.resetWithDouble4x4Array_atTimes_count_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.copyFloat4x4ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector4x4.copyFloat4x4ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector4x4.copyFloat4x4ArrayInto_maxCount_, 0)

            self.assertArgSizeInArg(ModelIO.MDLAnimatedVector4x4.copyDouble4x4ArrayInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLAnimatedVector4x4.copyDouble4x4ArrayInto_maxCount_, 0)
            self.assertArgIsOut(ModelIO.MDLAnimatedVector4x4.copyDouble4x4ArrayInto_maxCount_, 0)


if __name__ == "__main__":
    main()
