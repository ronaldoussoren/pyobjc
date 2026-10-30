import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase


class TestITLibMediaItemVideoInfo(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemVideoInfo, objc.objc_class)

    def test_methods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItemVideoInfo.isHD)
