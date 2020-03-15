import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSFormCell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSFormCell.isOpaque)
