from Quartz import *

import Utilities
import UIHandling
import Images
import ImageMasking
import BitmapContext
import EPSPrinting
import CoordinateSystem
import PathDrawing
import ColorAndGState
import QuartzTextDrawing
import PatternDrawing
import ShadowsAndTransparencyLayers
import Shadings
import DrawingBasics


# Defines
kCatPDF          = "Kitty.pdf"
kPDFForBlendMode = "blendmode.pdf"

kOurJPEG          = "Poot.jpg"
kQTImage          = "ptlobos.tif"
kOurSubstituteJPG = "LyingOnDeckNoProfile.JPG"
kOurEPS           = "imageturkey.eps"

RAW_IMAGE_WIDTH   = 400
RAW_IMAGE_HEIGHT  = 300
kRawColorImage    = "image-400x300x24.raw"
kOtherColorImage  = "otherimage-400x300x24.raw"

MASKING_IMAGE_WIDTH  = 400
MASKING_IMAGE_HEIGHT = 259
kMaskingImage        = "400x259x8.bw.raw"

noOffScreen     = 0
bitmapOffScreen = 1
layerOffScreen  = 2

# Cache info for GetURL
_mainBundle = None
_urlMap = {}

def GetURL(name):
    """
    Returns the CFURLRef for an embeded resource, or None of that cannot be found.
    """

    global _mainBundle
    if _mainBundle is None:
        _mainBundle = Utilities.getAppBundle()

    mainBundle = _mainBundle
    if mainBundle is not None:
        if name in _urlMap:
            return _urlMap[name]

        url = CFBundleCopyResourceURL(mainBundle, name, None, None)
        _urlMap[name] = url
    else:
        print >>sys.stderr, "Can't get the app bundle!"
        return

    if url is None:
        print >>sys.stderr, "Couldn't get URL for %r"%(name,)

    return url

#
# Helper functions for drawing
#

def callPDFDrawProc(context, proc, pdfFile):
    ourPDFurl = GetURL(pdfFile)

    if ourPDFurl:
        proc(context, ourPDFurl)

def doDrawJPEGFile(context):
    ourJPEGurl = GetURL(kOurJPEG)

    if ourJPEGurl is not None:
        Images.drawJPEGImage(context, ourJPEGurl)


def doRawImageFileWithURL(context):
    url = GetURL(kRawColorImage)

    if url is not None:
        Images.drawImageFromURL(context, url,
            RAW_IMAGE_WIDTH, RAW_IMAGE_HEIGHT,
            8, True);   # 8 bits per component, isColor = True


def doRawImageFileWithCallbacks(context):
    url = GetURL(kRawColorImage)

    if url is not None:
        Images.doImageWithCallbacksCreatedFromURL(context, url,
                RAW_IMAGE_WIDTH, RAW_IMAGE_HEIGHT,
                8, True);   # 8 bits per component, isColor = True


def doDrawImageWithCGImageSource(context):
    url = GetURL(kOurJPEG)
    if url is not None:
        Images.drawImageWithCGImageDataSource(context, url)

def doIncrementalImage(context):
    url = GetURL(kOurJPEG)

    if url is not None:
        Images.doIncrementalImageWithURL(context, url)

def doQTImage(context):
    url = GetURL(kQTImage)

    if url is not None:
        Images.drawQTImageWithQuartz(context, url)


def doJPEGDocumentWithMultipleProfiles(context):
    url = GetURL(kOurSubstituteJPG)

    if url is not None:
        Images.drawJPEGDocumentWithMultipleProfiles(context, url)

def doMaskImageWithMask(context):
    theImageToMaskURL = GetURL(kOtherColorImage)
    theMaskingImageURL = GetURL(kMaskingImage)

    if theImageToMaskURL is not None and  theMaskingImageURL is not None:
        ImageMasking.doMaskImageWithMaskFromURL(context, theImageToMaskURL, RAW_IMAGE_WIDTH,
                            RAW_IMAGE_HEIGHT, 8, theMaskingImageURL, MASKING_IMAGE_WIDTH,
                            MASKING_IMAGE_HEIGHT)

def doMaskImageWithGrayImage(context):
    theImageToMaskURL = GetURL(kOtherColorImage)
    theMaskingImageURL = GetURL(kMaskingImage)

    if theImageToMaskURL is not None and theMaskingImageURL is not None:
        ImageMasking.doMaskImageWithGrayImageFromURL(context, theImageToMaskURL, RAW_IMAGE_WIDTH,
                            RAW_IMAGE_HEIGHT, 8, theMaskingImageURL, MASKING_IMAGE_WIDTH,
                            MASKING_IMAGE_HEIGHT)

def doImageMaskedWithColor(context):
    url = GetURL(kOtherColorImage)

    if url is not None:
        ImageMasking.doMaskImageWithColorFromURL(context, url,
                        RAW_IMAGE_WIDTH, RAW_IMAGE_HEIGHT,
                        True)

