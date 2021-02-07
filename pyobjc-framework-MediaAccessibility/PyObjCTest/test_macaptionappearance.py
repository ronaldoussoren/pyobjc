import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestMAAudibleMedia(TestCase):
    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(
            MediaAccessibility.kMACaptionAppearanceSettingsChangedNotification, str
        )
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceDomainDefault, 0)
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceDomainUser, 1)

        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceDisplayTypeForcedOnly, 0
        )
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceDisplayTypeAutomatic, 1)
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceDisplayTypeAlwaysOn, 2)

        self.assertEqual(MediaAccessibility.kMACaptionAppearanceBehaviorUseValue, 0)
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceBehaviorUseContentIfAvailable, 1
        )

        self.assertEqual(MediaAccessibility.kMACaptionAppearanceFontStyleDefault, 0)
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceFontStyleMonospacedWithSerif, 1
        )
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceFontStyleProportionalWithSerif, 2
        )
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceFontStyleMonospacedWithoutSerif, 3
        )
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceFontStyleProportionalWithoutSerif, 4
        )
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceFontStyleCasual, 5)
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceFontStyleCursive, 6)
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceFontStyleSmallCapital, 7
        )

        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceTextEdgeStyleUndefined, 0
        )
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceTextEdgeStyleNone, 1)
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceTextEdgeStyleRaised, 2)
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceTextEdgeStyleDepressed, 3
        )
        self.assertEqual(MediaAccessibility.kMACaptionAppearanceTextEdgeStyleUniform, 4)
        self.assertEqual(
            MediaAccessibility.kMACaptionAppearanceTextEdgeStyleDropShadow, 5
        )

        self.assertIsInstance(
            MediaAccessibility.MAMediaCharacteristicDescribesMusicAndSoundForAccessibility,
            str,
        )
        self.assertIsInstance(
            MediaAccessibility.MAMediaCharacteristicTranscribesSpokenDialogForAccessibility,
            str,
        )

    @min_os_level("10.9")
    def test_functions(self):
        self.assertResultHasType(
            MediaAccessibility.MACaptionAppearanceAddSelectedLanguage, objc._C_BOOL
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopySelectedLanguages
        )
        self.assertIsInstance(
            MediaAccessibility.MACaptionAppearanceGetDisplayType, objc.function
        )
        self.assertIsInstance(
            MediaAccessibility.MACaptionAppearanceSetDisplayType, objc.function
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopyForegroundColor
        )
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceCopyForegroundColor, 1
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopyBackgroundColor
        )
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceCopyBackgroundColor, 1
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopyWindowColor
        )
        self.assertArgIsOut(MediaAccessibility.MACaptionAppearanceCopyWindowColor, 1)
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceGetForegroundOpacity, 1
        )
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceGetBackgroundOpacity, 1
        )
        self.assertArgIsOut(MediaAccessibility.MACaptionAppearanceGetWindowOpacity, 1)
        self.assertIsInstance(
            MediaAccessibility.MACaptionAppearanceGetWindowRoundedCornerRadius,
            objc.function,
        )
        self.assertResultIsCFRetained(
            MediaAccessibility.MACaptionAppearanceCopyFontDescriptorForStyle
        )
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceCopyFontDescriptorForStyle, 1
        )
        self.assertArgIsOut(
            MediaAccessibility.MACaptionAppearanceGetRelativeCharacterSize, 1
        )
        self.assertArgIsOut(MediaAccessibility.MACaptionAppearanceGetTextEdgeStyle, 1)

    @min_os_level("10.15")
    def test_functions10_15(self):
        MediaAccessibility.MACaptionAppearanceDidDisplayCaptions
