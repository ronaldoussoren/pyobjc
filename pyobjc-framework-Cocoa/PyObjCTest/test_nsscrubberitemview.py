import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScrubberItemView(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSScrubberArrangedView.isSelected)
        self.assertArgIsBOOL(AppKit.NSScrubberArrangedView.setSelected_, 0)

        self.assertResultIsBOOL(AppKit.NSScrubberArrangedView.isHighlighted)
        self.assertArgIsBOOL(AppKit.NSScrubberArrangedView.setHighlighted_, 0)
