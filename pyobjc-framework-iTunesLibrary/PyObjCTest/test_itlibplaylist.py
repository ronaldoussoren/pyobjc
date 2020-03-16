import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestITLibPlaylist(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibPlaylist, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibPlaylist.isMaster)
        self.assertResultIsBOOL(iTunesLibrary.ITLibPlaylist.isVisible)
        self.assertResultIsBOOL(iTunesLibrary.ITLibPlaylist.isAllItemsPlaylist)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindNone, 0)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindMovies, 1)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindTVShows, 2)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindMusic, 3)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindBooks, 4)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindRingtones, 5)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindPodcasts, 7)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindVoiceMemos, 14)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindPurchases, 16)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindiTunesU, 26)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKind90sMusic, 42)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindMyTopRated, 43)
        self.assertEqual(
            iTunesLibrary.ITLibDistinguishedPlaylistKindTop25MostPlayed, 44
        )
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindRecentlyPlayed, 45)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindRecentlyAdded, 46)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindMusicVideos, 47)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindClassicalMusic, 48)
        self.assertEqual(
            iTunesLibrary.ITLibDistinguishedPlaylistKindLibraryMusicVideos, 49
        )
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindHomeVideos, 50)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindApplications, 51)
        self.assertEqual(iTunesLibrary.ITLibDistinguishedPlaylistKindLovedSongs, 52)
        self.assertEqual(
            iTunesLibrary.ITLibDistinguishedPlaylistKindMusicShowsAndMovies, 53
        )
        self.assertEqual(iTunesLibrary.ITLibPlaylistKindRegular, 0)
        self.assertEqual(iTunesLibrary.ITLibPlaylistKindSmart, 1)
        self.assertEqual(iTunesLibrary.ITLibPlaylistKindGenius, 2)
        self.assertEqual(iTunesLibrary.ITLibPlaylistKindFolder, 3)
        self.assertEqual(iTunesLibrary.ITLibPlaylistKindGeniusMix, 4)

        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyName, str)
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyAllItemsPlaylist, str)
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyDistinguisedKind, str)
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyMaster, str)
        self.assertIsInstance(
            iTunesLibrary.ITLibPlaylistPropertyParentPersistentID, str
        )
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyVisible, str)
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyItems, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(iTunesLibrary.ITLibPlaylistPropertyKind, str)
