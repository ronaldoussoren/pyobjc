from PyObjCTools.TestSupport import TestCase, min_os_level
import ColorSync


class TestColorSyncHeadroomAdaptiveGainCurve(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsInstance(
            ColorSync.kColorSyncHeadroomAdaptiveGainCurveApplicationVersion, str
        )
        self.assertIsInstance(
            ColorSync.kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform, str
        )
        self.assertIsInstance(ColorSync.kColorSyncCustomHDRReferenceWhite, str)
        self.assertIsInstance(ColorSync.kColorSyncHeadroomAdaptiveToneMappingInfo, str)
        self.assertIsInstance(ColorSync.kColorSyncBaselineHeadroomStops, str)
        self.assertIsInstance(ColorSync.kColorSyncHeadroomAdaptiveGainCurveInfo, str)
        self.assertIsInstance(ColorSync.kColorSyncAlternateCurveCount, str)
        self.assertIsInstance(ColorSync.kColorSyncAlternateGainCurveInfo, str)
        self.assertIsInstance(ColorSync.kColorSyncGainCurveChromaticities, str)
        self.assertIsInstance(ColorSync.kColorSyncCommonComponentMixing, str)
        self.assertIsInstance(ColorSync.kColorSyncCommonCurveParameters, str)
        self.assertIsInstance(ColorSync.kColorSyncAlternateCurveHeadroomStops, str)
        self.assertIsInstance(ColorSync.kColorSyncComponentMix, str)
        self.assertIsInstance(ColorSync.kColorSyncComponentCoefficients, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientRed, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientGreen, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientBlue, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientBlue, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientMaxRGB, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientMinRGB, str)
        self.assertIsInstance(ColorSync.kColorSyncCoefficientComponent, str)
        self.assertIsInstance(ColorSync.kColorSyncMaxControlPointIndex, str)
        self.assertIsInstance(ColorSync.kColorSyncInterpolateSlopes, str)
        self.assertIsInstance(ColorSync.kColorSyncControlPointsX, str)
        self.assertIsInstance(ColorSync.kColorSyncControlPointsY, str)
        self.assertIsInstance(ColorSync.kColorSyncControlPointSlopes, str)

    @min_os_level("27.0")
    def test_functions(self):
        self.assertResultIsCFRetained(
            ColorSync.ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveMetadata
        )
        self.assertResultIsCFRetained(
            ColorSync.ColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata
        )
        self.assertResultIsCFRetained(
            ColorSync.ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveInfoDictionary
        )
        self.assertResultIsCFRetained(
            ColorSync.ColorSyncProfileCopyHeadroomAdaptiveGainCurveInfoDictionary
        )
        self.assertResultIsBOOL(
            ColorSync.ColorSyncProfileContainsHeadroomAdaptiveGainCurve
        )
