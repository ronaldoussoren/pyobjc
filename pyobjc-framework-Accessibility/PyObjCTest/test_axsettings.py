from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXSettings(TestCase):
    @min_os_level("14.0")
    def testConstants(self):
        self.assertIsInstance(
            Accessibility.AXAnimatedImagesEnabledDidChangeNotification, str
        )
        self.assertIsInstance(
            Accessibility.AXPrefersHorizontalTextLayoutDidChangeNotification, str
        )

    @min_os_level("14.0")
    def test_functions(self):
        self.assertResultIsBOOL(Accessibility.AXAnimatedImagesEnabled)
        self.assertResultIsBOOL(Accessibility.AXPrefersHorizontalTextLayout)
