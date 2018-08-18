from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCameraCalibrationData (TestCase):
    @expectedFailure
    @min_os_level('10.13')
    def testMethods_vector(self):
        # vector type
        self.fail("AVCameraCalibrationData.extrinsicMatrix")

if __name__ == "__main__":
    main()
