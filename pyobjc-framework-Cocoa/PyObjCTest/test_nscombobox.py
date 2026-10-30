import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSComboBoxHelper(AppKit.NSObject):
    def numberOfItemsInComboBox_(self, b):
        return 1

    def comboBox_objectValueForItemAtIndex_(self, b, i):
        return 1

    def comboBox_indexOfItemWithStringValue_(self, b, s):
        return 1


class TestNSComboBox(TestCase):
    def test_constants(self):
        self.assertIsInstance(AppKit.NSComboBoxWillPopUpNotification, str)
        self.assertIsInstance(AppKit.NSComboBoxWillDismissNotification, str)
        self.assertIsInstance(AppKit.NSComboBoxSelectionDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSComboBoxSelectionIsChangingNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSComboBox.hasVerticalScroller)
        self.assertArgIsBOOL(AppKit.NSComboBox.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBox.isButtonBordered)
        self.assertArgIsBOOL(AppKit.NSComboBox.setButtonBordered_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBox.usesDataSource)
        self.assertArgIsBOOL(AppKit.NSComboBox.setUsesDataSource_, 0)
        self.assertResultIsBOOL(AppKit.NSComboBox.completes)
        self.assertArgIsBOOL(AppKit.NSComboBox.setCompletes_, 0)

    def test_protocols(self):
        self.assertProtocolExists("NSComboBoxDataSource", AppKit)
        self.assertProtocolExists("NSComboBoxDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestNSComboBoxHelper.numberOfItemsInComboBox_, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSComboBoxHelper.comboBox_objectValueForItemAtIndex_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSComboBoxHelper.comboBox_indexOfItemWithStringValue_,
            objc._C_NSUInteger,
        )
