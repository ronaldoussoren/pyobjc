from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibrary (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibrary, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.shouldShowContentRating)

        self.assertArgIsOut(iTunesLibrary.ITLibrary.libraryWithAPIVersion_error_, 1)
        self.assertArgIsOut(iTunesLibrary.ITLibrary.initWithAPIVersion_error_, 1)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.reloadData)

    @min_os_level('10.14')
    def testMethods10_14(self):
        self.assertArgIsOut(iTunesLibrary.ITLibrary.libraryWithAPIVersion_options_error_, 2)
        self.assertArgIsOut(iTunesLibrary.ITLibrary.initWithAPIVersion_options_error_, 2)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibExportFeatureNone, 0)

        self.assertEqual(iTunesLibrary.ITLibInitOptionNone, 0)
        self.assertEqual(iTunesLibrary.ITLibInitOptionLazyLoadData, 1)


if __name__ == "__main__":
    main()
