import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMAMusicHaptics(TestCase):
    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(
            MediaAccessibility.MAMusicHapticsManagerActiveStatusDidChangeNotification,
            str,
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(MediaAccessibility.MAMusicHapticsManager.isActive)
        self.assertArgIsBlock(
            MediaAccessibility.MAMusicHapticsManager.checkHapticTrackAvailabilityForMediaMatchingCode_completionHandler_,
            1,
            b"vZ",
        )
        self.assertArgIsBlock(
            MediaAccessibility.MAMusicHapticsManager.addStatusObserver_, 0, b"v@Z"
        )
