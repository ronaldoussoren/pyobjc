from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibrary (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibrary, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.shouldShowContentRating)
        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.reloadData)

        self.assertArgIsOut(iTunesLibrary.ITLibrary.libraryWithAPIVersion_error_, 1)
        self.assertArgIsOut(iTunesLibrary.ITLibrary.initWithAPIVersion_error_, 1)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibExportFeatureNone, 0)


if __name__ == "__main__":
    main()
