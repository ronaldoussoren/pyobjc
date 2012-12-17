
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCIFilter (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIAttributeFilterName, unicode)
        self.assertIsInstance(kCIAttributeFilterDisplayName, unicode)
        self.assertIsInstance(kCIAttributeFilterCategories, unicode)
        self.assertIsInstance(kCIAttributeClass, unicode)
        self.assertIsInstance(kCIAttributeType, unicode)
        self.assertIsInstance(kCIAttributeMin, unicode)
        self.assertIsInstance(kCIAttributeMax, unicode)
        self.assertIsInstance(kCIAttributeSliderMin, unicode)
        self.assertIsInstance(kCIAttributeSliderMax, unicode)
        self.assertIsInstance(kCIAttributeDefault, unicode)
        self.assertIsInstance(kCIAttributeIdentity, unicode)
        self.assertIsInstance(kCIAttributeName, unicode)
        self.assertIsInstance(kCIAttributeDisplayName, unicode)
        self.assertIsInstance(kCIAttributeTypeTime, unicode)
        self.assertIsInstance(kCIAttributeTypeScalar, unicode)
        self.assertIsInstance(kCIAttributeTypeDistance, unicode)
        self.assertIsInstance(kCIAttributeTypeAngle, unicode)
        self.assertIsInstance(kCIAttributeTypeBoolean, unicode)
        self.assertIsInstance(kCIAttributeTypePosition, unicode)
        self.assertIsInstance(kCIAttributeTypeOffset, unicode)
        self.assertIsInstance(kCIAttributeTypePosition3, unicode)
        self.assertIsInstance(kCIAttributeTypeRectangle, unicode)
        self.assertIsInstance(kCIAttributeTypeOpaqueColor, unicode)
        self.assertIsInstance(kCIAttributeTypeGradient, unicode)
        self.assertIsInstance(kCICategoryDistortionEffect, unicode)
        self.assertIsInstance(kCICategoryGeometryAdjustment, unicode)
        self.assertIsInstance(kCICategoryCompositeOperation, unicode)
        self.assertIsInstance(kCICategoryHalftoneEffect, unicode)
        self.assertIsInstance(kCICategoryColorAdjustment, unicode)
        self.assertIsInstance(kCICategoryColorEffect, unicode)
        self.assertIsInstance(kCICategoryTransition, unicode)
        self.assertIsInstance(kCICategoryTileEffect, unicode)
        self.assertIsInstance(kCICategoryGenerator, unicode)
        self.assertIsInstance(kCICategoryReduction, unicode)
        self.assertIsInstance(kCICategoryGradient, unicode)
        self.assertIsInstance(kCICategoryStylize, unicode)
        self.assertIsInstance(kCICategorySharpen, unicode)
        self.assertIsInstance(kCICategoryBlur, unicode)
        self.assertIsInstance(kCICategoryVideo, unicode)
        self.assertIsInstance(kCICategoryStillImage, unicode)
        self.assertIsInstance(kCICategoryInterlaced, unicode)
        self.assertIsInstance(kCICategoryNonSquarePixels, unicode)
        self.assertIsInstance(kCICategoryHighDynamicRange, unicode)
        self.assertIsInstance(kCICategoryBuiltIn, unicode)
        self.assertIsInstance(kCIApplyOptionExtent, unicode)
        self.assertIsInstance(kCIApplyOptionDefinition, unicode)
        self.assertIsInstance(kCIApplyOptionUserInfo, unicode)






        @min_os_level('10.5')
        def testConstants10_5(self):

            self.assertIsInstance(kCIAttributeDescription, unicode)
            self.assertIsInstance(kCIAttributeReferenceDocumentation, unicode)
            self.assertIsInstance(kCIUIParameterSet, unicode)
            self.assertIsInstance(kCIUISetBasic, unicode)
            self.assertIsInstance(kCIUISetIntermediate, unicode)
            self.assertIsInstance(kCIUISetAdvanced, unicode)
            self.assertIsInstance(kCIUISetDevelopment, unicode)
            self.assertIsInstance(kCIAttributeTypeInteger, unicode)
            self.assertIsInstance(kCIAttributeTypeCount, unicode)
            self.assertIsInstance(kCICategoryFilterGenerator, unicode)
            self.assertIsInstance(kCIOutputImageKey, unicode)
            self.assertIsInstance(kCIInputBackgroundImageKey, unicode)
            self.assertIsInstance(kCIInputImageKey, unicode)
            self.assertIsInstance(kCIInputTimeKey, unicode)
            self.assertIsInstance(kCIInputTransformKey, unicode)
            self.assertIsInstance(kCIInputScaleKey, unicode)
            self.assertIsInstance(kCIInputAspectRatioKey, unicode)
            self.assertIsInstance(kCIInputCenterKey, unicode)
            self.assertIsInstance(kCIInputRadiusKey, unicode)
            self.assertIsInstance(kCIInputAngleKey, unicode)
            self.assertIsInstance(kCIInputRefractionKey, unicode)
            self.assertIsInstance(kCIInputWidthKey, unicode)
            self.assertIsInstance(kCIInputSharpnessKey, unicode)
            self.assertIsInstance(kCIInputIntensityKey, unicode)
            self.assertIsInstance(kCIInputEVKey, unicode)
            self.assertIsInstance(kCIInputSaturationKey, unicode)
            self.assertIsInstance(kCIInputColorKey, unicode)
            self.assertIsInstance(kCIInputBrightnessKey, unicode)
            self.assertIsInstance(kCIInputContrastKey, unicode)
            self.assertIsInstance(kCIInputGradientImageKey, unicode)
            self.assertIsInstance(kCIInputMaskImageKey, unicode)
            self.assertIsInstance(kCIInputShadingImageKey, unicode)
            self.assertIsInstance(kCIInputTargetImageKey, unicode)
            self.assertIsInstance(kCIInputExtentKey, unicode)

    def testMethods(self):
        self.assertIsNullTerminated(CIFilter.apply_)
        self.assertIsNullTerminated(CIFilter.filterWithName_keysAndValues_)


if __name__ == "__main__":
    main()
