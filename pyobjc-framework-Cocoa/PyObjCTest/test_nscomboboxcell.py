from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSComboBoxCellHelper (NSObject):
    def numberOfItemsInComboBoxCell_(self, c): return 1
    def comboBoxCell_objectValueForItemAtIndex_(self, c, i): return 1
    def comboBoxCell_indexOfItemWithStringValue_(self, c, v): return 1

class TestNSComboBoxCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSComboBoxCell.hasVerticalScroller)
        self.assertArgIsBOOL(NSComboBoxCell.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(NSComboBoxCell.isButtonBordered)
        self.assertArgIsBOOL(NSComboBoxCell.setButtonBordered_, 0)
        self.assertResultIsBOOL(NSComboBoxCell.usesDataSource)
        self.assertArgIsBOOL(NSComboBoxCell.setUsesDataSource_, 0)
        self.assertResultIsBOOL(NSComboBoxCell.completes)
        self.assertArgIsBOOL(NSComboBoxCell.setCompletes_, 0)

    @min_sdk_level('10.7')
    def testProtocolObjects(self):
        objc.protocolNamed('NSComboBoxCellDataSource')

    def testProtocol(self):
        self.assertResultHasType(TestNSComboBoxCellHelper.numberOfItemsInComboBoxCell_, objc._C_NSInteger)
        self.assertArgHasType(TestNSComboBoxCellHelper.comboBoxCell_objectValueForItemAtIndex_, 1, objc._C_NSInteger)
        self.assertResultHasType(TestNSComboBoxCellHelper.comboBoxCell_indexOfItemWithStringValue_, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
