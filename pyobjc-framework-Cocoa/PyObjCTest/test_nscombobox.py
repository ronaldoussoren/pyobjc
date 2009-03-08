
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSComboBox (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSComboBoxWillPopUpNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxWillDismissNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSComboBoxSelectionIsChangingNotification, unicode)

if __name__ == "__main__":
    main()
