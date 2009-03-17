
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSComboBox (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSComboBoxWillPopUpNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxWillDismissNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxSelectionIsChangingNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSComboBox.hasVerticalScroller)
        self.failUnlessArgIsBOOL(NSComboBox.setHasVerticalScroller_, 0)
        self.failUnlessResultIsBOOL(NSComboBox.isButtonBordered)
        self.failUnlessArgIsBOOL(NSComboBox.setButtonBordered_, 0)
        self.failUnlessResultIsBOOL(NSComboBox.usesDataSource)
        self.failUnlessArgIsBOOL(NSComboBox.setUsesDataSource_, 0)
        self.failUnlessResultIsBOOL(NSComboBox.completes)
        self.failUnlessArgIsBOOL(NSComboBox.setCompletes_, 0)

if __name__ == "__main__":
    main()
