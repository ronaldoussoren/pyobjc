
from PyObjCTools.TestSupport import *
from PreferencePanes import *

class TestNSPreferencePane (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSUnselectCancel, 0)
        self.failUnlessEqual(NSUnselectNow, 1)
        self.failUnlessEqual(NSUnselectLater, 2)

        self.failUnlessIsInstance(NSPreferencePaneDoUnselectNotification, unicode)
        self.failUnlessIsInstance(NSPreferencePaneCancelUnselectNotification, unicode)

        self.failUnlessEqual(kNSPrefPaneHelpMenuInfoPListKey, "NSPrefPaneHelpAnchors")
        self.failUnlessEqual(kNSPrefPaneHelpMenuTitleKey, "title")
        self.failUnlessEqual(kNSPrefPaneHelpMenuAnchorKey, "anchor")

    def testClasses(self):
        self.failUnlessArgIsBOOL(NSPreferencePane.replyToShouldUnselect_, 0)
        self.failUnlessResultIsBOOL(NSPreferencePane.autoSaveTextFields)
        self.failUnlessResultIsBOOL(NSPreferencePane.isSelected)

if __name__ == "__main__":
    main()
