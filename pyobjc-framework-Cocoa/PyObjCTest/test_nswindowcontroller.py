import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSWindowController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSWindowController.shouldCascadeWindows)
        self.assertArgIsBOOL(AppKit.NSWindowController.setShouldCascadeWindows_, 0)
        self.assertArgIsBOOL(AppKit.NSWindowController.setDocumentEdited_, 0)
        self.assertResultIsBOOL(AppKit.NSWindowController.shouldCloseDocument)
        self.assertArgIsBOOL(AppKit.NSWindowController.setShouldCloseDocument_, 0)
        self.assertResultIsBOOL(AppKit.NSWindowController.isWindowLoaded)
