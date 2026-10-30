import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSFormCell(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSFormCell.isOpaque)
