import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSActionCell(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSActionCell.setBordered_, 0)
        self.assertArgIsBOOL(AppKit.NSActionCell.setBezeled_, 0)
        self.assertArgIsBOOL(AppKit.NSActionCell.setEnabled_, 0)
        self.assertArgIsBOOL(AppKit.NSActionCell.setFloatingPointFormat_left_right_, 0)
        self.assertArgIsSEL(AppKit.NSActionCell.setAction_, 0, b"v@:@")
