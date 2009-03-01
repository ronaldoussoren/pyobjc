from __future__ import with_statement

from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import os


class TestCGContext (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGContextRef)

    def testConstants(self):
        self.failUnlessEqual(kCGLineJoinMiter, 0)
        self.failUnlessEqual(kCGLineJoinRound, 1)
        self.failUnlessEqual(kCGLineJoinBevel, 2)

        self.failUnlessEqual(kCGLineCapButt, 0)
        self.failUnlessEqual(kCGLineCapRound, 1)
        self.failUnlessEqual(kCGLineCapSquare, 2)

        self.failUnlessEqual(kCGPathFill, 0)
        self.failUnlessEqual(kCGPathEOFill, 1)
        self.failUnlessEqual(kCGPathStroke, 2)
        self.failUnlessEqual(kCGPathFillStroke, 3)
        self.failUnlessEqual(kCGPathEOFillStroke, 4)

        self.failUnlessEqual(kCGTextFill, 0)
        self.failUnlessEqual(kCGTextStroke, 1)
        self.failUnlessEqual(kCGTextFillStroke, 2)
        self.failUnlessEqual(kCGTextInvisible, 3)
        self.failUnlessEqual(kCGTextFillClip, 4)
        self.failUnlessEqual(kCGTextStrokeClip, 5)
        self.failUnlessEqual(kCGTextFillStrokeClip, 6)
        self.failUnlessEqual(kCGTextClip, 7)

        self.failUnlessEqual(kCGEncodingFontSpecific, 0)
        self.failUnlessEqual(kCGEncodingMacRoman, 1)

        self.failUnlessEqual(kCGInterpolationDefault, 0)
        self.failUnlessEqual(kCGInterpolationNone, 1)
        self.failUnlessEqual(kCGInterpolationLow, 2)
        self.failUnlessEqual(kCGInterpolationHigh, 3)

        self.failUnlessEqual(kCGBlendModeNormal, 0)
        self.failUnlessEqual(kCGBlendModeMultiply, 1)
        self.failUnlessEqual(kCGBlendModeScreen, 2)
        self.failUnlessEqual(kCGBlendModeOverlay, 3)
        self.failUnlessEqual(kCGBlendModeDarken, 4)
        self.failUnlessEqual(kCGBlendModeLighten, 5)
        self.failUnlessEqual(kCGBlendModeColorDodge, 6)
        self.failUnlessEqual(kCGBlendModeColorBurn, 7)
        self.failUnlessEqual(kCGBlendModeSoftLight, 8)
        self.failUnlessEqual(kCGBlendModeHardLight, 9)
        self.failUnlessEqual(kCGBlendModeDifference, 10)
        self.failUnlessEqual(kCGBlendModeExclusion, 11)
        self.failUnlessEqual(kCGBlendModeHue, 12)
        self.failUnlessEqual(kCGBlendModeSaturation, 13)
        self.failUnlessEqual(kCGBlendModeColor, 14)
        self.failUnlessEqual(kCGBlendModeLuminosity, 15)
        self.failUnlessEqual(kCGBlendModeClear, 16)
        self.failUnlessEqual(kCGBlendModeCopy, 17)
        self.failUnlessEqual(kCGBlendModeSourceIn, 18)
        self.failUnlessEqual(kCGBlendModeSourceOut, 19)
        self.failUnlessEqual(kCGBlendModeSourceAtop, 20)
        self.failUnlessEqual(kCGBlendModeDestinationOver, 21)
        self.failUnlessEqual(kCGBlendModeDestinationIn, 22)
        self.failUnlessEqual(kCGBlendModeDestinationOut, 23)
        self.failUnlessEqual(kCGBlendModeDestinationAtop, 24)
        self.failUnlessEqual(kCGBlendModeXOR, 25)
        self.failUnlessEqual(kCGBlendModePlusDarker, 26)
        self.failUnlessEqual(kCGBlendModePlusLighter, 27)

    def testFunctions(self):
        self.failUnlessIsInstance(CGContextGetTypeID(), (int, long))

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.failUnlessIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)

        self.failUnless(CGContextIsPathEmpty(context) is True)
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
            self.failUnlessIsInstance(tf, CGAffineTransform)

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
            self.failUnlessIsInstance(path, CGPathRef)
            CGContextAddPath(context, path)

            self.failUnlessResultHasType(CGContextIsPathEmpty, objc._C_BOOL)
            self.failUnless(CGContextIsPathEmpty(context) is False)

            pt = CGContextGetPathCurrentPoint(context)
            self.failUnlessIsInstance(pt, CGPoint)

            box = CGContextGetPathBoundingBox(context)
            self.failUnlessIsInstance(box, CGRect)

            self.failUnlessResultHasType(CGContextPathContainsPoint, objc._C_BOOL)
            self.failUnlessIsInstance(CGContextPathContainsPoint(context, pt, kCGPathStroke), bool)

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
            self.failUnlessIsInstance(box, CGRect)

            CGContextClipToRect(context, ((0, 0), (40, 50)))
            CGContextClipToRects(context,
                    [ ((0, 0), (40, 50)), ((60, 50), (90, 100))], 2)
            self.assertRaises(ValueError, CGContextClipToRects, context,
                    [ ((0, 0), (40, 50)), ((60, 50), (90, 100))], 3)

            color = CGColorCreateGenericRGB(1.0, 0.5, 0.5, 1.0)
            self.failUnlessIsInstance(color, CGColorRef)
            CGContextSetFillColorWithColor(context, color)
            CGContextSetStrokeColorWithColor(context, color)

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
            self.failUnlessIsInstance(v, (int, long))

            CGContextSetInterpolationQuality(context, kCGInterpolationHigh)

            CGContextSetShadowWithColor(context, (2, 3), 0.5, color)
            CGContextSetShadow(context, (5, 6), 0.6)

            gradient = CGGradientCreateWithColorComponents(
                    CGColorSpaceCreateDeviceGray(),
                    (0.25, 0.8), (0.95, 0.99), 2)
            self.failUnlessIsInstance(gradient, CGGradientRef)

            CGContextDrawLinearGradient(context, gradient, (0, 10), (50, 60),
                    kCGGradientDrawsAfterEndLocation)

            CGContextSetCharacterSpacing(context, 0.1)
            CGContextSetTextPosition(context, 10, 50)
            p = CGContextGetTextPosition(context)
            self.failUnlessIsInstance(pt, CGPoint)

            CGContextSetTextMatrix(context, CGAffineTransformIdentity)

            tr = CGContextGetTextMatrix(context)
            self.failUnlessIsInstance(tr, CGAffineTransform)

            CGContextSetTextDrawingMode(context, kCGTextStroke)

            font =  CGFontCreateWithFontName("Helvetica")
            self.failUnlessIsInstance(font, CGFontRef)
            CGContextSetFont(context, font)

            CGContextSetFontSize(context, 11.5)

            CGContextSelectFont(context, "Helvetica", 10.5, kCGEncodingMacRoman)

            CGContextShowText(context, "value", 5)
            CGContextShowTextAtPoint(context, 50, 60, "value", 5)


            v = CGContextRetain(context)
            self.failUnless(v is context)
            CGContextRelease(context)

            CGContextFlush(context)
            CGContextSynchronize(context)

            self.failUnlessArgHasType(CGContextSetShouldAntialias, 1, objc._C_BOOL)
            CGContextSetShouldAntialias(context, True)

            self.failUnlessArgHasType(CGContextSetAllowsAntialiasing, 1, objc._C_BOOL)
            CGContextSetAllowsAntialiasing(context, True)

            self.failUnlessArgHasType(CGContextSetShouldSmoothFonts, 1, objc._C_BOOL)
            CGContextSetShouldSmoothFonts(context, True)


            CGContextBeginTransparencyLayer(context, None)
            CGContextEndTransparencyLayer(context)

            CGContextBeginTransparencyLayerWithRect(context,
                    ((10, 10), (500, 100)), None)
            CGContextEndTransparencyLayer(context)

            tf = CGContextGetUserSpaceToDeviceSpaceTransform(context)
            self.failUnlessIsInstance(tf, CGAffineTransform)

            pt = CGContextConvertPointToDeviceSpace(context, (10.5, 11.9))
            self.failUnlessIsInstance(pt, CGPoint)

            pt = CGContextConvertPointToUserSpace(context, (10.5, 11.9))
            self.failUnlessIsInstance(pt, CGPoint)

            sz = CGContextConvertSizeToDeviceSpace(context, (10.5, 11.9))
            self.failUnlessIsInstance(sz, CGSize)

            sz = CGContextConvertSizeToUserSpace(context, (10.5, 11.9))
            self.failUnlessIsInstance(sz, CGSize)

            box = CGContextConvertRectToDeviceSpace(context, 
                    ((10.5, 11.9), (55.6, 39.3)))
            self.failUnlessIsInstance(box, CGRect)
            box = CGContextConvertRectToUserSpace(context, 
                    ((10.5, 11.9), (55.6, 39.3)))
            self.failUnlessIsInstance(box, CGRect)

            myInfo = object()
            def drawPattern(info, context):
                pass

            pattern = CGPatternCreate(myInfo, CGRectMake(0, 0, 10, 10), CGAffineTransformIdentity, 10.0, 10.0,
                            kCGPatternTilingConstantSpacing, True, drawPattern)
            self.failUnlessIsInstance(pattern, CGPatternRef)

            CGContextSetFillColorSpace(context, CGColorSpaceCreatePattern(None))
            CGContextSetStrokeColorSpace(context, CGColorSpaceCreatePattern(None))
            CGContextSetFillPattern(context, pattern, (1.0,1.0,1.0,1.0))
            CGContextSetStrokePattern(context, pattern, (1.0,1.0,1.0,1.0))

            provider = CGDataProviderCreateWithCFData(buffer(
                            open('/System/Library/CoreServices/DefaultDesktop.jpg', 'rb').read()))
            image = CGImageCreateWithJPEGDataProvider(provider, None, True, kCGRenderingIntentDefault)
            self.failUnlessIsInstance(image, CGImageRef)

            CGContextDrawImage(context, ((0, 0), (70, 50)), image)
            CGContextDrawTiledImage(context, ((0, 0), (10, 10)), image)

            provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 20 * 10))
            mask = CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
            self.failUnlessIsInstance(mask, CGImageRef)

            CGContextClipToMask(context, CGRectMake(0, 0, 50, 90), mask)

        finally:
            CGContextEndPage(context)
            CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testMissing(self):
        self.fail("CGContextShowGlyphsAtPositions")
        self.fail("CGContextShowGlyphs")
        self.fail("CGContextShowGlyphsAtPoint")
        self.fail("CGContextShowGlyphsWithAdvances")
        self.fail("CGContextDrawPDFPage")
        self.fail("CGContextDrawPDFDocument")


    def testContextManager(self):
        """
        Tests for some additional functionality
        """
        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.failUnlessIsInstance(context, CGContextRef)
        try:
            CGContextBeginPage(context, objc.NULL)
            transform = CGContextGetCTM(context)
            newTransform = CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)

            with CGSavedGState(context):
                CGContextConcatCTM(context, newTransform)
                tf = CGContextGetCTM(context)
                self.failIfEqual(tf, transform)


            tf = CGContextGetCTM(context)
            self.failUnlessEqual(tf, transform)

           
            # XXX: This need actual tests, this at least tests that
            # the contextmanagers can be used
            with CGTransparencyLayer(context, None):
                pass

            with CGTransparencyLayer(context, None, ((10, 10), (200, 200))):
                pass


            CGContextEndPage(context)
            with CGContextPage(context):
                pass

            with CGContextPage(context, CGRectMake(0, 0, 500, 500)):
                pass

            CGContextBeginPage(context, None)



        finally:
            CGContextEndPage(context)
            CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

if __name__ == "__main__":
    main()
