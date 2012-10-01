from PyObjCTools.TestSupport import *

import AppKit

class TestNSTableRowView (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
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

if __name__ == "__main__":
    main()
