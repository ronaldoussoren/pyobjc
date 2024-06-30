from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXTechnology(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsTypedEnum(Accessibility.AXTechnology, str)

        self.assertIsInstance(Accessibility.AXTechnologyVoiceOver, str)
        self.assertIsInstance(Accessibility.AXTechnologySwitchControl, str)
        self.assertIsInstance(Accessibility.AXTechnologyVoiceControl, str)
        self.assertIsInstance(Accessibility.AXTechnologyFullKeyboardAccess, str)
        self.assertIsInstance(Accessibility.AXTechnologySpeakScreen, str)
        self.assertIsInstance(Accessibility.AXTechnologyAutomation, str)
        self.assertIsInstance(Accessibility.AXTechnologyHoverText, str)
        self.assertIsInstance(Accessibility.AXTechnologyZoom, str)
