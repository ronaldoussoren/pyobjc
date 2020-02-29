import iTunesLibrary
import objc
from PyObjCTools.TestSupport import *


class TestITLibMediaItemVideoInfo(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemVideoInfo, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItemVideoInfo.isHD)


if __name__ == "__main__":
    main()
