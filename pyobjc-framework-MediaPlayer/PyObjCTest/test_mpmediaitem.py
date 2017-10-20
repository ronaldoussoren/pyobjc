from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer
    import Quartz

    class TestMPMediaItem (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(MediaPlayer.MPMediaTypeMusic, 1 << 0)
            self.assertEqual(MediaPlayer.MPMediaTypePodcast, 1 << 1)
            self.assertEqual(MediaPlayer.MPMediaTypeAudioBook, 1 << 2)
            self.assertEqual(MediaPlayer.MPMediaTypeAudioITunesU, 1 << 3)
            self.assertEqual(MediaPlayer.MPMediaTypeAnyAudio, 0x00ff)
            self.assertEqual(MediaPlayer.MPMediaTypeMovie, 1 << 8)
            self.assertEqual(MediaPlayer.MPMediaTypeTVShow, 1 << 9)
            self.assertEqual(MediaPlayer.MPMediaTypeVideoPodcast, 1 << 10)
            self.assertEqual(MediaPlayer.MPMediaTypeMusicVideo, 1 << 11)
            self.assertEqual(MediaPlayer.MPMediaTypeVideoITunesU, 1 << 12)
            self.assertEqual(MediaPlayer.MPMediaTypeHomeVideo, 1 << 13)
            self.assertEqual(MediaPlayer.MPMediaTypeAnyVideo, 0xff00)

            self.assertEqual(MediaPlayer.MPMediaTypeAny, 0xffffffffffffffff)


            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyMediaType, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyTitle, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTitle, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtist, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtistPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumArtist, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumArtistPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyGenre, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyGenrePersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComposer, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComposerPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPlaybackDuration, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTrackNumber, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAlbumTrackCount, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDiscNumber, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDiscCount, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyArtwork, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyIsExplicit, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyLyrics, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyReleaseDate, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyBeatsPerMinute, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyComments, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyAssetURL, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyIsCloudItem, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyHasProtectedAsset, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPodcastTitle, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPodcastPersistentID, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyPlayCount, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertySkipCount, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyRating, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyLastPlayedDate, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyUserGrouping, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyBookmarkTime, unicode)
            self.assertIsInstance(MediaPlayer.MPMediaItemPropertyDateAdded, unicode)

        @min_os_level('10.13.1')
        def testConstants10_13(self):
            self.assertIsInstance(MediaPlayer.MPNowPlayingInfoPropertyCurrentPlaybackDate, unicode)

        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isExplicitItem)
            self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isCompilation)
            self.assertResultIsBOOL(MediaPlayer.MPMediaItem.isCloudItem)
            self.assertResultIsBOOL(MediaPlayer.MPMediaItem.hasProtectedAsset)

            self.assertArgIsBlock(MediaPlayer.MPMediaItemArtwork.initWithBoundsSize_requestHandler_, 1, b'@' + Quartz.CGSize.__typestr__)


if __name__ == "__main__":
    main()
