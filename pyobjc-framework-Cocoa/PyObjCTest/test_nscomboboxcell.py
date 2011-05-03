from PyObjCTools.TestSupport import *
from AppKit import *

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

if __name__ == "__main__":
    main()
