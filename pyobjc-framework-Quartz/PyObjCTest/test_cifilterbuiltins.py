from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Quartz
import objc


class TestCIBuiltinFilterHelper(Quartz.NSObject):
    def periodicity(self):
        return 1

    def setPeriodicity_(self, a):
        pass

    def highLimit(self):
        return 1

    def setHighLimit_(self, a):
        pass

    def lowLimit(self):
        return 1

    def setLowLimit_(self, a):
        pass

    def passes(self):
        return 1

    def setPasses_(self, a):
        pass

    def EV(self):
        return 1

    def NRNoiseLevel(self):
        return 1

    def NRSharpness(self):
        return 1

    def acuteAngle(self):
        return 1

    def alwaysSpecifyCompaction(self):
        return 1

    def amount(self):
        return 1

    def angle(self):
        return 1

    def aspectRatio(self):
        return 1

    def barOffset(self):
        return 1

    def barcodeHeight(self):
        return 1

    def bias(self):
        return 1

    def bottomHeight(self):
        return 1

    def bottomLeft(self):
        return 1

    def bottomRight(self):
        return 1

    def breakpoint0(self):
        return 1

    def breakpoint1(self):
        return 1

    def brightness(self):
        return 1

    def center(self):
        return 1

    def centerStretchAmount(self):
        return 1

    def count(self):
        return 1

    def closeness1(self):
        return 1

    def closeness2(self):
        return 1

    def closeness3(self):
        return 1

    def compactStyle(self):
        return 1

    def compactionMode(self):
        return 1

    def compression(self):
        return 1

    def cropAmount(self):
        return 1

    def pitch(self):
        return 1

    def concentration(self):
        return 1

    def contrast(self):
        return 1

    def contrast1(self):
        return 1

    def contrast2(self):
        return 1

    def contrast3(self):
        return 1

    def correctionLevel(self):
        return 1

    def crop(self):
        return 1

    def crossAngle(self):
        return 1

    def crossOpacity(self):
        return 1

    def crossScale(self):
        return 1

    def crossWidth(self):
        return 1

    def cubeDimension(self):
        return 1

    def dataColumns(self):
        return 1

    def decay(self):
        return 1

    def dither(self):
        return 1

    def edgeIntensity(self):
        return 1

    def epsilon(self):
        return 1

    def extent(self):
        return 1

    def fadeThreshold(self):
        return 1

    def falloff(self):
        return 1

    def flipYTiles(self):
        return 1

    def focalLength(self):
        return 1

    def foldShadowAmount(self):
        return 1

    def fontSize(self):
        return 1

    def grayComponentReplacement(self):
        return 1

    def growAmount(self):
        return 1

    def haloOverlap(self):
        return 1

    def haloRadius(self):
        return 1

    def haloWidth(self):
        return 1

    def headIndex(self):
        return 1

    def height(self):
        return 1

    def highlightAmount(self):
        return 1

    def intensity(self):
        return 1

    def insetPoint0(self):
        return 1

    def insetPoint1(self):
        return 1

    def layers(self):
        return 1

    def levels(self):
        return 1

    def lumaSigma(self):
        return 1

    def maxHeight(self):
        return 1

    def maxStriationRadius(self):
        return 1

    def maxWidth(self):
        return 1

    def minHeight(self):
        return 1

    def minWidth(self):
        return 1

    def neutral(self):
        return 1

    def noiseLevel(self):
        return 1

    def numberOfFolds(self):
        return 1

    def opacity(self):
        return 1

    def parameterB(self):
        return 1

    def parameterC(self):
        return 1

    def perceptual(self):
        return 1

    def point(self):
        return 1

    def point0(self):
        return 1

    def point1(self):
        return 1

    def point2(self):
        return 1

    def point3(self):
        return 1

    def point4(self):
        return 1

    def power(self):
        return 1

    def preferredAspectRatio(self):
        return 1

    def quietSpace(self):
        return 1

    def radius(self):
        return 1

    def radius0(self):
        return 1

    def radius1(self):
        return 1

    def refraction(self):
        return 1

    def ringAmount(self):
        return 1

    def ringSize(self):
        return 1

    def rotation(self):
        return 1

    def rows(self):
        return 1

    def saturation(self):
        return 1

    def scale(self):
        return 1

    def scaleFactor(self):
        return 1

    def shadowAmount(self):
        return 1

    def shadowDensity(self):
        return 1

    def shadowExtent(self):
        return 1

    def shadowOffset(self):
        return 1

    def shadowRadius(self):
        return 1

    def shadowSize(self):
        return 1

    def sharpness(self):
        return 1

    def size(self):
        return 1

    def softmaxNormalization(self):
        return 1

    def softness(self):
        return 1

    def spatialSigma(self):
        return 1

    def strands(self):
        return 1

    def striationContrast(self):
        return 1

    def striationStrength(self):
        return 1

    def sunRadius(self):
        return 1

    def targetNeutral(self):
        return 1

    def threshold(self):
        return 1

    def time(self):
        return 1

    def topLeft(self):
        return 1

    def topRight(self):
        return 1

    def transform(self):
        return 1

    def underColorRemoval(self):
        return 1

    def unsharpMaskIntensity(self):
        return 1

    def unsharpMaskRadius(self):
        return 1

    def value(self):
        return 1

    def width(self):
        return 1

    def yaw(self):
        return 1

    def roll(self):
        return 1

    def zoom(self):
        return 1

    def setEV_(self, a):
        pass

    def setYaw_(self, a):
        pass

    def setRoll_(self, a):
        pass

    def setPitch_(self, a):
        pass

    def setCompression_(self, a):
        pass

    def setCropAmount_(self, a):
        pass

    def setCenterStretchAmount_(self, a):
        pass

    def setShadowOffset_(self, a):
        pass

    def setStrands_(self, a):
        pass

    def setNRNoiseLevel_(self, a):
        pass

    def setNRSharpness_(self, a):
        pass

    def setAcuteAngle_(self, a):
        pass

    def setAlwaysSpecifyCompaction_(self, a):
        pass

    def setAmount_(self, a):
        pass

    def setAngle_(self, a):
        pass

    def setAspectRatio_(self, a):
        pass

    def setBarOffset_(self, a):
        pass

    def setBarcodeHeight_(self, a):
        pass

    def setBias_(self, a):
        pass

    def setBottomHeight_(self, a):
        pass

    def setBottomLeft_(self, a):
        pass

    def setBottomRight_(self, a):
        pass

    def setBreakpoint0_(self, a):
        pass

    def setBreakpoint1_(self, a):
        pass

    def setBrightness_(self, a):
        pass

    def setCenter_(self, a):
        pass

    def setCount_(self, a):
        pass

    def setCloseness1_(self, a):
        pass

    def setCloseness2_(self, a):
        pass

    def setCloseness3_(self, a):
        pass

    def setCompactStyle_(self, a):
        pass

    def setCompactionMode_(self, a):
        pass

    def setcompression_(self, a):
        pass

    def setConcentration_(self, a):
        pass

    def setContrast_(self, a):
        pass

    def setContrast1_(self, a):
        pass

    def setContrast2_(self, a):
        pass

    def setContrast3_(self, a):
        pass

    def setCorrectionLevel_(self, a):
        pass

    def setCrop_(self, a):
        pass

    def setCrossAngle_(self, a):
        pass

    def setCrossOpacity_(self, a):
        pass

    def setCrossScale_(self, a):
        pass

    def setCrossWidth_(self, a):
        pass

    def setCubeDimension_(self, a):
        pass

    def setDataColumns_(self, a):
        pass

    def setDecay_(self, a):
        pass

    def setDither_(self, a):
        pass

    def setDdgeIntensity_(self, a):
        pass

    def setEpsilon_(self, a):
        pass

    def setEdgeIntensity_(self, a):
        pass

    def setExtent_(self, a):
        pass

    def setFadeThreshold_(self, a):
        pass

    def setFalloff_(self, a):
        pass

    def setFlipYTiles_(self, a):
        pass

    def setFocalLength_(self, a):
        pass

    def setFoldShadowAmount_(self, a):
        pass

    def setFontSize_(self, a):
        pass

    def setGrayComponentReplacement_(self, a):
        pass

    def setGrowAmount_(self, a):
        pass

    def setHaloOverlap_(self, a):
        pass

    def setHaloRadius_(self, a):
        pass

    def setHaloWidth_(self, a):
        pass

    def setHeadIndex_(self, a):
        pass

    def setHeight_(self, a):
        pass

    def setHighlightAmount_(self, a):
        pass

    def setIntensity_(self, a):
        pass

    def setInsetPoint0_(self, a):
        pass

    def setInsetPoint1_(self, a):
        pass

    def setLayers_(self, a):
        pass

    def setLevels_(self, a):
        pass

    def setLumaSigma_(self, a):
        pass

    def setMaxHeight_(self, a):
        pass

    def setMaxStriationRadius_(self, a):
        pass

    def setMaxWidth_(self, a):
        pass

    def setMinHeight_(self, a):
        pass

    def setMinWidth_(self, a):
        pass

    def setNeutral_(self, a):
        pass

    def setNoiseLevel_(self, a):
        pass

    def setNumberOfFolds_(self, a):
        pass

    def setOpacity_(self, a):
        pass

    def setParameterB_(self, a):
        pass

    def setParameterC_(self, a):
        pass

    def setPerceptual_(self, a):
        pass

    def setPoint_(self, a):
        pass

    def setPoint0_(self, a):
        pass

    def setPoint1_(self, a):
        pass

    def setPoint2_(self, a):
        pass

    def setPoint3_(self, a):
        pass

    def setPoint4_(self, a):
        pass

    def setPower_(self, a):
        pass

    def setPreferredAspectRatio_(self, a):
        pass

    def setQuietSpace_(self, a):
        pass

    def setRadius_(self, a):
        pass

    def setRadius0_(self, a):
        pass

    def setRadius1_(self, a):
        pass

    def setRefraction_(self, a):
        pass

    def setRingAmount_(self, a):
        pass

    def setRingSize_(self, a):
        pass

    def setRotation_(self, a):
        pass

    def setRows_(self, a):
        pass

    def setSaturation_(self, a):
        pass

    def setScale_(self, a):
        pass

    def setScaleFactor_(self, a):
        pass

    def setShadowAmount_(self, a):
        pass

    def setShadowDensity_(self, a):
        pass

    def setShadowExtent_(self, a):
        pass

    def setshadowOffset_(self, a):
        pass

    def setShadowRadius_(self, a):
        pass

    def setShadowSize_(self, a):
        pass

    def setSharpness_(self, a):
        pass

    def setSize_(self, a):
        pass

    def setSoftmaxNormalization_(self, a):
        pass

    def setSoftness_(self, a):
        pass

    def setSpatialSigma_(self, a):
        pass

    def setStriationContrast_(self, a):
        pass

    def setStriationStrength_(self, a):
        pass

    def setSunRadius_(self, a):
        pass

    def setTargetNeutral_(self, a):
        pass

    def setThreshold_(self, a):
        pass

    def setTime_(self, a):
        pass

    def setTopLeft_(self, a):
        pass

    def setTopRight_(self, a):
        pass

    def setTransform_(self, a):
        pass

    def setUnderColorRemoval_(self, a):
        pass

    def setUnsharpMaskIntensity_(self, a):
        return 1

    def setUnsharpMaskRadius_(self, a):
        return 1

    def setValue_(self, a):
        return 1

    def setWidth_(self, a):
        return 1

    def setZoom_(self, a):
        return 1


