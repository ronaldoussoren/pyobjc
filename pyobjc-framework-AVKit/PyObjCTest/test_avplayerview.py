import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import AVKit

    class TestAVPlayerView (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(AVKit.AVPlayerView, objc.objc_class)

        @min_os_level("10.9")
        def testMethods10_9(self):
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsFrameSteppingButtons_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsFrameSteppingButtons)
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsSharingServiceButton_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsSharingServiceButton)
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsFullScreenToggleButton_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsFullScreenToggleButton)
            self.assertResultIsBOOL(AVKit.AVPlayerView.canBeginTrimming)

            self.assertArgIsBlock(AVKit.AVPlayerView.beginTrimmingWithCompletionHandler_, 0, b"v" + objc._C_NSInteger)

        @min_os_level("10.9")
        @expectedFailure
        def testMethods10_9_missing(self):
            self.assertResultIsBOOL(AVKit.AVCaptureView.alloc().init().isReadyForDisplay)
            self.assertArgIsBOOL(AVKit.AVCaptureView.setReadyForDisplay_, 0)

        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertArgIsBOOL(AVKit.AVPlayerView.setUpdatesNowPlayingInfoCenter_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.updatesNowPlayingInfoCenter)

        @min_os_level("10.9")
        def test_constants(self):
            self.assertEqual(AVKit.AVPlayerViewControlsStyleNone, 0)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleInline, 1)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleFloating, 2)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleMinimal, 3)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleDefault, AVKit.AVPlayerViewControlsStyleInline, 4)

            self.assertEqual(AVKit.AVPlayerViewTrimOKButton, 0)
            self.assertEqual(AVKit.AVPlayerViewTrimCancelButton, 1)

if __name__ == "__main__":
    main()
