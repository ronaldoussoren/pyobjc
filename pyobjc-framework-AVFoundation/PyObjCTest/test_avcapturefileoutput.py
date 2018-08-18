from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureFileOutputHelper (AVFoundation.NSObject):
    def captureOutputShouldProvideSampleAccurateRecordingStart_(self, a): return 1

class TestAVCaptureFileOutput (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecording)
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecordingPaused)

    def testProtocols(self):
        objc.protocolNamed('AVCaptureFileOutputRecordingDelegate')
        objc.protocolNamed('AVCaptureFileOutputDelegate')

    def testMethods(self):
        self.assertResultIsBOOL(TestAVCaptureFileOutputHelper.captureOutputShouldProvideSampleAccurateRecordingStart_)


if __name__ == "__main__":
    main()
