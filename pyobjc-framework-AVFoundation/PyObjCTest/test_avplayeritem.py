from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVPlayerItem (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemTimeJumpedNotification, unicode)
        self.assertIsInstance(AVFoundation.AVPlayerItemDidPlayToEndTimeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVPlayerItemFailedToPlayToEndTimeNotification, unicode)

        self.assertIsInstance(AVFoundation.AVPlayerItemFailedToPlayToEndTimeErrorKey, unicode)

        self.assertEqual(AVFoundation.AVPlayerItemStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerItemStatusReadyToPlay, 1)
        self.assertEqual(AVFoundation.AVPlayerItemStatusFailed, 2)


    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemPlaybackStalledNotification, unicode)
        self.assertIsInstance(AVFoundation.AVPlayerItemNewAccessLogEntryNotification, unicode)
        self.assertIsInstance(AVFoundation.AVPlayerItemNewErrorLogEntryNotification, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(AVFoundation.AVPlayerItem.seekToTime_completionHandler_, 1, b'vZ')
        self.assertArgIsBlock(AVFoundation.AVPlayerItem.seekToTime_toleranceBefore_toleranceAfter_completionHandler_, 3, b'vZ')
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.seekToDate_)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.seekToDate_completionHandler_)
        self.assertArgIsBlock(AVFoundation.AVPlayerItem.seekToDate_completionHandler_, 1, b'vZ')
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackLikelyToKeepUp)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackBufferFull)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackBufferEmpty)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayFastForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlaySlowForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlaySlowReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayFastReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canStepForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canStepBackward)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.seekingWaitsForVideoCompositionRendering)
        self.assertArgIsBOOL(AVFoundation.AVPlayerItem.setSeekingWaitsForVideoCompositionRendering_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canUseNetworkResourcesForLiveStreamingWhilePaused)
        self.assertArgIsBOOL(AVFoundation.AVPlayerItem.setCanUseNetworkResourcesForLiveStreamingWhilePaused_, 0)

if __name__ == "__main__":
    main()
