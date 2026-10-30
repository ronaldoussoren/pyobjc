import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableRowView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTableRowView.isEmphasized)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setEmphasized_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isGroupRowStyle)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setGroupRowStyle_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setSelected_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isFloating)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setFloating_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isTargetForDropOperation)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setTargetForDropOperation_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isNextRowSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setNextRowSelected_, 0)

        self.assertResultIsBOOL(AppKit.NSTableRowView.isPreviousRowSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setPreviousRowSelected_, 0)
