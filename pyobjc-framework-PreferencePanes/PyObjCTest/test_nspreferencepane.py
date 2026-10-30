import PreferencePanes
from PyObjCTools.TestSupport import TestCase


class TestNSPreferencePane(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PreferencePanes.NSPreferencePaneUnselectReply)
        self.assertEqual(PreferencePanes.NSUnselectCancel, 0)
        self.assertEqual(PreferencePanes.NSUnselectNow, 1)
        self.assertEqual(PreferencePanes.NSUnselectLater, 2)

    def test_constants(self):
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

        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuInfoPListKey, str)
        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuTitleKey, str)
        self.assertIsInstance(PreferencePanes.NSPrefPaneHelpMenuAnchorKey, str)

        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneSwitchToPaneNotification, str
        )
        self.assertIsInstance(
            PreferencePanes.NSPreferencePrefPaneIsAvailableNotification, str
        )
        self.assertIsInstance(
            PreferencePanes.NSPreferencePaneUpdateHelpMenuNotification, str
        )

    def test_methods(self):
        self.assertArgIsBOOL(PreferencePanes.NSPreferencePane.replyToShouldUnselect_, 0)
        self.assertResultIsBOOL(PreferencePanes.NSPreferencePane.autoSaveTextFields)
        self.assertResultIsBOOL(PreferencePanes.NSPreferencePane.isSelected)
