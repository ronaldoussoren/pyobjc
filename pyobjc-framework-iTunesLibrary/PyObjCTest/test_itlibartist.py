import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase


class TestITLibArtist(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibArtist, objc.objc_class)
