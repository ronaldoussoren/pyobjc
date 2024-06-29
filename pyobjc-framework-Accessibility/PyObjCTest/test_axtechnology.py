from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXTechnology(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsTypedEnum(Accessibility.AXTechnology, str)

        self.assertEqual(Accessibility.AXTechnologyVoiceOver, str)
        self.assertEqual(Accessibility.AXTechnologySwitchControl, str)
        self.assertEqual(Accessibility.AXTechnologyVoiceControl, str)
        self.assertEqual(Accessibility.AXTechnologyFullKeyboardAccess, str)
        self.assertEqual(Accessibility.AXTechnologySpeakScreen, str)
        self.assertEqual(Accessibility.AXTechnologyAutomation, str)
        self.assertEqual(Accessibility.AXTechnologyHoverText, str)
        self.assertEqual(Accessibility.AXTechnologyZoom, str)
