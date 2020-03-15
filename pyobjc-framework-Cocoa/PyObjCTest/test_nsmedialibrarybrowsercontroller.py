import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMediaLibraryBrowserController(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSMediaLibraryAudio, 1 << 0)
        self.assertEqual(AppKit.NSMediaLibraryImage, 1 << 1)
        self.assertEqual(AppKit.NSMediaLibraryMovie, 1 << 2)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMediaLibraryBrowserController.isVisible)
        self.assertArgIsBOOL(AppKit.NSMediaLibraryBrowserController.setVisible_, 0)
