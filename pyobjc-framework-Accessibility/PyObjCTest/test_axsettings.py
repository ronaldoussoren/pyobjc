from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXSettings(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Accessibility.AXSettingsFeature)
        self.assertEqual(
            Accessibility.AXSettingsFeaturePersonalVoiceAllowAppsToRequestToUse, 1
        )
        self.assertEqual(Accessibility.AXSettingsFeatureAllowAppsToAddAudioToCalls, 2)

    @min_os_level("14.0")
    def testConstants(self):
        self.assertIsInstance(
            Accessibility.AXAnimatedImagesEnabledDidChangeNotification, str
        )
        self.assertIsInstance(
            Accessibility.AXPrefersHorizontalTextLayoutDidChangeNotification, str
        )

    @min_os_level("15.0")
    def testConstants15_0(self):
        self.assertIsInstance(
            Accessibility.AXPrefersNonBlinkingTextInsertionIndicatorDidChangeNotification,
            str,
        )

    @min_os_level("14.0")
    def test_functions(self):
        self.assertResultIsBOOL(Accessibility.AXAnimatedImagesEnabled)
        self.assertResultIsBOOL(Accessibility.AXPrefersHorizontalTextLayout)

    @min_os_level("15.0")
    def test_functions15_0(self):
        self.assertResultIsBOOL(Accessibility.AXAssistiveAccessEnabled)
        self.assertResultIsBOOL(
            Accessibility.AXPrefersNonBlinkingTextInsertionIndicator
        )

        self.assertArgIsBlock(Accessibility.AXOpenSettingsFeature, 1, b"v@")
