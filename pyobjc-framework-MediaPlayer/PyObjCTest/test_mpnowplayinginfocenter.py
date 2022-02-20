from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_level_key,
    os_release,
    expectedFailureIf,
)
import MediaPlayer


class TestMPNowPlayingInfoCenter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MediaPlayer.MPNowPlayingInfoMediaType)
        self.assertIsEnumType(MediaPlayer.MPNowPlayingPlaybackState)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeNone, 0)
        self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeAudio, 1)
        self.assertEqual(MediaPlayer.MPNowPlayingInfoMediaTypeVideo, 2)
        self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateUnknown, 0)
        self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStatePlaying, 1)
        self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStatePaused, 2)
        self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateStopped, 3)
        self.assertEqual(MediaPlayer.MPNowPlayingPlaybackStateInterrupted, 4)

        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyElapsedPlaybackTime, str
        )
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackRate, str)
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyDefaultPlaybackRate, str
        )
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyPlaybackQueueIndex, str
        )
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyPlaybackQueueCount, str
        )
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyChapterNumber, str)
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyChapterCount, str)
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyIsLiveStream, str)
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyAvailableLanguageOptions, str
        )
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyCurrentLanguageOptions, str
        )
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoCollectionIdentifier, str)
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyExternalContentIdentifier, str
        )
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyExternalUserProfileIdentifier, str
        )
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyPlaybackProgress, str)
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyMediaType, str)
        self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyAssetURL, str)

    @min_os_level("10.13")
    @expectedFailureIf(
        os_level_key(os_release()) < os_level_key("10.14")
    )  # Documented for 10.13, but doesn't work there
    def testConstants10_13(self):
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyServiceIdentifier, str
        )

    @min_os_level("10.13.1")
    def testConstants10_13_1(self):
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyCurrentPlaybackDate, str
        )
