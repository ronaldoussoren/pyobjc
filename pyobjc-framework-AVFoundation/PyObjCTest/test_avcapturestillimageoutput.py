from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureStillImageOutput (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(AVFoundation.AVCaptureStillImageOutput.captureStillImageAsynchronouslyFromConnection_completionHandler_, 1, b'v@@')

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureStillImageOutput.isCapturingStillImage)

if __name__ == "__main__":
    main()
