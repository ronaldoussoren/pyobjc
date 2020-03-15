import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSBrowserCell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSBrowserCell.isLeaf)
        self.assertArgIsBOOL(AppKit.NSBrowserCell.setLeaf_, 0)
        self.assertResultIsBOOL(AppKit.NSBrowserCell.isLoaded)
        self.assertArgIsBOOL(AppKit.NSBrowserCell.setLoaded_, 0)
