import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAppleMenuItem(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsTypedEnum(AutomaticAssessmentConfiguration.AEAppleMenuItem, str)
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemAboutThisMac, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemAppStore, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemForceQuit, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemLocation, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemLockScreen, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemLogout, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemRecent, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemRestart, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemShutDown, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemSleep, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemSystemInformation, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAppleMenuItemSystemSettings, str
        )
