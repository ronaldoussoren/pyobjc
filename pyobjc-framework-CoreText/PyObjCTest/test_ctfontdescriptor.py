import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTFontDescriptor(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTFontDescriptorRef, objc.objc_class)

    def testConstants(self):
        self.assertIsInstance(CoreText.kCTFontNameAttribute, str)
        self.assertIsInstance(CoreText.kCTFontDisplayNameAttribute, str)
        self.assertIsInstance(CoreText.kCTFontFamilyNameAttribute, str)
        self.assertIsInstance(CoreText.kCTFontStyleNameAttribute, str)
        self.assertIsInstance(CoreText.kCTFontTraitsAttribute, str)
        self.assertIsInstance(CoreText.kCTFontVariationAttribute, str)
        self.assertIsInstance(CoreText.kCTFontSizeAttribute, str)
        self.assertIsInstance(CoreText.kCTFontMatrixAttribute, str)
        self.assertIsInstance(CoreText.kCTFontCascadeListAttribute, str)
        self.assertIsInstance(CoreText.kCTFontCharacterSetAttribute, str)
        self.assertIsInstance(CoreText.kCTFontLanguagesAttribute, str)
        self.assertIsInstance(CoreText.kCTFontBaselineAdjustAttribute, str)
        self.assertIsInstance(CoreText.kCTFontMacintoshEncodingsAttribute, str)
        self.assertIsInstance(CoreText.kCTFontFeaturesAttribute, str)
        self.assertIsInstance(CoreText.kCTFontFeatureSettingsAttribute, str)
        self.assertIsInstance(CoreText.kCTFontFixedAdvanceAttribute, str)
        self.assertIsInstance(CoreText.kCTFontOrientationAttribute, str)

        self.assertEqual(CoreText.kCTFontDefaultOrientation, 0)
        self.assertEqual(CoreText.kCTFontHorizontalOrientation, 1)
        self.assertEqual(CoreText.kCTFontVerticalOrientation, 2)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreText.kCTFontURLAttribute, str)
        self.assertIsInstance(CoreText.kCTFontFormatAttribute, str)
        self.assertIsInstance(CoreText.kCTFontRegistrationScopeAttribute, str)
        self.assertIsInstance(CoreText.kCTFontPriorityAttribute, str)
        self.assertIsInstance(CoreText.kCTFontEnabledAttribute, str)
        self.assertIsInstance(CoreText.kCTFontEnabledAttribute, str)

        self.assertEqual(CoreText.kCTFontFormatUnrecognized, 0)
        self.assertEqual(CoreText.kCTFontFormatOpenTypePostScript, 1)
        self.assertEqual(CoreText.kCTFontFormatOpenTypeTrueType, 2)
        self.assertEqual(CoreText.kCTFontFormatTrueType, 3)
        self.assertEqual(CoreText.kCTFontFormatPostScript, 4)
        self.assertEqual(CoreText.kCTFontFormatBitmap, 5)

        self.assertEqual(CoreText.kCTFontPrioritySystem, 10000)
        self.assertEqual(CoreText.kCTFontPriorityNetwork, 20000)
        self.assertEqual(CoreText.kCTFontPriorityComputer, 30000)
        self.assertEqual(CoreText.kCTFontPriorityUser, 40000)
        self.assertEqual(CoreText.kCTFontPriorityDynamic, 50000)
        self.assertEqual(CoreText.kCTFontPriorityProcess, 60000)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(CoreText.kCTFontOrientationDefault, 0)
        self.assertEqual(CoreText.kCTFontOrientationHorizontal, 1)
        self.assertEqual(CoreText.kCTFontOrientationVertical, 2)
        self.assertEqual(
            CoreText.kCTFontDefaultOrientation, CoreText.kCTFontOrientationDefault
        )
        self.assertEqual(
            CoreText.kCTFontHorizontalOrientation, CoreText.kCTFontOrientationHorizontal
        )
        self.assertEqual(
            CoreText.kCTFontVerticalOrientation, CoreText.kCTFontOrientationVertical
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDidBegin, 0)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDidFinish, 1)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingWillBeginQuerying, 2)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingStalled, 3)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingWillBeginDownloading, 4)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDownloading, 5)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDidFinishDownloading, 6)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDidMatch, 7)
        self.assertEqual(CoreText.kCTFontDescriptorMatchingDidFailWithError, 8)

        self.assertIsInstance(CoreText.kCTFontDownloadableAttribute, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingSourceDescriptor, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingDescriptors, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingResult, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingPercentage, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingCurrentAssetSize, str)
        self.assertIsInstance(
            CoreText.kCTFontDescriptorMatchingTotalDownloadedSize, str
        )
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingTotalAssetSize, str)
        self.assertIsInstance(CoreText.kCTFontDescriptorMatchingError, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CoreText.kCTFontOpticalSizeAttribute, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreText.kCTFontDownloadedAttribute, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreText.kCTFontVariationAxesAttribute, str)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        CoreText.CTFontDescriptorProgressHandler = (
            objc._C_BOOL + objc._C_UINT + objc._C_ID
        )
        self.assertResultHasType(
            CoreText.CTFontDescriptorMatchFontDescriptorsWithProgressHandler,
            objc._C_BOOL,
        )
        self.assertArgIsBlock(
            CoreText.CTFontDescriptorMatchFontDescriptorsWithProgressHandler,
            2,
            CoreText.CTFontDescriptorProgressHandler,
        )

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateCopyWithFamily)
        self.assertResultIsCFRetained(
            CoreText.CTFontDescriptorCreateCopyWithSymbolicTraits
        )

    def testFunctions(self):

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateWithAttributes)
        v = CoreText.CTFontDescriptorCreateWithAttributes(
            {
                CoreText.kCTFontNameAttribute: "Optima Bold",
                CoreText.kCTFontSizeAttribute: "23.4",
            }
        )
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateWithNameAndSize)
        v = CoreText.CTFontDescriptorCreateWithNameAndSize("Optima Bold", 15.0)
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)
        descriptor = v

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateCopyWithAttributes)
        v = CoreText.CTFontDescriptorCreateCopyWithAttributes(v, {"foo": "bar"})
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateCopyWithVariation)
        v = CoreText.CTFontDescriptorCreateCopyWithVariation(v, 0, 5.0)
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCreateCopyWithFeature)
        v = CoreText.CTFontDescriptorCreateCopyWithFeature(v, 0, 6)
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)

        self.assertResultIsCFRetained(
            CoreText.CTFontDescriptorCreateMatchingFontDescriptors
        )
        v = CoreText.CTFontDescriptorCreateMatchingFontDescriptors(descriptor, None)
        self.assertIsInstance(v, CoreText.CFArrayRef)

        self.assertResultIsCFRetained(
            CoreText.CTFontDescriptorCreateMatchingFontDescriptor
        )
        v = CoreText.CTFontDescriptorCreateMatchingFontDescriptor(descriptor, None)
        self.assertIsInstance(v, CoreText.CTFontDescriptorRef)

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCopyAttributes)
        v = CoreText.CTFontDescriptorCopyAttributes(descriptor)
        self.assertIsInstance(v, CoreText.CFDictionaryRef)

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCopyAttribute)
        v = CoreText.CTFontDescriptorCopyAttribute(
            descriptor, CoreText.kCTFontNameAttribute
        )
        self.assertEqual(v, "Optima Bold")

        self.assertResultIsCFRetained(CoreText.CTFontDescriptorCopyLocalizedAttribute)
        self.assertArgIsOut(CoreText.CTFontDescriptorCopyLocalizedAttribute, 2)
        v, locattr = CoreText.CTFontDescriptorCopyLocalizedAttribute(
            descriptor, CoreText.kCTFontDisplayNameAttribute, None
        )
        self.assertIsInstance(v, str)
        self.assertIsInstance(locattr, (str, type(None)))

        v = CoreText.CTFontDescriptorGetTypeID()
        self.assertIsInstance(v, int)
