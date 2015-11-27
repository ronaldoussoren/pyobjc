from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVSampleBufferDisplayLayer (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusRendering, 1)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusFailed, 2)

        self.assertIsInstance(AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey, unicode)

    @min_os_level('10.8')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVSampleBufferDisplayLayer.isReadyForMoreMediaData)
        self.assertArgIsBlock(AVFoundation.AVSampleBufferDisplayLayer.requestMediaDataWhenReadyOnQueue_usingBlock_, 1, b'v')

if __name__ == "__main__":
    main()
