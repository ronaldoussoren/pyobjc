from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureAudioDataOutput (TestCase):
    def testClasses(self):
        AVFoundation.AVCaptureAudioDataOutput

    @min_sdk_level('10.7')
    def testProtocols(self):
        objc.protocolNamed('AVCaptureAudioDataOutputSampleBufferDelegate')

if __name__ == "__main__":
    main()
