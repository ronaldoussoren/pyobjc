from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibArtwork (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibArtwork, objc.objc_class)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatNone, 0)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatBitmap, 1)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatJPEG, 2)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatJPEG2000, 3)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatGIF, 4)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatPNG, 5)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatBMP, 6)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatTIFF, 7)
        self.assertEqual(iTunesLibrary.ITLibArtworkFormatPICT, 8)


if __name__ == "__main__":
    main()
