
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontDescriptor (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(CTFontDescriptorRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessIsInstance(kCTFontNameAttribute, unicode)
        self.failUnlessIsInstance(kCTFontDisplayNameAttribute, unicode)
        self.failUnlessIsInstance(kCTFontFamilyNameAttribute, unicode)
        self.failUnlessIsInstance(kCTFontStyleNameAttribute, unicode)
        self.failUnlessIsInstance(kCTFontTraitsAttribute, unicode)
        self.failUnlessIsInstance(kCTFontVariationAttribute, unicode)
        self.failUnlessIsInstance(kCTFontSizeAttribute, unicode)
        self.failUnlessIsInstance(kCTFontMatrixAttribute, unicode)
        self.failUnlessIsInstance(kCTFontCascadeListAttribute, unicode)
        self.failUnlessIsInstance(kCTFontCharacterSetAttribute, unicode)
        self.failUnlessIsInstance(kCTFontLanguagesAttribute, unicode)
        self.failUnlessIsInstance(kCTFontBaselineAdjustAttribute, unicode)
        self.failUnlessIsInstance(kCTFontMacintoshEncodingsAttribute, unicode)
        self.failUnlessIsInstance(kCTFontFeaturesAttribute, unicode)
        self.failUnlessIsInstance(kCTFontFeatureSettingsAttribute, unicode)
        self.failUnlessIsInstance(kCTFontFixedAdvanceAttribute, unicode)
        self.failUnlessIsInstance(kCTFontOrientationAttribute, unicode)

        self.failUnlessEqual(kCTFontDefaultOrientation, 0)
        self.failUnlessEqual(kCTFontHorizontalOrientation, 1)
        self.failUnlessEqual(kCTFontVerticalOrientation, 2)

    def testFunctions(self):

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateWithAttributes)
        v = CTFontDescriptorCreateWithAttributes(
                {
                    kCTFontNameAttribute: u"Optima Bold",
                    kCTFontSizeAttribute: u"23.4",
                })
        self.failUnlessIsInstance(v, CTFontDescriptorRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateWithNameAndSize)
        v = CTFontDescriptorCreateWithNameAndSize(u"Optima Bold", 15.0)
        self.failUnlessIsInstance(v, CTFontDescriptorRef)
        descriptor = v

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateCopyWithAttributes)
        v = CTFontDescriptorCreateCopyWithAttributes(v, {
            "foo": "bar",
        })
        self.failUnlessIsInstance(v, CTFontDescriptorRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateCopyWithVariation)
        v = CTFontDescriptorCreateCopyWithVariation(v, 0, 5.0)
        self.failUnlessIsInstance(v, CTFontDescriptorRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateCopyWithFeature)
        v = CTFontDescriptorCreateCopyWithFeature(v, 0, 6)
        self.failUnlessIsInstance(v, CTFontDescriptorRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateMatchingFontDescriptors)
        v = CTFontDescriptorCreateMatchingFontDescriptors(descriptor, None)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCreateMatchingFontDescriptor)
        v = CTFontDescriptorCreateMatchingFontDescriptor(descriptor, None)
        self.failUnlessIsInstance(v, CTFontDescriptorRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCopyAttributes)
        v = CTFontDescriptorCopyAttributes(descriptor)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessResultIsCFRetained(CTFontDescriptorCopyAttribute)
        v = CTFontDescriptorCopyAttribute(descriptor, kCTFontNameAttribute)
        self.failUnlessEqual(v, u"Optima Bold")

        self.failUnlessResultIsCFRetained(CTFontDescriptorCopyLocalizedAttribute)
        self.failUnlessArgIsOut(CTFontDescriptorCopyLocalizedAttribute, 2)
        v, l = CTFontDescriptorCopyLocalizedAttribute(descriptor, kCTFontDisplayNameAttribute, None)
        self.failUnlessIsInstance(v, unicode)
        self.failUnlessIsInstance(l, unicode)

        v = CTFontDescriptorGetTypeID()
        self.failUnlessIsInstance(v, (int, long))





if __name__ == "__main__":
    main()
