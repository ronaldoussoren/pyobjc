import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSPopUpButtonCell(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPopUpArrowPosition)

    def testConstants(self):
        self.assertEqual(AppKit.NSPopUpNoArrow, 0)
        self.assertEqual(AppKit.NSPopUpArrowAtCenter, 1)
        self.assertEqual(AppKit.NSPopUpArrowAtBottom, 2)

        self.assertIsInstance(AppKit.NSPopUpButtonCellWillPopUpNotification, str)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSPopUpButtonCell.initTextCell_pullsDown_, 1)
        self.assertResultIsBOOL(AppKit.NSPopUpButtonCell.pullsDown)
        self.assertArgIsBOOL(AppKit.NSPopUpButtonCell.setPullsDown_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButtonCell.autoenablesItems)
        self.assertArgIsBOOL(AppKit.NSPopUpButtonCell.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButtonCell.usesItemFromMenu)
        self.assertArgIsBOOL(AppKit.NSPopUpButtonCell.setUsesItemFromMenu_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButtonCell.altersStateOfSelectedItem)
        self.assertArgIsBOOL(AppKit.NSPopUpButtonCell.setAltersStateOfSelectedItem_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButtonCell.selectItemWithTag_)
