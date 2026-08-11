from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXAttributeConstants(TestCase):
    @min_os_level("27.0")
    def test_constants27(self):
        self.assertIsInstance(Accessibility.AXSpeechAttributeSSML, str)
