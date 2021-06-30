import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSTextRangeHelper(AppKit.NSObject):
    def compare_(self, a):
        pass


class TestNSTextRange(TestCase):
    def test_methods(self):
        self.assertResultHasType(TestNSTextRangeHelper.compare_, objc._C_NSInteger)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AppKit.NSTextRange.isEmpty)
        self.assertResultIsBOOL(AppKit.NSTextRange.isEqualToTextRange_)
        self.assertResultIsBOOL(AppKit.NSTextRange.containsLocation_)
        self.assertResultIsBOOL(AppKit.NSTextRange.containsRange_)
        self.assertResultIsBOOL(AppKit.NSTextRange.intersectsWithTextRange_)
