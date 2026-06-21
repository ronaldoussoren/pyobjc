import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEMenuBarItem(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsTypedEnum(AutomaticAssessmentConfiguration.AEMenuBarItem, str)
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEMenuBarItemBattery, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEMenuBarItemBluetooth, str
        )
        self.assertIsInstance(AutomaticAssessmentConfiguration.AEMenuBarItemClock, str)
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEMenuBarItemDisplays, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEMenuBarItemKeyboard, str
        )
        self.assertIsInstance(AutomaticAssessmentConfiguration.AEMenuBarItemVolume, str)
        self.assertIsInstance(AutomaticAssessmentConfiguration.AEMenuBarItemWifi, str)