def exportImageMaskedWithImage(context):
    theImageToMaskURL = GetURL(kOtherColorImage)
    theMaskingImageURL = GetURL(kMaskingImage)

    if theImageToMaskURL is not None and theMaskingImageURL is not None:
        ImageMasking.exportImageWithMaskFromURLWithDestination(
                context, theImageToMaskURL, RAW_IMAGE_WIDTH,
                RAW_IMAGE_HEIGHT, 8, theMaskingImageURL,
                MASKING_IMAGE_WIDTH, MASKING_IMAGE_HEIGHT)

def doClipMask(context):
    theMaskingImageURL = GetURL(kMaskingImage)

    if theMaskingImageURL is not None:
        ImageMasking.drawWithClippingMask(context,
            theMaskingImageURL, MASKING_IMAGE_WIDTH, MASKING_IMAGE_HEIGHT)

def tilePDFDocument(context, offscreenType):
    url = GetURL(kCatPDF)

    if url is not None:
        if offscreenType == noOffScreen:
            BitmapContext.TilePDFNoBuffer(context, url)
        elif offscreenType == bitmapOffScreen:
            BitmapContext.TilePDFWithOffscreenBitmap(context, url)
        else:
            BitmapContext.TilePDFWithCGLayer(context, url)

def doCompatibleEPSDrawing(context):
    ourEPSurl = GetURL(kOurEPS)

    if ourEPSurl is not None:
        EPSPrinting.drawEPSDataImage(context, ourEPSurl)


