import AVFoundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVCameraCalibrationData(TestCase):
    @expectedFailure
    @min_os_level("10.13")
    def testMethods_vector(self):
        # vector type
        self.fail("AVCameraCalibrationData.extrinsicMatrix")
