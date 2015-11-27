from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVPlayer (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVPlayerStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerStatusReadyToPlay, 1)
        self.assertEqual(AVFoundation.AVPlayerStatusFailed, 2)

        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndAdvance, 0)
        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndPause, 1)
        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndNone, 2)


    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVPlayer.seekToDate_completionHandler_, 1, b'vZ')
        self.assertArgIsBlock(AVFoundation.AVPlayer.seekToTime_completionHandler_, 1, b'vZ')
        self.assertArgIsBlock(AVFoundation.AVPlayer.seekToTime_toleranceBefore_toleranceAfter_completionHandler_, 3, b'vZ')
        self.assertArgIsBlock(AVFoundation.AVPlayer.prerollAtRate_completionHandler_, 1, b'vZ')
        self.assertArgIsBlock(AVFoundation.AVPlayer.addPeriodicTimeObserverForInterval_queue_usingBlock_, 2, b'v{_CMTime=qiIq}')
        self.assertArgIsBlock(AVFoundation.AVPlayer.addBoundaryTimeObserverForTimes_queue_usingBlock_, 2, b'v')
        self.assertResultIsBOOL(AVFoundation.AVPlayer.isMuted)
        self.assertArgIsBOOL(AVFoundation.AVPlayer.setMuted_, 0)
        self.assertResultIsBOOL(AVFoundation.AVPlayer.isClosedCaptionDisplayEnabled)
        self.assertArgIsBOOL(AVFoundation.AVPlayer.setClosedCaptionDisplayEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVQueuePlayer.canInsertItem_afterItem_)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayer.appliesMediaSelectionCriteriaAutomatically)
        self.assertArgIsBOOL(AVFoundation.AVPlayer.setAppliesMediaSelectionCriteriaAutomatically_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayer.allowsExternalPlayback)
        self.assertArgIsBOOL(AVFoundation.AVPlayer.setAllowsExternalPlayback_, 0)
        self.assertResultIsBOOL(AVFoundation.AVPlayer.isExternalPlaybackActive)

if __name__ == "__main__":
    main()
