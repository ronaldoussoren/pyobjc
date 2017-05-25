from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibArtist (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibArtist, objc.objc_class)

if __name__ == "__main__":
    main()
