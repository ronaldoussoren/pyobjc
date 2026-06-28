import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSMediaLibraryBrowserController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSMediaLibrary)

    def test_constants(self):
        self.assertEqual(AppKit.NSMediaLibraryAudio, 1 << 0)
        self.assertEqual(AppKit.NSMediaLibraryImage, 1 << 1)
        self.assertEqual(AppKit.NSMediaLibraryMovie, 1 << 2)

    def test_methods(self):
        self.assertResultIsBOOL(
            AppKit.NSMediaLibraryBrowserController.sharedMediaLibraryBrowserController().isVisible
        )
        self.assertArgIsBOOL(
            AppKit.NSMediaLibraryBrowserController.sharedMediaLibraryBrowserController().setVisible_,
            0,
        )
