
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButtonCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPopUpNoArrow, 0)
        self.failUnlessEqual(NSPopUpArrowAtCenter, 1)
        self.failUnlessEqual(NSPopUpArrowAtBottom, 2)

        self.failUnlessIsInstance(NSPopUpButtonCellWillPopUpNotification, unicode)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSPopUpButtonCell.initTextCell_pullsDown_, 1)
        self.failUnlessResultIsBOOL(NSPopUpButtonCell.pullsDown)
        self.failUnlessArgIsBOOL(NSPopUpButtonCell.setPullsDown_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButtonCell.autoenablesItems)
        self.failUnlessArgIsBOOL(NSPopUpButtonCell.setAutoenablesItems_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButtonCell.usesItemFromMenu)
        self.failUnlessArgIsBOOL(NSPopUpButtonCell.setUsesItemFromMenu_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButtonCell.altersStateOfSelectedItem)
        self.failUnlessArgIsBOOL(NSPopUpButtonCell.setAltersStateOfSelectedItem_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButtonCell.selectItemWithTag_)


if __name__ == "__main__":
    main()
