
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontDescriptor (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTFontDescriptorRef, objc.objc_class)

    def testConstants(self):
        self.assertIsInstance(kCTFontNameAttribute, unicode)
        self.assertIsInstance(kCTFontDisplayNameAttribute, unicode)
        self.assertIsInstance(kCTFontFamilyNameAttribute, unicode)
        self.assertIsInstance(kCTFontStyleNameAttribute, unicode)
        self.assertIsInstance(kCTFontTraitsAttribute, unicode)
        self.assertIsInstance(kCTFontVariationAttribute, unicode)
        self.assertIsInstance(kCTFontSizeAttribute, unicode)
        self.assertIsInstance(kCTFontMatrixAttribute, unicode)
        self.assertIsInstance(kCTFontCascadeListAttribute, unicode)
        self.assertIsInstance(kCTFontCharacterSetAttribute, unicode)
        self.assertIsInstance(kCTFontLanguagesAttribute, unicode)
        self.assertIsInstance(kCTFontBaselineAdjustAttribute, unicode)
        self.assertIsInstance(kCTFontMacintoshEncodingsAttribute, unicode)
        self.assertIsInstance(kCTFontFeaturesAttribute, unicode)
        self.assertIsInstance(kCTFontFeatureSettingsAttribute, unicode)
        self.assertIsInstance(kCTFontFixedAdvanceAttribute, unicode)
        self.assertIsInstance(kCTFontOrientationAttribute, unicode)

        self.assertEqual(kCTFontDefaultOrientation, 0)
        self.assertEqual(kCTFontHorizontalOrientation, 1)
        self.assertEqual(kCTFontVerticalOrientation, 2)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCTFontURLAttribute, unicode)
        self.assertIsInstance(kCTFontFormatAttribute, unicode)
        self.assertIsInstance(kCTFontRegistrationScopeAttribute, unicode)
        self.assertIsInstance(kCTFontPriorityAttribute, unicode)
        self.assertIsInstance(kCTFontEnabledAttribute, unicode)
        self.assertIsInstance(kCTFontEnabledAttribute, unicode)

        self.assertEqual(kCTFontFormatUnrecognized, 0)
        self.assertEqual(kCTFontFormatOpenTypePostScript, 1)
        self.assertEqual(kCTFontFormatOpenTypeTrueType, 2)
        self.assertEqual(kCTFontFormatTrueType, 3)
        self.assertEqual(kCTFontFormatPostScript, 4)
        self.assertEqual(kCTFontFormatBitmap, 5)

        self.assertEqual(kCTFontPrioritySystem,  10000)
        self.assertEqual(kCTFontPriorityNetwork,  20000)
        self.assertEqual(kCTFontPriorityComputer,  30000)
        self.assertEqual(kCTFontPriorityUser,  40000)
        self.assertEqual(kCTFontPriorityDynamic,  50000)
        self.assertEqual(kCTFontPriorityProcess,  60000)



    def testFunctions(self):

        self.assertResultIsCFRetained(CTFontDescriptorCreateWithAttributes)
        v = CTFontDescriptorCreateWithAttributes(
                {
                    kCTFontNameAttribute: u"Optima Bold",
                    kCTFontSizeAttribute: u"23.4",
                })
        self.assertIsInstance(v, CTFontDescriptorRef)

        self.assertResultIsCFRetained(CTFontDescriptorCreateWithNameAndSize)
        v = CTFontDescriptorCreateWithNameAndSize(u"Optima Bold", 15.0)
        self.assertIsInstance(v, CTFontDescriptorRef)
        descriptor = v

        self.assertResultIsCFRetained(CTFontDescriptorCreateCopyWithAttributes)
        v = CTFontDescriptorCreateCopyWithAttributes(v, {
            "foo": "bar",
        })
        self.assertIsInstance(v, CTFontDescriptorRef)

        self.assertResultIsCFRetained(CTFontDescriptorCreateCopyWithVariation)
        v = CTFontDescriptorCreateCopyWithVariation(v, 0, 5.0)
        self.assertIsInstance(v, CTFontDescriptorRef)

        self.assertResultIsCFRetained(CTFontDescriptorCreateCopyWithFeature)
        v = CTFontDescriptorCreateCopyWithFeature(v, 0, 6)
        self.assertIsInstance(v, CTFontDescriptorRef)

        self.assertResultIsCFRetained(CTFontDescriptorCreateMatchingFontDescriptors)
        v = CTFontDescriptorCreateMatchingFontDescriptors(descriptor, None)
        self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(CTFontDescriptorCreateMatchingFontDescriptor)
        v = CTFontDescriptorCreateMatchingFontDescriptor(descriptor, None)
        self.assertIsInstance(v, CTFontDescriptorRef)

        self.assertResultIsCFRetained(CTFontDescriptorCopyAttributes)
        v = CTFontDescriptorCopyAttributes(descriptor)
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertResultIsCFRetained(CTFontDescriptorCopyAttribute)
        v = CTFontDescriptorCopyAttribute(descriptor, kCTFontNameAttribute)
        self.assertEqual(v, u"Optima Bold")

        self.assertResultIsCFRetained(CTFontDescriptorCopyLocalizedAttribute)
        self.assertArgIsOut(CTFontDescriptorCopyLocalizedAttribute, 2)
        v, l = CTFontDescriptorCopyLocalizedAttribute(descriptor, kCTFontDisplayNameAttribute, None)
        self.assertIsInstance(v, unicode)
        self.assertIsInstance(l, (unicode, type(None)))

        v = CTFontDescriptorGetTypeID()
        self.assertIsInstance(v, (int, long))





if __name__ == "__main__":
    main()
