import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
from objc import simd


class TestAVCameraCalibrationData(TestCase):
    @min_os_level("10.13")
    def testMethods_vector(self):
        self.assertResultHasType(
            AVFoundation.AVCameraCalibrationData.intrinsicMatrix,
            simd.matrix_float3x3.__typestr__,
        )
        self.assertResultHasType(
            AVFoundation.AVCameraCalibrationData.extrinsicMatrix,
            simd.matrix_float4x3.__typestr__,
        )
