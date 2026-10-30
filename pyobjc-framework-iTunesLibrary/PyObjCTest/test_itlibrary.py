import iTunesLibrary
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestITLibrary(TestCase):
    def test_enums(self):
        self.assertIsEnumType(iTunesLibrary.ITLibExportFeature)
        self.assertEqual(iTunesLibrary.ITLibExportFeatureNone, 0)

        self.assertIsEnumType(iTunesLibrary.ITLibInitOptions)
        self.assertEqual(iTunesLibrary.ITLibInitOptionNone, 0)
        self.assertEqual(iTunesLibrary.ITLibInitOptionLazyLoadData, 1)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(iTunesLibrary.ITLibraryDidChangeNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.shouldShowContentRating)

        self.assertArgIsOut(iTunesLibrary.ITLibrary.libraryWithAPIVersion_error_, 1)
        self.assertArgIsOut(iTunesLibrary.ITLibrary.initWithAPIVersion_error_, 1)

        self.assertResultIsBOOL(iTunesLibrary.ITLibrary.reloadData)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsOut(
            iTunesLibrary.ITLibrary.libraryWithAPIVersion_options_error_, 2
        )
        self.assertArgIsOut(
            iTunesLibrary.ITLibrary.initWithAPIVersion_options_error_, 2
        )
