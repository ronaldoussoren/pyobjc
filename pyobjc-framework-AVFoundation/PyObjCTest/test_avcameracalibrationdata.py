from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCameraCalibrationData (TestCase):
    @min_os_level('10.13')
    def testMethods_vector(self):
        self.fail("AVCameraCalibrationData.extrinsicMatrix")

if __name__ == "__main__":
    main()
