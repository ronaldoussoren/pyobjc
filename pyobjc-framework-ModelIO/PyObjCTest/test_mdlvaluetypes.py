from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import ModelIO

from objc import simd


class TestMDLValueTypes(TestCase):
    @min_os_level("10.13")
    @expectedFailure
    def testMethodsSIMD(self):
        # SIMD types
        self.assertArgHasType(
            ModelIO.MDLMatrix4x4Array.setFloat4x4Array_count_,
            0,
            b"n^" + simd.matrix_float4x4.__typestr__,
        )
        self.assertArgSizeInArg(ModelIO.MDLMatrix4x4Array.setFloat4x4Array_count_, 0, 1)
        self.assertArgIsIn(ModelIO.MDLMatrix4x4Array.setFloat4x4Array_count_, 0)

        self.assertArgHasType(
            ModelIO.MDLMatrix4x4Array.setDouble4x4Array_count_,
            0,
            b"n^" + simd.matrix_double4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLMatrix4x4Array.setDouble4x4Array_count_, 0, 1
        )
        self.assertArgIsIn(ModelIO.MDLMatrix4x4Array.setDouble4x4Array_count_, 0)

        self.assertArgHasType(
            ModelIO.MDLMatrix4x4Array.getFloat4x4Array_maxCount_,
            0,
            b"o^" + simd.matrix_float4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLMatrix4x4Array.getFloat4x4Array_maxCount_, 0)

        self.assertArgHasType(
            ModelIO.MDLMatrix4x4Array.getDouble4x4Array_maxCount_,
            0,
            b"o^" + simd.matrix_double4x4.__typestr__,
        )
        self.assertArgSizeInArg(
            ModelIO.MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0, 1
        )
        self.assertArgSizeInResult(
            ModelIO.MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0
        )
        self.assertArgIsOut(ModelIO.MDLMatrix4x4Array.getDouble4x4Array_maxCount_, 0)
