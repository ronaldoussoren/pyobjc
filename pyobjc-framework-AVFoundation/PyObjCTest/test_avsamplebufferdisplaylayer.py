from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVSampleBufferDisplayLayer(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusRendering, 1)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusFailed, 2)

        self.assertIsInstance(
            AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotification, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey,
            unicode,
        )

    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.isReadyForMoreMediaData
        )
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferDisplayLayer.requestMediaDataWhenReadyOnQueue_usingBlock_,
            1,
            b"v",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        # Header says 10.15, but new in the 10.14.4 SDK headers
        self.assertResultIsBOOL(AVFoundation.AVSampleBufferDisplayLayer.preventsCapture)
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.setPreventsCapture_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.preventsDisplaySleepDuringVideoPlayback
        )
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.setPreventsDisplaySleepDuringVideoPlayback_,
            0,
        )


if __name__ == "__main__":
    main()
