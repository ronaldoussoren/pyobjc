from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibAlbum (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibAlbum, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isCompilation)
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isRatingComputed)
        self.assertResultIsBOOL(iTunesLibrary.ITLibAlbum.isGapless)


if __name__ == "__main__":
    main()