class TestCIFilterBuiltins(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("CIGaussianGradient")
        objc.protocolNamed("CIHueSaturationValueGradient")
        objc.protocolNamed("CILinearGradient")
        objc.protocolNamed("CIRadialGradient")
        objc.protocolNamed("CISmoothLinearGradient")
        objc.protocolNamed("CISharpenLuminance")
        objc.protocolNamed("CIUnsharpMask")
        objc.protocolNamed("CICircularScreen")
        objc.protocolNamed("CICMYKHalftone")
        objc.protocolNamed("CIDotScreen")
        objc.protocolNamed("CIHatchedScreen")
        objc.protocolNamed("CILineScreen")
        objc.protocolNamed("CIBicubicScaleTransform")
        objc.protocolNamed("CIFourCoordinateGeometryFilter")
        objc.protocolNamed("CIEdgePreserveUpsample")
        objc.protocolNamed("CIKeystoneCorrectionCombined")
        objc.protocolNamed("CIKeystoneCorrectionHorizontal")
        objc.protocolNamed("CIKeystoneCorrectionVertical")
        objc.protocolNamed("CILanczosScaleTransform")
        objc.protocolNamed("CIPerspectiveCorrection")
        objc.protocolNamed("CIPerspectiveRotate")
        objc.protocolNamed("CIPerspectiveTransform")
        objc.protocolNamed("CIPerspectiveTransformWithExtent")
        objc.protocolNamed("CIStraighten")
        objc.protocolNamed("CITransitionFilter")
        objc.protocolNamed("CIAccordionFoldTransition")
        objc.protocolNamed("CIBarsSwipeTransition")
        objc.protocolNamed("CICopyMachineTransition")
        objc.protocolNamed("CIDisintegrateWithMaskTransition")
        objc.protocolNamed("CIDissolveTransition")
        objc.protocolNamed("CIFlashTransition")
        objc.protocolNamed("CIModTransition")
        objc.protocolNamed("CIPageCurlTransition")
        objc.protocolNamed("CIPageCurlWithShadowTransition")
        objc.protocolNamed("CIRippleTransition")
        objc.protocolNamed("CISwipeTransition")
        objc.protocolNamed("CICompositeOperation")
        objc.protocolNamed("CIColorClamp")
        objc.protocolNamed("CIColorControls")
        objc.protocolNamed("CIColorMatrix")
        objc.protocolNamed("CIColorPolynomial")
        objc.protocolNamed("CIDepthToDisparity")
        objc.protocolNamed("CIDisparityToDepth")
        objc.protocolNamed("CIExposureAdjust")
        objc.protocolNamed("CIGammaAdjust")
        objc.protocolNamed("CIHueAdjust")
        objc.protocolNamed("CILinearToSRGBToneCurve")
        objc.protocolNamed("CISRGBToneCurveToLinear")
        objc.protocolNamed("CITemperatureAndTint")
        objc.protocolNamed("CIToneCurve")
        objc.protocolNamed("CIVibrance")
        objc.protocolNamed("CIWhitePointAdjust")
        objc.protocolNamed("CIColorCrossPolynomial")
        objc.protocolNamed("CIColorCube")
        objc.protocolNamed("CIColorCubesMixedWithMask")
        objc.protocolNamed("CIColorCubeWithColorSpace")
        objc.protocolNamed("CIColorCurves")
        objc.protocolNamed("CIColorInvert")
        objc.protocolNamed("CIColorMap")
        objc.protocolNamed("CIColorMonochrome")
        objc.protocolNamed("CIColorPosterize")
        objc.protocolNamed("CIDither")
        objc.protocolNamed("CIDocumentEnhancer")
        objc.protocolNamed("CIFalseColor")
        objc.protocolNamed("CILabDeltaE")
        objc.protocolNamed("CIMaskToAlpha")
        objc.protocolNamed("CIMaximumComponent")
        objc.protocolNamed("CIMinimumComponent")
        objc.protocolNamed("CIPaletteCentroid")
        objc.protocolNamed("CIPalettize")
        objc.protocolNamed("CIPhotoEffect")
        objc.protocolNamed("CISepiaTone")
        objc.protocolNamed("CIThermal")
        objc.protocolNamed("CIVignette")
        objc.protocolNamed("CIVignetteEffect")
        objc.protocolNamed("CIXRay")
        objc.protocolNamed("CIAffineClamp")
        objc.protocolNamed("CIAffineTile")
        objc.protocolNamed("CIEightfoldReflectedTile")
        objc.protocolNamed("CIFourfoldReflectedTile")
        objc.protocolNamed("CIFourfoldRotatedTile")
        objc.protocolNamed("CIFourfoldTranslatedTile")
        objc.protocolNamed("CIGlideReflectedTile")
        objc.protocolNamed("CIKaleidoscope")
        objc.protocolNamed("CIOpTile")
        objc.protocolNamed("CIParallelogramTile")
        objc.protocolNamed("CIPerspectiveTile")
        objc.protocolNamed("CISixfoldReflectedTile")
        objc.protocolNamed("CISixfoldRotatedTile")
        objc.protocolNamed("CITriangleKaleidoscope")
        objc.protocolNamed("CITriangleTile")
        objc.protocolNamed("CITwelvefoldReflectedTile")
        objc.protocolNamed("CIAttributedTextImageGenerator")
        objc.protocolNamed("CIAztecCodeGenerator")
        objc.protocolNamed("CIBarcodeGenerator")
        objc.protocolNamed("CICheckerboardGenerator")
        objc.protocolNamed("CICode128BarcodeGenerator")
        objc.protocolNamed("CILenticularHaloGenerator")
        objc.protocolNamed("CIMeshGenerator")
        objc.protocolNamed("CIPDF417BarcodeGenerator")
        objc.protocolNamed("CIQRCodeGenerator")
        objc.protocolNamed("CIRandomGenerator")
        objc.protocolNamed("CIRoundedRectangleGenerator")
        objc.protocolNamed("CIStarShineGenerator")
        objc.protocolNamed("CIStripesGenerator")
        objc.protocolNamed("CISunbeamsGenerator")
        objc.protocolNamed("CITextImageGenerator")
        objc.protocolNamed("CIBlendWithMask")
        objc.protocolNamed("CIGaborGradients")
        objc.protocolNamed("CIBloom")
        objc.protocolNamed("CIComicEffect")
        objc.protocolNamed("CIConvolution")
        objc.protocolNamed("CICoreMLModel")
        objc.protocolNamed("CICrystallize")
        objc.protocolNamed("CIDepthOfField")
        objc.protocolNamed("CIEdges")
        objc.protocolNamed("CIEdgeWork")
        objc.protocolNamed("CIGloom")
        objc.protocolNamed("CIHeightFieldFromMask")
        objc.protocolNamed("CIHexagonalPixellate")
        objc.protocolNamed("CIHighlightShadowAdjust")
        objc.protocolNamed("CILineOverlay")
        objc.protocolNamed("CIMix")
        objc.protocolNamed("CIPixellate")
        objc.protocolNamed("CIPointillize")
        objc.protocolNamed("CISaliencyMap")
        objc.protocolNamed("CIShadedMaterial")
        objc.protocolNamed("CISpotColor")
        objc.protocolNamed("CISpotLight")
        objc.protocolNamed("CIBokehBlur")
        objc.protocolNamed("CIBoxBlur")
        objc.protocolNamed("CIDiscBlur")
        objc.protocolNamed("CIGaussianBlur")
        objc.protocolNamed("CIMaskedVariableBlur")
        objc.protocolNamed("CIMedian")
        objc.protocolNamed("CIMorphologyGradient")
        objc.protocolNamed("CIMorphologyMaximum")
        objc.protocolNamed("CIMorphologyMinimum")
        objc.protocolNamed("CIMorphologyRectangleMaximum")
        objc.protocolNamed("CIMorphologyRectangleMinimum")
        objc.protocolNamed("CIMotionBlur")
        objc.protocolNamed("CINoiseReduction")
        objc.protocolNamed("CIZoomBlur")

    @min_sdk_level("10.16")
    def test_protocols10_16(self):
        objc.protocolNamed("CIColorAbsoluteDifference")
        objc.protocolNamed("CIColorThreshold")
        objc.protocolNamed("CIColorThresholdOtsu")
        objc.protocolNamed("CIBumpDistortion")
        objc.protocolNamed("CIBumpDistortionLinear")
        objc.protocolNamed("CICircleSplashDistortion")
        objc.protocolNamed("CICircularWrap")
        objc.protocolNamed("CIDisplacementDistortion")
        objc.protocolNamed("CIDroste")
        objc.protocolNamed("CIGlassDistortion")
        objc.protocolNamed("CIGlassLozenge")
        objc.protocolNamed("CIHoleDistortion")
        objc.protocolNamed("CILightTunnel")
        objc.protocolNamed("CINinePartStretched")
        objc.protocolNamed("CINinePartTiled")
        objc.protocolNamed("CIPinchDistortion")
        objc.protocolNamed("CIStretchCrop")
        objc.protocolNamed("CITorusLensDistortion")
        objc.protocolNamed("CITwirlDistortion")
        objc.protocolNamed("CIVortexDistortion")
        objc.protocolNamed("CIAreaReductionFilter")
        objc.protocolNamed("CIAreaAverage")
        objc.protocolNamed("CIAreaHistogram")
        objc.protocolNamed("CIAreaMaximum")
        objc.protocolNamed("CIAreaMaximumAlpha")
        objc.protocolNamed("CIAreaMinimum")
        objc.protocolNamed("CIAreaMinimumAlpha")
        objc.protocolNamed("CIAreaMinMax")
        objc.protocolNamed("CIAreaMinMaxRed")
        objc.protocolNamed("CIColumnAverage")
        objc.protocolNamed("CIHistogramDisplay")
        objc.protocolNamed("CIKMeans")
        objc.protocolNamed("CIRowAverage")

    def assert_rw_prop(self, cls, name, typestr):
        self.assertResultHasType(getattr(cls, name), typestr)
        setter = "set" + name[0].upper() + name[1:] + "_"
        self.assertArgHasType(getattr(cls, setter), 0, typestr)

    def test_methods(self):
        with self.subTest("CIGaussianGradient"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIHueSaturationValueGradient"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "value", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "softness", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "dither", objc._C_FLT)

        with self.subTest("CILinearGradient"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point1", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIRadialGradient"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius0", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius1", objc._C_FLT)

        with self.subTest("CISmoothLinearGradient"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point1", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CISharpenLuminance"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIUnsharpMask"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CICircularScreen"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CICMYKHalftone"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "grayComponentReplacement", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "underColorRemoval", objc._C_FLT
            )

        with self.subTest("CIDotScreen"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CIHatchedScreen"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CILineScreen"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CIFourCoordinateGeometryFilter"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "topLeft", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "topRight", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "bottomRight", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "bottomLeft", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIBicubicScaleTransform"):
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "aspectRatio", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "parameterB", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "parameterC", objc._C_FLT)

        with self.subTest("CIEdgePreserveUpsample"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "spatialSigma", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "lumaSigma", objc._C_FLT)

        with self.subTest("CIKeystoneCorrectionCombined"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "focalLength", objc._C_FLT)

        with self.subTest("CIKeystoneCorrectionHorizontal"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "focalLength", objc._C_FLT)

        with self.subTest("CIKeystoneCorrectionVertical"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "focalLength", objc._C_FLT)

        with self.subTest("CILanczosScaleTransform"):
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "aspectRatio", objc._C_FLT)

        with self.subTest("CIPerspectiveCorrection"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "crop", objc._C_BOOL)

        with self.subTest("CIPerspectiveRotate"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "focalLength", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "pitch", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "yaw", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "roll", objc._C_FLT)

        with self.subTest("CIPerspectiveTransform"):
            pass

        with self.subTest("CIPerspectiveTransformWithExtent"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )

        with self.subTest("CIStraighten"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CITransitionFilter"):
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "time", objc._C_FLT)
            pass

        with self.subTest("CIAccordionFoldTransition"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "bottomHeight", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "numberOfFolds", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "foldShadowAmount", objc._C_FLT
            )

        with self.subTest("CIBarsSwipeTransition"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "barOffset", objc._C_FLT)

        with self.subTest("CICopyMachineTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "opacity", objc._C_FLT)

        with self.subTest("CIDisintegrateWithMaskTransition"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "shadowRadius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "shadowDensity", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "shadowOffset", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIDissolveTransition"):
            pass

        with self.subTest("CIFlashTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "maxStriationRadius", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationStrength", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationContrast", objc._C_FLT
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "fadeThreshold", objc._C_FLT)

        with self.subTest("CIModTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "compression", objc._C_FLT)

        with self.subTest("CIPageCurlTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIPageCurlWithShadowTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "shadowSize", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "shadowAmount", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "shadowExtent", Quartz.CGRect.__typestr__
            )

        with self.subTest("CIRippleTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CISwipeTransition"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "opacity", objc._C_FLT)

        with self.subTest("CICompositeOperation"):
            pass

        with self.subTest("CIColorClamp"):
            pass

        with self.subTest("CIColorControls"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "saturation", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "brightness", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "contrast", objc._C_FLT)

        with self.subTest("CIColorMatrix"):
            pass

        with self.subTest("CIColorPolynomial"):
            pass

        with self.subTest("CIDepthToDisparity"):
            pass

        with self.subTest("CIDisparityToDepth"):
            pass

        with self.subTest("CIExposureAdjust"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "EV", objc._C_FLT)

        with self.subTest("CIGammaAdjust"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "power", objc._C_FLT)

        with self.subTest("CIHueAdjust"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CILinearToSRGBToneCurve"):
            pass

        with self.subTest("CISRGBToneCurveToLinear"):
            pass

        with self.subTest("CITemperatureAndTint"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "neutral", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "targetNeutral", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIToneCurve"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point1", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point2", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point3", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point4", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIVibrance"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "amount", objc._C_FLT)

        with self.subTest("CIWhitePointAdjust"):
            pass

        with self.subTest("CIColorCrossPolynomial"):
            pass

        with self.subTest("CIColorCube"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "cubeDimension", objc._C_FLT)

        with self.subTest("CIColorCubesMixedWithMask"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "cubeDimension", objc._C_FLT)

        with self.subTest("CIColorCubeWithColorSpace"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "cubeDimension", objc._C_FLT)

        with self.subTest("CIColorCurves"):
            pass

        with self.subTest("CIColorInvert"):
            pass

        with self.subTest("CIColorMap"):
            pass

        with self.subTest("CIColorMonochrome"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIColorPosterize"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "levels", objc._C_FLT)

        with self.subTest("CIDither"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIDocumentEnhancer"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "amount", objc._C_FLT)

        with self.subTest("CIFalseColor"):
            pass

        with self.subTest("CILabDeltaE"):
            pass

        with self.subTest("CIMaskToAlpha"):
            pass

        with self.subTest("CIMaximumComponent"):
            pass

        with self.subTest("CIMinimumComponent"):
            pass

        with self.subTest("CIPaletteCentroid"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "perceptual", objc._C_BOOL)

        with self.subTest("CIPalettize"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "perceptual", objc._C_BOOL)

        with self.subTest("CIPhotoEffect"):
            pass

        with self.subTest("CISepiaTone"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIThermal"):
            pass

        with self.subTest("CIVignette"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIVignetteEffect"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "falloff", objc._C_FLT)

        with self.subTest("CIXRay"):
            pass

        with self.subTest("CIAffineClamp"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper,
                "transform",
                Quartz.CGAffineTransform.__typestr__,
            )

        with self.subTest("CIAffineTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper,
                "transform",
                Quartz.CGAffineTransform.__typestr__,
            )

        with self.subTest("CIEightfoldReflectedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIFourfoldReflectedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "acuteAngle", objc._C_FLT)

        with self.subTest("CIFourfoldRotatedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIFourfoldTranslatedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "acuteAngle", objc._C_FLT)

        with self.subTest("CIGlideReflectedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIKaleidoscope"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "count", objc._C_NSInteger)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CIOpTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIParallelogramTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "acuteAngle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIPerspectiveTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "topLeft", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "topRight", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "bottomRight", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "bottomLeft", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CISixfoldReflectedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CISixfoldRotatedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CITriangleKaleidoscope"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point", Quartz.CGPoint.__typestr__
            )

            # XXX: Conflict between two protocols...
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "size", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "rotation", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "decay", objc._C_FLT)

        with self.subTest("CITriangleTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CITwelvefoldReflectedTile"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIAttributedTextImageGenerator"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "scaleFactor", objc._C_FLT)

        with self.subTest("CIAztecCodeGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "correctionLevel", objc._C_FLT
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "layers", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "compactStyle", objc._C_FLT)

        with self.subTest("CIBarcodeGenerator"):
            pass

        with self.subTest("CICheckerboardGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CICode128BarcodeGenerator"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "quietSpace", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "barcodeHeight", objc._C_FLT)

        with self.subTest("CILenticularHaloGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "haloRadius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "haloWidth", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "haloOverlap", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationStrength", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationContrast", objc._C_FLT
            )
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "time", objc._C_FLT)

        with self.subTest("CIMeshGenerator"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)

        with self.subTest("CIPDF417BarcodeGenerator"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "minWidth", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "maxWidth", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "minHeight", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "maxHeight", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "dataColumns", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "rows", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "preferredAspectRatio", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "compactionMode", objc._C_FLT
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "compactStyle", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "correctionLevel", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "alwaysSpecifyCompaction", objc._C_FLT
            )

        with self.subTest("CIQRCodeGenerator"):
            pass

        with self.subTest("CIRandomGenerator"):
            pass

        with self.subTest("CIRoundedRectangleGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIStarShineGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "crossScale", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "crossAngle", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "crossOpacity", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "crossWidth", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "epsilon", objc._C_FLT)

        with self.subTest("CIStripesGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CISunbeamsGenerator"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sunRadius", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "maxStriationRadius", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationStrength", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "striationContrast", objc._C_FLT
            )
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "time", objc._C_FLT)

        with self.subTest("CITextImageGenerator"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "fontSize", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "scaleFactor", objc._C_FLT)

        with self.subTest("CIBlendWithMask"):
            pass

        with self.subTest("CIBloom"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIComicEffect"):
            pass

        with self.subTest("CIConvolution"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "bias", objc._C_FLT)

        with self.subTest("CICoreMLModel"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "headIndex", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "softmaxNormalization", objc._C_BOOL
            )

        with self.subTest("CICrystallize"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CIDepthOfField"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point1", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "saturation", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "unsharpMaskRadius", objc._C_FLT
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "unsharpMaskIntensity", objc._C_FLT
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIEdges"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIEdgeWork"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIGaborGradients"):
            pass

        with self.subTest("CIGloom"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "intensity", objc._C_FLT)

        with self.subTest("CIHeightFieldFromMask"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIHexagonalPixellate"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CIHighlightShadowAdjust"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "shadowAmount", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "highlightAmount", objc._C_FLT
            )

        with self.subTest("CILineOverlay"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "NRNoiseLevel", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "NRSharpness", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "edgeIntensity", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "threshold", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "contrast", objc._C_FLT)

        with self.subTest("CIMix"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "amount", objc._C_FLT)

        with self.subTest("CIPixellate"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CIPointillize"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )

        with self.subTest("CISaliencyMap"):
            pass

        with self.subTest("CIShadedMaterial"):
            # XXX: Disabled this auto-detection because it conflicts with an older
            # binding for Foundation.
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            pass

        with self.subTest("CISpotColor"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "closeness1", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "contrast1", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "closeness2", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "contrast2", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "closeness3", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "contrast3", objc._C_FLT)

        with self.subTest("CISpotLight"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "brightness", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "concentration", objc._C_FLT)

        with self.subTest("CIBokehBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "ringAmount", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "ringSize", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "softness", objc._C_FLT)

        with self.subTest("CIBoxBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIDiscBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIGaussianBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIMaskedVariableBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIMedian"):
            pass

        with self.subTest("CIMorphologyGradient"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIMorphologyMaximum"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIMorphologyMinimum"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CIMorphologyRectangleMaximum"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "height", objc._C_FLT)

        with self.subTest("CIMorphologyRectangleMinimum"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "height", objc._C_FLT)

        with self.subTest("CIMotionBlur"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CINoiseReduction"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "noiseLevel", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "sharpness", objc._C_FLT)

        with self.subTest("CIZoomBlur"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "amount", objc._C_FLT)

        with self.subTest("CIColorAbsoluteDifference"):
            pass

        with self.subTest("CINoiseReduction"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "threshold", objc._C_FLT)

        with self.subTest("CIColorThresholdOtsu"):
            pass

        with self.subTest("CIBumpDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CIBumpDistortionLinear"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CICircleSplashDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CICircularWrap"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CIDisplacementDistortion"):
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            pass

        with self.subTest("CIDroste"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "insetPoint0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "insetPoint1", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "strands", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "periodicity", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "rotation", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "zoom", objc._C_FLT)

        with self.subTest("CIGlassDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CIGlassLozenge"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "point1", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "refraction", objc._C_FLT)

        with self.subTest("CIHoleDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CILightTunnel"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "rotation", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)

        with self.subTest("CILightTunnel"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "breakpoint0", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "breakpoint1", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "growAmount", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "flipYTiles", objc._C_BOOL)

        with self.subTest("CIPinchDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)

        with self.subTest("CIStretchCrop"):
            # self.assert_rw_prop(
            #     TestCIBuiltinFilterHelper, "size", Quartz.CGPoint.__typestr__
            # )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "cropAmount", objc._C_FLT)
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "centerStretchAmount", objc._C_FLT
            )

        with self.subTest("CITorusLensDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "width", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "refraction", objc._C_FLT)

        with self.subTest("CITwirlDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CIVortexDistortion"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "center", Quartz.CGPoint.__typestr__
            )
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "radius", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "angle", objc._C_FLT)

        with self.subTest("CIAreaReductionFilter"):
            self.assert_rw_prop(
                TestCIBuiltinFilterHelper, "extent", Quartz.CGRect.__typestr__
            )

        with self.subTest("CIAreaAverage"):
            pass

        with self.subTest("CIAreaHistogram"):
            # self.assert_rw_prop(TestCIBuiltinFilterHelper, "scale", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "count", objc._C_NSInteger)

        with self.subTest("CIAreaMaximum"):
            pass

        with self.subTest("CIAreaMaximumAlpha"):
            pass

        with self.subTest("CIAreaMinimum"):
            pass

        with self.subTest("CIAreaMinimumAlpha"):
            pass

        with self.subTest("CIAreaMinMax"):
            pass

        with self.subTest("CIAreaMinMaxRed"):
            pass

        with self.subTest("CIColumnAverage"):
            pass

        with self.subTest("CIHistogramDisplay"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "height", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "highLimit", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "lowLimit", objc._C_FLT)

        with self.subTest("CIAreaHistogram"):
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "count", objc._C_NSInteger)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "passes", objc._C_FLT)
            self.assert_rw_prop(TestCIBuiltinFilterHelper, "perceptual", objc._C_BOOL)

        with self.subTest("CIRowAverage"):
            pass
