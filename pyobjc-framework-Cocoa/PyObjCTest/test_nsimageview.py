import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSImage(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSImageView.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.isEditable)
        self.assertArgIsBOOL(AppKit.NSImageView.setAnimates_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.animates)
        self.assertArgIsBOOL(AppKit.NSImageView.setAllowsCutCopyPaste_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.allowsCutCopyPaste)
