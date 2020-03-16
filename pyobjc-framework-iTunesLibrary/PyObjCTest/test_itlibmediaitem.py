import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestITMediaItem(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItem, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isRatingComputed)

        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.hasArtworkAvailable)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isPurchased)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isCloud)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isDRMProtected)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isVideo)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isUserDisabled)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindUnknown, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindSong, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindMovie, 3)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPodcast, 4)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindAudiobook, 5)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPDFBooklet, 6)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindMusicVideo, 7)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindTVShow, 8)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindInteractiveBooklet, 9)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindHomeVideo, 12)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindRingtone, 14)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindDigitalBooklet, 15)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindIOSApplication, 16)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindVoiceMemo, 17)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindiTunesU, 18)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindBook, 19)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPDFBook, 20)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindAlertTone, 21)

        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingNone, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingExplicit, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingClean, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeUnknown, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeFile, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeURL, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeRemote, 3)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusNone, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusPartiallyPlayed, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusUnplayed, 2)

        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumTitle, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortAlbumTitle, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumArtist, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumRating, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumRatingComputed, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortAlbumArtist, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumIsGapless, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumIsCompilation, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumDiscCount, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumDiscNumber, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumTrackCount, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyArtistName, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortArtistName, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoIsHD, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoWidth, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoHeight, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoSeries, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoSortSeries, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoSeason, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoEpisode, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVideoEpisodeOrder, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyHasArtwork, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyBitRate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyBeatsPerMinute, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyCategory, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyComments, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyComposer, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortComposer, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyContentRating, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyLyricsContentRating, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAddedDate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyModifiedDate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyDescription, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsUserDisabled, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyGenre, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyGrouping, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsVideo, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyKind, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTitle, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortTitle, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVolumeNormalizationEnergy, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyPlayCount, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLastPlayDate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsDRMProtected, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsPurchased, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyRating, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyRatingComputed, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyReleaseDate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySampleRate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySize, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyFileSize, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyUserSkipCount, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySkipDate, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyStartTime, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyStopTime, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTotalTime, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTrackNumber, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLocationType, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVoiceOverLanguage, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVolumeAdjustment, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyYear, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMediaKind, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLocation, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyArtwork, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyPlayStatus, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMovementCount, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMovementName, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMovementNumber, str)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyWork, str)

    @expectedFailure
    def testConstants_missing(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyFileType, str)
