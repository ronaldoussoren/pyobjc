from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXSettings(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Accessibility.AXSettingsFeature)
        self.assertEqual(
            Accessibility.AXSettingsFeaturePersonalVoiceAllowAppsToRequestToUse, 1
        )
        self.assertEqual(Accessibility.AXSettingsFeatureAllowAppsToAddAudioToCalls, 2)
        self.assertEqual(Accessibility.AXSettingsFeatureAssistiveTouch, 3)
        self.assertEqual(Accessibility.AXSettingsFeatureAssistiveTouchDevices, 4)
        self.assertEqual(Accessibility.AXSettingsFeatureDwellControl, 5)
        self.assertEqual(Accessibility.AXSettingsFeatureCaptionStyles, 6)

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

    @min_os_level("26.1")
    def testConstants26_1(self):
        self.assertIsInstance(
            Accessibility.AXPrefersActionSliderAlternativeDidChangeNotification,
            str,
        )
        self.assertIsInstance(
            Accessibility.AXShowBordersEnabledStatusDidChangeNotification,
            str,
        )

    @min_os_level("26.4")
    def testConstants26_4(self):
        self.assertIsInstance(
            Accessibility.AXReduceHighlightingEffectsEnabledDidChangeNotification,
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

    @min_os_level("26.4")
    def test_functions26_4(self):
        self.assertResultIsBOOL(Accessibility.AXOpenSettingsFeatureIsSupported)
        self.assertResultIsBOOL(Accessibility.AXReduceHighlightingEffectsEnabled)
