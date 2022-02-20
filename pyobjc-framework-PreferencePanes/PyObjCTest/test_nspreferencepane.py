import PreferencePanes
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPreferencePane(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PreferencePanes.NSPreferencePaneUnselectReply)

    def testConstants(self):
        self.assertEqual(PreferencePanes.NSUnselectCancel, 0)
        self.assertEqual(PreferencePanes.NSUnselectNow, 1)
        self.assertEqual(PreferencePanes.NSUnselectLater, 2)

        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneDoUnselectNotification, str
        )
        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneCancelUnselectNotification, str
        )

        self.assertEqual(
            PreferencePanes.kNSPrefPaneHelpMenuInfoPListKey, "NSPrefPaneHelpAnchors"
        )
        self.assertEqual(PreferencePanes.kNSPrefPaneHelpMenuTitleKey, "title")
        self.assertEqual(PreferencePanes.kNSPrefPaneHelpMenuAnchorKey, "anchor")

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuInfoPListKey, str)
        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuTitleKey, str)
        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuAnchorKey, str)

    # @min_os_level('10.12')
    # Added in 10.12, but available before that
    def testConstants10_12(self):
        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneSwitchToPaneNotification, str
        )
        self.assertIsInstance(
            PreferencePanes.NSPreferencePrefPaneIsAvailableNotification, str
        )
        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneUpdateHelpMenuNotification, str
        )

    def testClasses(self):
        self.assertArgIsBOOL(PreferencePanes.NSPreferencePane.replyToShouldUnselect_, 0)
        self.assertResultIsBOOL(PreferencePanes.NSPreferencePane.autoSaveTextFields)
        self.assertResultIsBOOL(PreferencePanes.NSPreferencePane.isSelected)
