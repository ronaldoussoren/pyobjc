
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSComboBoxHelper (NSObject):
    def numberOfItemsInComboBox_(self, b): return 1
    def comboBox_objectValueForItemAtIndex_(self, b, i): return 1
    def comboBox_indexOfItemWithStringValue_(self, b, s): return 1


class TestNSComboBox (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSComboBoxWillPopUpNotification, unicode)
        self.assertIsInstance(NSComboBoxWillDismissNotification, unicode)
        self.assertIsInstance(NSComboBoxSelectionDidChangeNotification, unicode)
        self.assertIsInstance(NSComboBoxSelectionIsChangingNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSComboBox.hasVerticalScroller)
        self.assertArgIsBOOL(NSComboBox.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(NSComboBox.isButtonBordered)
        self.assertArgIsBOOL(NSComboBox.setButtonBordered_, 0)
        self.assertResultIsBOOL(NSComboBox.usesDataSource)
        self.assertArgIsBOOL(NSComboBox.setUsesDataSource_, 0)
        self.assertResultIsBOOL(NSComboBox.completes)
        self.assertArgIsBOOL(NSComboBox.setCompletes_, 0)

    @min_os_level('10.6')
    def testProtocolObjects(self):
        objc.protocolNamed('NSComboBoxDataSource')
        objc.protocolNamed('NSComboBoxDelegate')

    def testProtocols(self):
        self.assertResultHasType(TestNSComboBoxHelper.numberOfItemsInComboBox_, objc._C_NSInteger)
        self.assertArgHasType(TestNSComboBoxHelper.comboBox_objectValueForItemAtIndex_, 1, objc._C_NSInteger)
        self.assertResultHasType(TestNSComboBoxHelper.comboBox_indexOfItemWithStringValue_, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
