import iTunesLibrary
import objc
from PyObjCTools.TestSupport import *


class TestITLibArtist(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibArtist, objc.objc_class)


if __name__ == "__main__":
    main()
