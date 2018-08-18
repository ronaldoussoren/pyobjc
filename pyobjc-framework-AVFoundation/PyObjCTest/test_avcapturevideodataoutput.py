from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureVideoDataOutput (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames)
        self.assertArgIsBOOL(AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_, 0)

    @min_sdk_level('10.7')
    def testProtocols(self):
        objc.protocolNamed('AVCaptureVideoDataOutputSampleBufferDelegate')

if __name__ == "__main__":
    main()
