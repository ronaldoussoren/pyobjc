
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButtonCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSPopUpNoArrow, 0)
        self.assertEqual(NSPopUpArrowAtCenter, 1)
        self.assertEqual(NSPopUpArrowAtBottom, 2)

        self.assertIsInstance(NSPopUpButtonCellWillPopUpNotification, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(NSPopUpButtonCell.initTextCell_pullsDown_, 1)
        self.assertResultIsBOOL(NSPopUpButtonCell.pullsDown)
        self.assertArgIsBOOL(NSPopUpButtonCell.setPullsDown_, 0)
        self.assertResultIsBOOL(NSPopUpButtonCell.autoenablesItems)
        self.assertArgIsBOOL(NSPopUpButtonCell.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(NSPopUpButtonCell.usesItemFromMenu)
        self.assertArgIsBOOL(NSPopUpButtonCell.setUsesItemFromMenu_, 0)
        self.assertResultIsBOOL(NSPopUpButtonCell.altersStateOfSelectedItem)
        self.assertArgIsBOOL(NSPopUpButtonCell.setAltersStateOfSelectedItem_, 0)
        self.assertResultIsBOOL(NSPopUpButtonCell.selectItemWithTag_)


if __name__ == "__main__":
    main()
