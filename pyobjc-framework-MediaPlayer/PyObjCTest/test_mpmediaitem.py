from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer
import Quartz


class TestMPMediaItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MediaPlayer.MPMediaType)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(MediaPlayer.MPMediaTypeMusic, 1 << 0)
        self.assertEqual(MediaPlayer.MPMediaTypePodcast, 1 << 1)
        self.assertEqual(MediaPlayer.MPMediaTypeAudioBook, 1 << 2)
        self.assertEqual(MediaPlayer.MPMediaTypeAudioITunesU, 1 << 3)
        self.assertEqual(MediaPlayer.MPMediaTypeAnyAudio, 0x00FF)
        self.assertEqual(MediaPlayer.MPMediaTypeMovie, 1 << 8)
        self.assertEqual(MediaPlayer.MPMediaTypeTVShow, 1 << 9)
        self.assertEqual(MediaPlayer.MPMediaTypeVideoPodcast, 1 << 10)
        self.assertEqual(MediaPlayer.MPMediaTypeMusicVideo, 1 << 11)
        self.assertEqual(MediaPlayer.MPMediaTypeVideoITunesU, 1 << 12)
        self.assertEqual(MediaPlayer.MPMediaTypeHomeVideo, 1 << 13)
        self.assertEqual(MediaPlayer.MPMediaTypeAnyVideo, 0xFF00)

        self.assertEqual(MediaPlayer.MPMediaTypeAny, 0xFFFFFFFFFFFFFFFF)

        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyMediaType, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyTitle, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTitle, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumPersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtist, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtistPersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumArtist, str)
        self.assertIsInstance(
            MediaPlayer.MPMediaItemPropertyAlbumArtistPersistentID, str
        )
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyGenre, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyGenrePersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComposer, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComposerPersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPlaybackDuration, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTrackNumber, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTrackCount, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDiscNumber, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDiscCount, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtwork, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyIsExplicit, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyLyrics, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyReleaseDate, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyBeatsPerMinute, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComments, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAssetURL, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyIsCloudItem, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyHasProtectedAsset, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPodcastTitle, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPodcastPersistentID, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPlayCount, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertySkipCount, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyRating, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyLastPlayedDate, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyUserGrouping, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyBookmarkTime, str)
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDateAdded, str)

    @min_os_level("10.13.1")
    def testConstants10_13(self):
        self.assertIsInstance(
            MediaPlayer.MPNowPlayingInfoPropertyCurrentPlaybackDate, str
        )
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPlaybackStoreID, str)

    @min_os_level("11.3")
    def testConstants11_3(self):
        self.assertIsInstance(MediaPlayer.MPMediaItemPropertyIsPreorder, str)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isExplicitItem)
        self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isCompilation)
        self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isCloudItem)
        self.assertResultIsBOOL(MediaPlayer.MPMediaItem.hasProtectedAsset)

        self.assertArgIsBlock(
            MediaPlayer.MPMediaItemArtwork.initWithBoundsSize_requestHandler_,
            1,
            b"@" + Quartz.CGSize.__typestr__,
        )
