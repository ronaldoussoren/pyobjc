
from PyObjCTools.TestSupport import *
from AppKit import *

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

if __name__ == "__main__":
    main()
