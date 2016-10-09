
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

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSPrefPaneHelpMenuInfoPListKey, unicode)
        self.assertIsInstance(NSPrefPaneHelpMenuTitleKey, unicode)
        self.assertIsInstance(NSPrefPaneHelpMenuAnchorKey, unicode)

    #@min_os_level('10.12')
    # Added in 10.12, but available before that
    def testConstants10_12(self):
        self.assertIsInstance(NSPreferencePaneSwitchToPaneNotification, unicode)
        self.assertIsInstance(NSPreferencePrefPaneIsAvailableNotification, unicode)
        self.assertIsInstance(NSPreferencePaneUpdateHelpMenuNotification, unicode)

    def testClasses(self):
        self.assertArgIsBOOL(NSPreferencePane.replyToShouldUnselect_, 0)
        self.assertResultIsBOOL(NSPreferencePane.autoSaveTextFields)
        self.assertResultIsBOOL(NSPreferencePane.isSelected)

if __name__ == "__main__":
    main()
