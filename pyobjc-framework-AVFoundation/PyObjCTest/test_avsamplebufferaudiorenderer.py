from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVSampleBufferAudioRenderer (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVSampleBufferAudioRenderer.isMuted)
        self.assertArgIsBOOL(AVFoundation.AVSampleBufferAudioRenderer.setMuted_, 0)

        self.assertArgIsBlock(AVFoundation.AVSampleBufferAudioRenderer.flushFromSourceTime_completionHandler_, 1, b'vZ')


    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification, unicode)
        self.assertIsInstance(AVFoundation.AVSampleBufferAudioRendererFlushTimeKey, unicode)


if __name__ == "__main__":
    main()
