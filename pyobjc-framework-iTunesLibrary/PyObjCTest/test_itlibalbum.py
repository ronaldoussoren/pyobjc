import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase


class TestITLibAlbum(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibAlbum, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isCompilation)
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isRatingComputed)
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isGapless)
