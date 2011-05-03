
from PyObjCTools.TestSupport import *
from PreferencePanes import *

class TestNSPreferencePane (TestCase):
    def testConstants(self):
        self.assertEqual(NSUnselectCancel, 0)
        self.assertEqual(NSUnselectNow, 1)
        self.assertEqual(NSUnselectLater, 2)

        self.assertIsInstance(NSPreferencePaneDoUnselectNotification, unicode)
        self.assertIsInstance(NSPreferencePaneCancelUnselectNotification, unicode)

        self.assertEqual(kNSPrefPaneHelpMenuInfoPListKey, "NSPrefPaneHelpAnchors")
        self.assertEqual(kNSPrefPaneHelpMenuTitleKey, "title")
        self.assertEqual(kNSPrefPaneHelpMenuAnchorKey, "anchor")

    def testClasses(self):
        self.assertArgIsBOOL(NSPreferencePane.replyToShouldUnselect_, 0)
        self.assertResultIsBOOL(NSPreferencePane.autoSaveTextFields)
        self.assertResultIsBOOL(NSPreferencePane.isSelected)

if __name__ == "__main__":
    main()
