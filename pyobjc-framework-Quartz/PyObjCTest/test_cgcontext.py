from __future__ import with_statement

from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
import os
import sys

try:
    long
except NameError:
    long = int

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')


class TestCGContext (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGContextRef)

    def testConstants(self):
        self.assertEqual(kCGLineJoinMiter, 0)
        self.assertEqual(kCGLineJoinRound, 1)
        self.assertEqual(kCGLineJoinBevel, 2)

        self.assertEqual(kCGLineCapButt, 0)
        self.assertEqual(kCGLineCapRound, 1)
        self.assertEqual(kCGLineCapSquare, 2)

        self.assertEqual(kCGPathFill, 0)
        self.assertEqual(kCGPathEOFill, 1)
        self.assertEqual(kCGPathStroke, 2)
        self.assertEqual(kCGPathFillStroke, 3)
        self.assertEqual(kCGPathEOFillStroke, 4)

        self.assertEqual(kCGTextFill, 0)
        self.assertEqual(kCGTextStroke, 1)
        self.assertEqual(kCGTextFillStroke, 2)
        self.assertEqual(kCGTextInvisible, 3)
        self.assertEqual(kCGTextFillClip, 4)
        self.assertEqual(kCGTextStrokeClip, 5)
        self.assertEqual(kCGTextFillStrokeClip, 6)
        self.assertEqual(kCGTextClip, 7)

        self.assertEqual(kCGEncodingFontSpecific, 0)
        self.assertEqual(kCGEncodingMacRoman, 1)

        self.assertEqual(kCGInterpolationDefault, 0)
        self.assertEqual(kCGInterpolationNone, 1)
        self.assertEqual(kCGInterpolationLow, 2)
        self.assertEqual(kCGInterpolationHigh, 3)

        self.assertEqual(kCGBlendModeNormal, 0)
        self.assertEqual(kCGBlendModeMultiply, 1)
        self.assertEqual(kCGBlendModeScreen, 2)
        self.assertEqual(kCGBlendModeOverlay, 3)
        self.assertEqual(kCGBlendModeDarken, 4)
        self.assertEqual(kCGBlendModeLighten, 5)
        self.assertEqual(kCGBlendModeColorDodge, 6)
        self.assertEqual(kCGBlendModeColorBurn, 7)
        self.assertEqual(kCGBlendModeSoftLight, 8)
        self.assertEqual(kCGBlendModeHardLight, 9)
        self.assertEqual(kCGBlendModeDifference, 10)
        self.assertEqual(kCGBlendModeExclusion, 11)
        self.assertEqual(kCGBlendModeHue, 12)
        self.assertEqual(kCGBlendModeSaturation, 13)
        self.assertEqual(kCGBlendModeColor, 14)
        self.assertEqual(kCGBlendModeLuminosity, 15)
        self.assertEqual(kCGBlendModeClear, 16)
        self.assertEqual(kCGBlendModeCopy, 17)
        self.assertEqual(kCGBlendModeSourceIn, 18)
        self.assertEqual(kCGBlendModeSourceOut, 19)
        self.assertEqual(kCGBlendModeSourceAtop, 20)
        self.assertEqual(kCGBlendModeDestinationOver, 21)
        self.assertEqual(kCGBlendModeDestinationIn, 22)
        self.assertEqual(kCGBlendModeDestinationOut, 23)
        self.assertEqual(kCGBlendModeDestinationAtop, 24)
        self.assertEqual(kCGBlendModeXOR, 25)
        self.assertEqual(kCGBlendModePlusDarker, 26)
        self.assertEqual(kCGBlendModePlusLighter, 27)

    @min_os_level('10.5')
    def testFunctions10_5(self):

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)
        try:
            fn = '/System/Library/CoreServices/DefaultDesktop.jpg'
            if not os.path.exists(fn):
                fn = '/System/Library/Automator/Apply ColorSync Profile to Images.action/Contents/Resources/A-1075-normal.jpg'

            with open(fn, 'rb') as fp:
                data = fp.read()

            provider = CGDataProviderCreateWithCFData(buffer(data))
            image = CGImageCreateWithJPEGDataProvider(provider, None, True, kCGRenderingIntentDefault)
            self.assertIsInstance(image, CGImageRef)

            CGContextDrawTiledImage(context, ((0, 0), (10, 10)), image)

            font =  CGFontCreateWithFontName("Helvetica")
            self.assertIsInstance(font, CGFontRef)
            CGContextSetFont(context, font)

            CGContextBeginTransparencyLayerWithRect(context,
                    ((10, 10), (500, 100)), None)
            CGContextEndTransparencyLayer(context)

            color = CGColorCreateGenericRGB(1.0, 0.5, 0.5, 1.0)
            self.assertIsInstance(color, CGColorRef)
            CGContextSetFillColorWithColor(context, color)
            CGContextSetStrokeColorWithColor(context, color)

            gradient = CGGradientCreateWithColorComponents(
                CGColorSpaceCreateDeviceGray(),
                (0.25, 0.8), (0.95, 0.99), 2)
            self.assertIsInstance(gradient, CGGradientRef)

            CGContextDrawRadialGradient(context, gradient, (10, 15),
                    30, (50, 70), 99.5, kCGGradientDrawsAfterEndLocation)

            def evaluate(info, input, output):
                return input * 4

            func = CGFunctionCreate(None, 1, (0, 1), 2, (0, 1, 0, 1), evaluate)
            self.assertIsInstance(func, CGFunctionRef)
            shading = CGShadingCreateAxial(
                    CGColorSpaceCreateDeviceGray(),
                    (0, 0), (30,90), func, False, False)
            self.assertIsInstance(shading, CGShadingRef)

            self.assertArgHasType(CGContextSetShouldSubpixelPositionFonts, 1, objc._C_BOOL)
            self.assertArgHasType(CGContextSetAllowsFontSubpixelPositioning, 1, objc._C_BOOL)
            self.assertArgHasType(CGContextSetShouldSubpixelQuantizeFonts, 1, objc._C_BOOL)

            gradient = CGGradientCreateWithColorComponents(
                    CGColorSpaceCreateDeviceGray(),
                    (0.25, 0.8), (0.95, 0.99), 2)
            self.assertIsInstance(gradient, CGGradientRef)

            CGContextDrawLinearGradient(context, gradient, (0, 10), (50, 60),
                    kCGGradientDrawsAfterEndLocation)

        finally:
            CGContextEndPage(context)
            if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")



    def testFunctions(self):
        self.assertIsInstance(CGContextGetTypeID(), (int, long))

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)

        self.assertTrue(CGContextIsPathEmpty(context) is True)
        try:
            CGContextBeginPath(context)
            CGContextAddEllipseInRect(context, ((0, 10), (50, 30)))
            CGContextDrawPath(context, kCGPathStroke)

            CGContextSaveGState(context)
            CGContextRestoreGState(context)

            CGContextScaleCTM(context, 5.5, 9.5)
            CGContextTranslateCTM(context, 4.5, 3.5)
            CGContextRotateCTM(context, 0.79)
            CGContextConcatCTM(context, CGAffineTransformIdentity)

            tf = CGContextGetCTM(context)
            self.assertIsInstance(tf, CGAffineTransform)

            CGContextSetLineWidth(context, 2.5)
            CGContextSetLineCap(context, kCGLineCapRound)
            CGContextSetLineJoin(context, kCGLineJoinMiter)
            CGContextSetMiterLimit(context, 9.5)

            CGContextSetLineDash(context, 0.5, [0.4, 0.2, 0.8, 0.1], 4)

            self.assertRaises(ValueError, CGContextSetLineDash,
                    context, 0.5, [0.4, 0.2, 0.8, 0.1], 8)

            CGContextSetFlatness(context, 0.8)
            CGContextSetAlpha(context, 0.5)
            CGContextSetBlendMode(context, kCGBlendModeLighten)


            CGContextMoveToPoint(context, 10.5, 50.8)
            CGContextAddLineToPoint(context, 0.5, 0.7)
            CGContextAddCurveToPoint(context, 7.5, 8.7, 9.10, 9.10, 99.5, 80.5)
            CGContextAddQuadCurveToPoint(context, 50.5, 50.5, 75.9, 78.4)
            CGContextClosePath(context)

            CGContextAddRect(context, CGRect(CGPoint(10, 10), CGSize(50, 50)))
            CGContextAddRects(context, [
                ( (8, 8), (7, 7) ),
                ( (90, 80), (6, 6) ),
                ( (50, 80), (60, 6) ),
            ], 3)
            self.assertRaises(ValueError,
                CGContextAddRects, context, [
                    ( (8, 8), (7, 7) ),
                    ( (90, 80), (6, 6) ),
                    ( (50, 80), (60, 6) ),
                ], 8)


            CGContextAddLines(context, [ (0, 10), (50, 7), (50, 90), (90.5, 8)],
                    4)
            self.assertRaises(ValueError,
                CGContextAddLines, context, [ (0, 10), (50, 7), (50, 90), (90.5, 8)],
                    7)

            CGContextAddEllipseInRect(context, ((0, 10), (50, 30)))

            CGContextAddArc(context, 50, 50, 70.5, 0.5, 1.3, 0)

            CGContextAddArcToPoint(context, 20, 30, 70, 20, 55)

            path = CGPathCreateMutable()
            CGPathAddEllipseInRect(path, None, ((10, 50), (33, 33)))
            self.assertIsInstance(path, CGPathRef)
            CGContextAddPath(context, path)

            self.assertResultHasType(CGContextIsPathEmpty, objc._C_BOOL)
            self.assertTrue(CGContextIsPathEmpty(context) is False)

            pt = CGContextGetPathCurrentPoint(context)
            self.assertIsInstance(pt, CGPoint)

            box = CGContextGetPathBoundingBox(context)
            self.assertIsInstance(box, CGRect)

            self.assertResultHasType(CGContextPathContainsPoint, objc._C_BOOL)
            self.assertIsInstance(CGContextPathContainsPoint(context, pt, kCGPathStroke), bool)

            CGContextFillPath(context)
            CGContextEOFillPath(context)
            CGContextStrokePath(context)
            CGContextFillRect(context, ((10, 10), (50, 30)))

            CGContextFillRects(context, [
                ((10, 10), (50, 30)),
                ((90, 10), (50, 30)),
                ((30, 50), (50, 30))], 3)
            self.assertRaises(ValueError, CGContextFillRects, context, [
                ((10, 10), (50, 30)),
                ((90, 10), (50, 30)),
                ((30, 50), (50, 30))], 6)

            CGContextStrokeRect(context, ((10, 10), (50, 30)))
            CGContextStrokeRectWithWidth(context, ((10, 10), (50, 30)), 8.0)
            CGContextClearRect(context, ((10, 10), (50, 30)))

            CGContextFillEllipseInRect(context, ((10, 10), (50, 30)))
            CGContextStrokeEllipseInRect(context, ((10, 10), (50, 30)))

            CGContextStrokeLineSegments(context,
                    [ (0, 0), (10, 15), (15, 10) ], 3)
            self.assertRaises(ValueError, CGContextStrokeLineSegments, context,
                    [ (0, 0), (10, 15), (15, 10) ], 4)

            CGContextAddRect(context, CGRect(CGPoint(10, 10), CGSize(50, 50)))
            CGContextClip(context)

            CGContextAddRect(context, CGRect(CGPoint(10, 10), CGSize(50, 50)))
            CGContextEOClip(context)

            box = CGContextGetClipBoundingBox(context)
            self.assertIsInstance(box, CGRect)

            CGContextClipToRect(context, ((0, 0), (40, 50)))
            CGContextClipToRects(context,
                    [ ((0, 0), (40, 50)), ((60, 50), (90, 100))], 2)
            self.assertRaises(ValueError, CGContextClipToRects, context,
                    [ ((0, 0), (40, 50)), ((60, 50), (90, 100))], 3)


            CGContextSetFillColorSpace(context, CGColorSpaceCreateDeviceGray())
            CGContextSetStrokeColorSpace(context, CGColorSpaceCreateDeviceGray())

            CGContextSetFillColor(context, [0.5, 1.0])
            CGContextSetStrokeColor(context, [0.5, 1.0])

            CGContextSetPatternPhase(context, CGSize(10.0, 50.0))

            CGContextSetGrayFillColor(context, 0.8, 1.0)
            CGContextSetGrayStrokeColor(context, 0.8, 1.0)

            CGContextSetRGBFillColor(context, 1.0, 1.0, 1.0, 1.0)
            CGContextSetRGBStrokeColor(context, 1.0, 1.0, 1.0, 1.0)

            CGContextSetCMYKFillColor(context, 1.0, 1.0, 1.0, 0.5, 0.8)
            CGContextSetCMYKStrokeColor(context, 1.0, 1.0, 1.0, 0.5, 0.8)

            CGContextSetRenderingIntent(context, kCGRenderingIntentPerceptual)

            v = CGContextGetInterpolationQuality(context)
            self.assertIsInstance(v, (int, long))

            CGContextSetInterpolationQuality(context, kCGInterpolationHigh)

            color = CGColorCreate(CGColorSpaceCreateDeviceRGB(), (1,1,1,1))

            CGContextSetShadowWithColor(context, (2, 3), 0.5, color)
            CGContextSetShadow(context, (5, 6), 0.6)


            CGContextSetCharacterSpacing(context, 0.1)
            CGContextSetTextPosition(context, 10, 50)
            p = CGContextGetTextPosition(context)
            self.assertIsInstance(pt, CGPoint)

            CGContextSetTextMatrix(context, CGAffineTransformIdentity)

            tr = CGContextGetTextMatrix(context)
            self.assertIsInstance(tr, CGAffineTransform)

            CGContextSetTextDrawingMode(context, kCGTextStroke)


            CGContextSetFontSize(context, 11.5)

            CGContextSelectFont(context, b"Helvetica", 10.5, kCGEncodingMacRoman)

            CGContextShowText(context, b"value", 5)
            CGContextShowTextAtPoint(context, 50, 60, b"value", 5)


            v = CGContextRetain(context)
            self.assertTrue(v is context)
            CGContextRelease(context)

            CGContextFlush(context)
            CGContextSynchronize(context)

            self.assertArgHasType(CGContextSetShouldAntialias, 1, objc._C_BOOL)
            CGContextSetShouldAntialias(context, True)

            self.assertArgHasType(CGContextSetAllowsAntialiasing, 1, objc._C_BOOL)
            CGContextSetAllowsAntialiasing(context, True)

            self.assertArgHasType(CGContextSetShouldSmoothFonts, 1, objc._C_BOOL)
            CGContextSetShouldSmoothFonts(context, True)


            CGContextBeginTransparencyLayer(context, None)
            CGContextEndTransparencyLayer(context)


            tf = CGContextGetUserSpaceToDeviceSpaceTransform(context)
            self.assertIsInstance(tf, CGAffineTransform)

            pt = CGContextConvertPointToDeviceSpace(context, (10.5, 11.9))
            self.assertIsInstance(pt, CGPoint)

            pt = CGContextConvertPointToUserSpace(context, (10.5, 11.9))
            self.assertIsInstance(pt, CGPoint)

            sz = CGContextConvertSizeToDeviceSpace(context, (10.5, 11.9))
            self.assertIsInstance(sz, CGSize)

            sz = CGContextConvertSizeToUserSpace(context, (10.5, 11.9))
            self.assertIsInstance(sz, CGSize)

            box = CGContextConvertRectToDeviceSpace(context,
                    ((10.5, 11.9), (55.6, 39.3)))
            self.assertIsInstance(box, CGRect)
            box = CGContextConvertRectToUserSpace(context,
                    ((10.5, 11.9), (55.6, 39.3)))
            self.assertIsInstance(box, CGRect)

            myInfo = object()
            def drawPattern(info, context):
                pass

            pattern = CGPatternCreate(myInfo, CGRectMake(0, 0, 10, 10), CGAffineTransformIdentity, 10.0, 10.0,
                            kCGPatternTilingConstantSpacing, True, drawPattern)
            self.assertIsInstance(pattern, CGPatternRef)

            CGContextSetFillColorSpace(context, CGColorSpaceCreatePattern(None))
            CGContextSetStrokeColorSpace(context, CGColorSpaceCreatePattern(None))
            CGContextSetFillPattern(context, pattern, (1.0,1.0,1.0,1.0))
            CGContextSetStrokePattern(context, pattern, (1.0,1.0,1.0,1.0))

            fn = '/System/Library/CoreServices/DefaultDesktop.jpg'
            if not os.path.exists(fn):
                fn = '/System/Library/Automator/Apply ColorSync Profile to Images.action/Contents/Resources/A-1075-normal.jpg'

            with open(fn, 'rb') as fp:
                data = fp.read()
            provider = CGDataProviderCreateWithCFData(buffer(data))
            image = CGImageCreateWithJPEGDataProvider(provider, None, True, kCGRenderingIntentDefault)
            self.assertIsInstance(image, CGImageRef)

            CGContextDrawImage(context, ((0, 0), (70, 50)), image)

            provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 20 * 10))
            mask = CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
            self.assertIsInstance(mask, CGImageRef)

            CGContextClipToMask(context, CGRectMake(0, 0, 50, 90), mask)

        finally:
            CGContextEndPage(context)
            if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testGlyphFunctions(self):
        self.assertArgHasType(CGContextShowGlyphsAtPositions, 1, b'n^S')
        self.assertArgSizeInArg(CGContextShowGlyphsAtPositions, 1, 3)
        self.assertArgHasType(CGContextShowGlyphsAtPositions, 2, b'n^' + CGPoint.__typestr__)
        self.assertArgSizeInArg(CGContextShowGlyphsAtPositions, 2, 3)

        self.assertArgHasType(CGContextShowGlyphs, 1, b'n^S')
        self.assertArgSizeInArg(CGContextShowGlyphs, 1, 2)

        self.assertArgHasType(CGContextShowGlyphsAtPoint, 1, objc._C_CGFloat)
        self.assertArgHasType(CGContextShowGlyphsAtPoint, 2, objc._C_CGFloat)
        self.assertArgHasType(CGContextShowGlyphsAtPoint, 3, b'n^S')
        self.assertArgSizeInArg(CGContextShowGlyphsAtPoint, 3, 4)

        self.assertArgHasType(CGContextShowGlyphsWithAdvances, 1, b'n^S')
        self.assertArgSizeInArg(CGContextShowGlyphsWithAdvances, 1, 3)
        self.assertArgHasType(CGContextShowGlyphsWithAdvances, 2, b'n^' + CGSize.__typestr__)
        self.assertArgSizeInArg(CGContextShowGlyphsWithAdvances, 2, 3)

        self.assertArgHasType(CGContextDrawPDFPage, 0, b'^{CGContext=}')
        self.assertArgHasType(CGContextDrawPDFPage, 1, b'^{CGPDFPage=}')

        self.assertArgHasType(CGContextDrawPDFDocument, 0, b'^{CGContext=}')
        self.assertArgHasType(CGContextDrawPDFDocument, 1, CGRect.__typestr__)
        self.assertArgHasType(CGContextDrawPDFDocument, 2, b'^{CGPDFDocument=}')
        self.assertArgHasType(CGContextDrawPDFDocument, 3, objc._C_INT)


    @min_os_level('10.5')
    def testContextManager10_5(self):
        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        try:
            CGContextBeginPage(context, objc.NULL)

            # XXX: This need actual tests, this at least tests that
            # the contextmanagers can be used
            with CGTransparencyLayer(context, None):
                pass

            with CGTransparencyLayer(context, None, ((10, 10), (200, 200))):
                pass

        finally:
            CGContextEndPage(context)
            if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testContextManager(self):
        """
        Tests for some additional functionality
        """
        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        try:
            CGContextBeginPage(context, objc.NULL)
            transform = CGContextGetCTM(context)
            newTransform = CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)

            with CGSavedGState(context):
                CGContextConcatCTM(context, newTransform)
                tf = CGContextGetCTM(context)
                self.assertNotEqual(tf, transform)


            tf = CGContextGetCTM(context)
            self.assertEqual(tf, transform)




            CGContextEndPage(context)
            with CGContextPage(context):
                pass

            with CGContextPage(context, CGRectMake(0, 0, 500, 500)):
                pass

            CGContextBeginPage(context, None)



        finally:
            CGContextEndPage(context)
            if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

if __name__ == "__main__":
    main()