def DispatchDrawing(context, drawingType):
    """ Drawing dispatcher """
    if drawingType == UIHandling.kHICommandSimpleRect:
        DrawingBasics.doSimpleRect(context)

    elif drawingType == UIHandling.kHICommandStrokedRect:
        DrawingBasics.doStrokedRect(context)

    elif drawingType == UIHandling.kHICommandStrokedAndFilledRect:
        DrawingBasics.doStrokedAndFilledRect(context)

    elif drawingType == UIHandling.kHICommandPathRects:
        DrawingBasics.doPathRects(context)

    elif drawingType == UIHandling.kHICommandAlphaRects:
        DrawingBasics.doAlphaRects(context)

    elif drawingType == UIHandling.kHICommandDashed:
        DrawingBasics.doDashedLines(context)

    elif drawingType == UIHandling.kHICommandSimpleClip:
        DrawingBasics.doClippedCircle(context)

    elif drawingType == UIHandling.kHICommandPDFDoc:
        callPDFDrawProc(context, DrawingBasics.doPDFDocument, kCatPDF)

    elif drawingType == UIHandling.kHICommandRotatedEllipses:
        CoordinateSystem.doRotatedEllipses(context)

    elif drawingType == UIHandling.kHICommandDrawSkewCoordinates:
        CoordinateSystem.drawSkewedCoordinateSystem(context)

    elif drawingType == UIHandling.kHICommandBezierEgg:
        PathDrawing.doEgg(context)

    elif drawingType == UIHandling.kHICommandRoundedRects:
        PathDrawing.doRoundedRects(context)

    elif drawingType == UIHandling.kHICommandStrokeWithCTM:
        PathDrawing.doStrokeWithCTM(context)

    elif drawingType == UIHandling.kHICommandRotatedEllipsesWithCGPath:
        PathDrawing.doRotatedEllipsesWithCGPath(context)

    elif drawingType == UIHandling.kHICommandPixelAligned:
        PathDrawing.doPixelAlignedFillAndStroke(context)

    elif drawingType == UIHandling.kHICommandDeviceFillAndStrokeColor:
        ColorAndGState.doColorSpaceFillAndStroke(context)

    elif drawingType == UIHandling.kHICommandCLUTDrawGraphics:
        ColorAndGState.doIndexedColorDrawGraphics(context)

    elif drawingType == UIHandling.kHICommandDrawWithGlobalAlpha:
        ColorAndGState.drawWithGlobalAlpha(context)

    elif drawingType == UIHandling.kHICommandDrawWithBlendMode:
        callPDFDrawProc(context, ColorAndGState.drawWithColorBlendMode, kPDFForBlendMode)

    elif drawingType == UIHandling.kHICommandDrawWithColorRefs:
        ColorAndGState.drawWithColorRefs(context)

    elif drawingType == UIHandling.kHICommandFunctionsHaveOwnGSave:
        ColorAndGState.doClippedEllipse(context)

    elif drawingType == UIHandling.kHICommandDrawJPEGImage:
        doDrawJPEGFile(context)

    elif drawingType == UIHandling.kHICommandColorImageFromFile:
        doRawImageFileWithURL(context)

    elif drawingType == UIHandling.kHICommandColorImageFromData:
        Images.doColorRampImage(context)

    elif drawingType == UIHandling.kHICommandColorImageFromCallbacks:
        doRawImageFileWithCallbacks(context)

    elif drawingType == UIHandling.kHICommandGrayRamp:
        Images.doGrayRamp(context)

    elif drawingType == UIHandling.kHICommandDrawWithCGImageSource:
        doDrawImageWithCGImageSource(context)

    elif drawingType == UIHandling.kHICommandDrawWithCGImageSourceIncremental:
        doIncrementalImage(context)

    elif drawingType == UIHandling.kHICommandDrawWithQuickTime:
        doQTImage(context)

    elif drawingType == UIHandling.kHICommandSubstituteImageProfile:
        doJPEGDocumentWithMultipleProfiles(context)

    elif drawingType == UIHandling.kHICommandDoSubImage:
        Images.doColorRampSubImage(context)

    elif drawingType == UIHandling.kHICommandExportWithQuickTime:
        Images.exportColorRampImageWithQT(context)

    elif drawingType == UIHandling.kHICommandMaskTurkeyImage:
        ImageMasking.doOneBitMaskImages(context)

    elif drawingType == UIHandling.kHICommandImageMaskedWithMask:
        doMaskImageWithMask(context)

    elif drawingType == UIHandling.kHICommandImageMaskedWithGrayImage:
        doMaskImageWithGrayImage(context)

    elif drawingType == UIHandling.kHICommandMaskImageWithColor:
        doImageMaskedWithColor(context)

    elif drawingType == UIHandling.kHICommandClipToMask:
        doClipMask(context)

    elif drawingType == UIHandling.kHICommandExportWithCGImageDestination:
        exportImageMaskedWithImage(context)

    elif drawingType == UIHandling.kHICommandSimpleCGLayer:
        BitmapContext.doSimpleCGLayer(context)

    elif drawingType == UIHandling.kHICommandAlphaOnlyContext:
        BitmapContext.doAlphaOnlyContext(context)

    elif drawingType == UIHandling.kHICommandDrawNoOffScreenImage:
        tilePDFDocument(context, noOffScreen)

    elif drawingType == UIHandling.kHICommandDrawOffScreenImage:
        tilePDFDocument(context, bitmapOffScreen)

    elif drawingType == UIHandling.kHICommandDrawWithLayer:
        tilePDFDocument(context, layerOffScreen)

    elif drawingType == UIHandling.kHICommandQuartzRomanText:
        QuartzTextDrawing.drawQuartzRomanText(context)

    elif drawingType == UIHandling.kHICommandQuartzTextModes:
        QuartzTextDrawing.drawQuartzTextWithTextModes(context)

    elif drawingType == UIHandling.kHICommandQuartzTextMatrix:
        QuartzTextDrawing.drawQuartzTextWithTextMatrix(context)

    elif drawingType == UIHandling.kHICommandSimplePattern:
        PatternDrawing.doRedBlackCheckerboard(context)

    elif drawingType == UIHandling.kHICommandPatternPhase:
        PatternDrawing.doPatternPhase(context)

    elif drawingType == UIHandling.kHICommandPatternMatrix:
        PatternDrawing.doPatternMatrix(context)

    elif drawingType == UIHandling.kHICommandUncoloredPattern:
        PatternDrawing.doStencilPattern(context)

    elif drawingType == UIHandling.kHICommandDrawWithPDFPattern:
        callPDFDrawProc(context, PatternDrawing.drawWithPDFPattern, kCatPDF)

    elif drawingType == UIHandling.kHICommandSimpleShadow:
        ShadowsAndTransparencyLayers.drawSimpleShadow(context)

    elif drawingType == UIHandling.kHICommandShadowScaling:
        ShadowsAndTransparencyLayers.doShadowScaling(context)

    elif drawingType == UIHandling.kHICommandShadowProblems:
        ShadowsAndTransparencyLayers.showComplexShadowIssues(context)

    elif drawingType == UIHandling.kHICommandComplexShadow:
        ShadowsAndTransparencyLayers.showComplexShadow(context)

    elif drawingType == UIHandling.kHICommandMultipleShapeComposite:
        ShadowsAndTransparencyLayers.doLayerCompositing(context)

    elif drawingType == UIHandling.kHICommandFillAndStrokeWithShadow:
        ShadowsAndTransparencyLayers.drawFillAndStrokeWithShadow(context)

    elif drawingType == UIHandling.kHICommandPDFDocumentShadow:
        callPDFDrawProc(context, ShadowsAndTransparencyLayers.shadowPDFDocument, kCatPDF)

    elif drawingType == UIHandling.kHICommandSimpleAxialShading:
        Shadings.doSimpleAxialShading(context)

    elif drawingType == UIHandling.kHICommandExampleAxialShadings:
        Shadings.doExampleAxialShading(context)

    elif drawingType == UIHandling.kHICommandSimpleRadialShading:
        Shadings.doSimpleRadialShading(context)

    elif drawingType == UIHandling.kHICommandExampleRadialShadings:
        Shadings.doExampleRadialShadings(context)

    elif drawingType == UIHandling.kHICommandEllipseShading:
        Shadings.doEllipseShading(context)

    elif drawingType == UIHandling.kHICommandDoCompatibleEPS:
        doCompatibleEPSDrawing(context)
