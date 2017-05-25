from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibMediaItemVideoInfo (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemVideoInfo, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItemVideoInfo.isHD)

if __name__ == "__main__":
    main()
