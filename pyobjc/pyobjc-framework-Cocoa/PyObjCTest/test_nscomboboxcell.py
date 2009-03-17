from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSComboBoxCell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSComboBoxCell.hasVerticalScroller)
        self.failUnlessArgIsBOOL(NSComboBoxCell.setHasVerticalScroller_, 0)
        self.failUnlessResultIsBOOL(NSComboBoxCell.isButtonBordered)
        self.failUnlessArgIsBOOL(NSComboBoxCell.setButtonBordered_, 0)
        self.failUnlessResultIsBOOL(NSComboBoxCell.usesDataSource)
        self.failUnlessArgIsBOOL(NSComboBoxCell.setUsesDataSource_, 0)
        self.failUnlessResultIsBOOL(NSComboBoxCell.completes)
        self.failUnlessArgIsBOOL(NSComboBoxCell.setCompletes_, 0)

if __name__ == "__main__":
    main()
