import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSComboBoxCellHelper(AppKit.NSObject):
    def numberOfItemsInComboBoxCell_(self, c):
        return 1

    def comboBoxCell_objectValueForItemAtIndex_(self, c, i):
        return 1

    def comboBoxCell_indexOfItemWithStringValue_(self, c, v):
        return 1


class TestNSComboBoxCell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSComboBoxCell.hasVerticalScroller)
        self.assertArgIsBOOL(AppKit.NSComboBoxCell.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBoxCell.isButtonBordered)
        self.assertArgIsBOOL(AppKit.NSComboBoxCell.setButtonBordered_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBoxCell.usesDataSource)
        self.assertArgIsBOOL(AppKit.NSComboBoxCell.setUsesDataSource_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBoxCell.completes)
        self.assertArgIsBOOL(AppKit.NSComboBoxCell.setCompletes_, 0)

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        objc.protocolNamed("NSComboBoxCellDataSource")

    def testProtocol(self):
        self.assertResultHasType(
            TestNSComboBoxCellHelper.numberOfItemsInComboBoxCell_, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSComboBoxCellHelper.comboBoxCell_objectValueForItemAtIndex_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSComboBoxCellHelper.comboBoxCell_indexOfItemWithStringValue_,
            objc._C_NSUInteger,
        )
