import os
import objc

import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCGContext(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGContextRef)

    def testConstants(self):
        self.assertEqual(Quartz.kCGLineJoinMiter, 0)
        self.assertEqual(Quartz.kCGLineJoinRound, 1)
        self.assertEqual(Quartz.kCGLineJoinBevel, 2)

        self.assertEqual(Quartz.kCGLineCapButt, 0)
        self.assertEqual(Quartz.kCGLineCapRound, 1)
        self.assertEqual(Quartz.kCGLineCapSquare, 2)

        self.assertEqual(Quartz.kCGPathFill, 0)
        self.assertEqual(Quartz.kCGPathEOFill, 1)
        self.assertEqual(Quartz.kCGPathStroke, 2)
        self.assertEqual(Quartz.kCGPathFillStroke, 3)
        self.assertEqual(Quartz.kCGPathEOFillStroke, 4)

        self.assertEqual(Quartz.kCGTextFill, 0)
        self.assertEqual(Quartz.kCGTextStroke, 1)
        self.assertEqual(Quartz.kCGTextFillStroke, 2)
        self.assertEqual(Quartz.kCGTextInvisible, 3)
        self.assertEqual(Quartz.kCGTextFillClip, 4)
        self.assertEqual(Quartz.kCGTextStrokeClip, 5)
        self.assertEqual(Quartz.kCGTextFillStrokeClip, 6)
        self.assertEqual(Quartz.kCGTextClip, 7)

        self.assertEqual(Quartz.kCGEncodingFontSpecific, 0)
        self.assertEqual(Quartz.kCGEncodingMacRoman, 1)

        self.assertEqual(Quartz.kCGInterpolationDefault, 0)
        self.assertEqual(Quartz.kCGInterpolationNone, 1)
        self.assertEqual(Quartz.kCGInterpolationLow, 2)
        self.assertEqual(Quartz.kCGInterpolationHigh, 3)

        self.assertEqual(Quartz.kCGBlendModeNormal, 0)
        self.assertEqual(Quartz.kCGBlendModeMultiply, 1)
        self.assertEqual(Quartz.kCGBlendModeScreen, 2)
        self.assertEqual(Quartz.kCGBlendModeOverlay, 3)
        self.assertEqual(Quartz.kCGBlendModeDarken, 4)
        self.assertEqual(Quartz.kCGBlendModeLighten, 5)
        self.assertEqual(Quartz.kCGBlendModeColorDodge, 6)
        self.assertEqual(Quartz.kCGBlendModeColorBurn, 7)
        self.assertEqual(Quartz.kCGBlendModeSoftLight, 8)
        self.assertEqual(Quartz.kCGBlendModeHardLight, 9)
        self.assertEqual(Quartz.kCGBlendModeDifference, 10)
        self.assertEqual(Quartz.kCGBlendModeExclusion, 11)
        self.assertEqual(Quartz.kCGBlendModeHue, 12)
        self.assertEqual(Quartz.kCGBlendModeSaturation, 13)
        self.assertEqual(Quartz.kCGBlendModeColor, 14)
        self.assertEqual(Quartz.kCGBlendModeLuminosity, 15)
        self.assertEqual(Quartz.kCGBlendModeClear, 16)
        self.assertEqual(Quartz.kCGBlendModeCopy, 17)
        self.assertEqual(Quartz.kCGBlendModeSourceIn, 18)
        self.assertEqual(Quartz.kCGBlendModeSourceOut, 19)
        self.assertEqual(Quartz.kCGBlendModeSourceAtop, 20)
        self.assertEqual(Quartz.kCGBlendModeDestinationOver, 21)
        self.assertEqual(Quartz.kCGBlendModeDestinationIn, 22)
        self.assertEqual(Quartz.kCGBlendModeDestinationOut, 23)
        self.assertEqual(Quartz.kCGBlendModeDestinationAtop, 24)
        self.assertEqual(Quartz.kCGBlendModeXOR, 25)
        self.assertEqual(Quartz.kCGBlendModePlusDarker, 26)
        self.assertEqual(Quartz.kCGBlendModePlusLighter, 27)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        Quartz.CGContextBeginPage(context, objc.NULL)
        try:
            fn = "/System/Library/CoreServices/DefaultDesktop.jpg"
            if not os.path.exists(fn):
                fn = "/System/Library/Automator/Apply ColorSync Profile to Images.action/Contents/Resources/A-1075-normal.jpg"
                if not os.path.exists(fn):
                    fn = "/System/Library/CoreServices//RemoteManagement/ARDAgent.app/Contents/Resources/Lock.jpg"

            with open(fn, "rb") as fp:
                data = fp.read()

            provider = Quartz.CGDataProviderCreateWithCFData(data)
            image = Quartz.CGImageCreateWithJPEGDataProvider(
                provider, None, True, Quartz.kCGRenderingIntentDefault
            )
            self.assertIsInstance(image, Quartz.CGImageRef)
            self.assertArgIsIn(Quartz.CGImageCreateWithJPEGDataProvider, 1)
            self.assertArgIsVariableSize(Quartz.CGImageCreateWithJPEGDataProvider, 1)

            Quartz.CGContextDrawTiledImage(context, ((0, 0), (10, 10)), image)

            font = Quartz.CGFontCreateWithFontName("Helvetica")
            self.assertIsInstance(font, Quartz.CGFontRef)
            Quartz.CGContextSetFont(context, font)

            Quartz.CGContextBeginTransparencyLayerWithRect(
                context, ((10, 10), (500, 100)), None
            )
            Quartz.CGContextEndTransparencyLayer(context)

            color = Quartz.CGColorCreateGenericRGB(1.0, 0.5, 0.5, 1.0)
            self.assertIsInstance(color, Quartz.CGColorRef)
            Quartz.CGContextSetFillColorWithColor(context, color)
            Quartz.CGContextSetStrokeColorWithColor(context, color)

            gradient = Quartz.CGGradientCreateWithColorComponents(
                Quartz.CGColorSpaceCreateDeviceGray(), (0.25, 0.8), (0.95, 0.99), 2
            )
            self.assertIsInstance(gradient, Quartz.CGGradientRef)

            Quartz.CGContextDrawRadialGradient(
                context,
                gradient,
                (10, 15),
                30,
                (50, 70),
                99.5,
                Quartz.kCGGradientDrawsAfterEndLocation,
            )

            Quartz.CGContextDrawShading

            def evaluate(info, input_value, output_value):
                return input_value * 4

            func = Quartz.CGFunctionCreate(None, 1, (0, 1), 2, (0, 1, 0, 1), evaluate)
            self.assertIsInstance(func, Quartz.CGFunctionRef)
            shading = Quartz.CGShadingCreateAxial(
                Quartz.CGColorSpaceCreateDeviceGray(),
                (0, 0),
                (30, 90),
                func,
                False,
                False,
            )
            self.assertIsInstance(shading, Quartz.CGShadingRef)

            self.assertArgHasType(
                Quartz.CGContextSetShouldSubpixelPositionFonts, 1, objc._C_BOOL
            )
            self.assertArgHasType(
                Quartz.CGContextSetAllowsFontSubpixelPositioning, 1, objc._C_BOOL
            )
            self.assertArgHasType(
                Quartz.CGContextSetShouldSubpixelQuantizeFonts, 1, objc._C_BOOL
            )

            gradient = Quartz.CGGradientCreateWithColorComponents(
                Quartz.CGColorSpaceCreateDeviceGray(), (0.25, 0.8), (0.95, 0.99), 2
            )
            self.assertIsInstance(gradient, Quartz.CGGradientRef)

            Quartz.CGContextDrawLinearGradient(
                context,
                gradient,
                (0, 10),
                (50, 60),
                Quartz.kCGGradientDrawsAfterEndLocation,
            )

        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGContextGetTypeID(), int)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        Quartz.CGContextBeginPage(context, objc.NULL)

        self.assertTrue(Quartz.CGContextIsPathEmpty(context) is True)
        try:
            Quartz.CGContextBeginPath(context)
            Quartz.CGContextAddEllipseInRect(context, ((0, 10), (50, 30)))
            Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

            Quartz.CGContextSaveGState(context)
            Quartz.CGContextRestoreGState(context)

            Quartz.CGContextScaleCTM(context, 5.5, 9.5)
            Quartz.CGContextTranslateCTM(context, 4.5, 3.5)
            Quartz.CGContextRotateCTM(context, 0.79)
            Quartz.CGContextConcatCTM(context, Quartz.CGAffineTransformIdentity)

            tf = Quartz.CGContextGetCTM(context)
            self.assertIsInstance(tf, Quartz.CGAffineTransform)

            Quartz.CGContextSetLineWidth(context, 2.5)
            Quartz.CGContextSetLineCap(context, Quartz.kCGLineCapRound)
            Quartz.CGContextSetLineJoin(context, Quartz.kCGLineJoinMiter)
            Quartz.CGContextSetMiterLimit(context, 9.5)

            Quartz.CGContextSetLineDash(context, 0.5, [0.4, 0.2, 0.8, 0.1], 4)

            self.assertRaises(
                ValueError,
                Quartz.CGContextSetLineDash,
                context,
                0.5,
                [0.4, 0.2, 0.8, 0.1],
                8,
            )

            Quartz.CGContextSetFlatness(context, 0.8)
            Quartz.CGContextSetAlpha(context, 0.5)
            Quartz.CGContextSetBlendMode(context, Quartz.kCGBlendModeLighten)

            Quartz.CGContextMoveToPoint(context, 10.5, 50.8)
            Quartz.CGContextAddLineToPoint(context, 0.5, 0.7)
            Quartz.CGContextAddCurveToPoint(context, 7.5, 8.7, 9.10, 9.10, 99.5, 80.5)
            Quartz.CGContextAddQuadCurveToPoint(context, 50.5, 50.5, 75.9, 78.4)
            Quartz.CGContextClosePath(context)

            Quartz.CGContextAddRect(
                context, Quartz.CGRect(Quartz.CGPoint(10, 10), Quartz.CGSize(50, 50))
            )
            Quartz.CGContextAddRects(
                context, [((8, 8), (7, 7)), ((90, 80), (6, 6)), ((50, 80), (60, 6))], 3
            )
            self.assertRaises(
                ValueError,
                Quartz.CGContextAddRects,
                context,
                [((8, 8), (7, 7)), ((90, 80), (6, 6)), ((50, 80), (60, 6))],
                8,
            )

            Quartz.CGContextAddLines(
                context, [(0, 10), (50, 7), (50, 90), (90.5, 8)], 4
            )
            self.assertRaises(
                ValueError,
                Quartz.CGContextAddLines,
                context,
                [(0, 10), (50, 7), (50, 90), (90.5, 8)],
                7,
            )

            Quartz.CGContextAddEllipseInRect(context, ((0, 10), (50, 30)))

            Quartz.CGContextAddArc(context, 50, 50, 70.5, 0.5, 1.3, 0)

            Quartz.CGContextAddArcToPoint(context, 20, 30, 70, 20, 55)

            path = Quartz.CGPathCreateMutable()
            Quartz.CGPathAddEllipseInRect(path, None, ((10, 50), (33, 33)))
            self.assertIsInstance(path, Quartz.CGPathRef)
            Quartz.CGContextAddPath(context, path)

            Quartz.CGContextReplacePathWithStrokedPath(context)

            self.assertResultHasType(Quartz.CGContextIsPathEmpty, objc._C_BOOL)
            self.assertTrue(Quartz.CGContextIsPathEmpty(context) is False)

            pt = Quartz.CGContextGetPathCurrentPoint(context)
            self.assertIsInstance(pt, Quartz.CGPoint)

            box = Quartz.CGContextGetPathBoundingBox(context)
            self.assertIsInstance(box, Quartz.CGRect)

            p = Quartz.CGContextCopyPath(context)
            self.assertIsInstance(p, Quartz.CGPathRef)

            self.assertResultHasType(Quartz.CGContextPathContainsPoint, objc._C_BOOL)
            self.assertIsInstance(
                Quartz.CGContextPathContainsPoint(context, pt, Quartz.kCGPathStroke),
                bool,
            )

            Quartz.CGContextFillPath(context)
            Quartz.CGContextEOFillPath(context)
            Quartz.CGContextStrokePath(context)
            Quartz.CGContextFillRect(context, ((10, 10), (50, 30)))

            Quartz.CGContextFillRects(
                context,
                [((10, 10), (50, 30)), ((90, 10), (50, 30)), ((30, 50), (50, 30))],
                3,
            )
            self.assertRaises(
                ValueError,
                Quartz.CGContextFillRects,
                context,
                [((10, 10), (50, 30)), ((90, 10), (50, 30)), ((30, 50), (50, 30))],
                6,
            )

            Quartz.CGContextStrokeRect(context, ((10, 10), (50, 30)))
            Quartz.CGContextStrokeRectWithWidth(context, ((10, 10), (50, 30)), 8.0)
            Quartz.CGContextClearRect(context, ((10, 10), (50, 30)))

            Quartz.CGContextFillEllipseInRect(context, ((10, 10), (50, 30)))
            Quartz.CGContextStrokeEllipseInRect(context, ((10, 10), (50, 30)))

            Quartz.CGContextStrokeLineSegments(
                context, [(0, 0), (10, 15), (15, 10), (0, 0)], 4
            )
            self.assertRaises(
                ValueError,
                Quartz.CGContextStrokeLineSegments,
                context,
                [(0, 0), (10, 15), (15, 10)],
                4,
            )

            Quartz.CGContextAddRect(
                context, Quartz.CGRect(Quartz.CGPoint(10, 10), Quartz.CGSize(50, 50))
            )
            Quartz.CGContextClip(context)

            Quartz.CGContextAddRect(
                context, Quartz.CGRect(Quartz.CGPoint(10, 10), Quartz.CGSize(50, 50))
            )
            Quartz.CGContextEOClip(context)

            box = Quartz.CGContextGetClipBoundingBox(context)
            self.assertIsInstance(box, Quartz.CGRect)

            Quartz.CGContextClipToRect(context, ((0, 0), (40, 50)))
            Quartz.CGContextClipToRects(
                context, [((0, 0), (40, 50)), ((60, 50), (90, 100))], 2
            )
            self.assertRaises(
                ValueError,
                Quartz.CGContextClipToRects,
                context,
                [((0, 0), (40, 50)), ((60, 50), (90, 100))],
                3,
            )

            Quartz.CGContextSetFillColorSpace(
                context, Quartz.CGColorSpaceCreateDeviceGray()
            )
            Quartz.CGContextSetStrokeColorSpace(
                context, Quartz.CGColorSpaceCreateDeviceGray()
            )

            Quartz.CGContextSetFillColor(context, [0.5, 1.0])
            Quartz.CGContextSetStrokeColor(context, [0.5, 1.0])

            Quartz.CGContextSetPatternPhase(context, Quartz.CGSize(10.0, 50.0))

            Quartz.CGContextSetGrayFillColor(context, 0.8, 1.0)
            Quartz.CGContextSetGrayStrokeColor(context, 0.8, 1.0)

            Quartz.CGContextSetRGBFillColor(context, 1.0, 1.0, 1.0, 1.0)
            Quartz.CGContextSetRGBStrokeColor(context, 1.0, 1.0, 1.0, 1.0)

            Quartz.CGContextSetCMYKFillColor(context, 1.0, 1.0, 1.0, 0.5, 0.8)
            Quartz.CGContextSetCMYKStrokeColor(context, 1.0, 1.0, 1.0, 0.5, 0.8)

            Quartz.CGContextSetRenderingIntent(
                context, Quartz.kCGRenderingIntentPerceptual
            )

            v = Quartz.CGContextGetInterpolationQuality(context)
            self.assertIsInstance(v, int)

            Quartz.CGContextSetInterpolationQuality(
                context, Quartz.kCGInterpolationHigh
            )

            color = Quartz.CGColorCreate(
                Quartz.CGColorSpaceCreateDeviceRGB(), (1, 1, 1, 1)
            )

            Quartz.CGContextSetShadowWithColor(context, (2, 3), 0.5, color)
            Quartz.CGContextSetShadow(context, (5, 6), 0.6)

            Quartz.CGContextSetCharacterSpacing(context, 0.1)
            Quartz.CGContextSetTextPosition(context, 10, 50)
            p = Quartz.CGContextGetTextPosition(context)
            self.assertIsInstance(pt, Quartz.CGPoint)

            Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)

            tr = Quartz.CGContextGetTextMatrix(context)
            self.assertIsInstance(tr, Quartz.CGAffineTransform)

            Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextStroke)

            Quartz.CGContextSetFontSize(context, 11.5)

            Quartz.CGContextSelectFont(
                context, b"Helvetica", 10.5, Quartz.kCGEncodingMacRoman
            )

            Quartz.CGContextShowText(context, b"value", 5)
            Quartz.CGContextShowTextAtPoint(context, 50, 60, b"value", 5)

            v = Quartz.CGContextRetain(context)
            self.assertTrue(v is context)
            Quartz.CGContextRelease(context)

            Quartz.CGContextFlush(context)
            Quartz.CGContextSynchronize(context)

            self.assertArgHasType(Quartz.CGContextSetShouldAntialias, 1, objc._C_BOOL)
            Quartz.CGContextSetShouldAntialias(context, True)

            self.assertArgHasType(
                Quartz.CGContextSetAllowsAntialiasing, 1, objc._C_BOOL
            )
            Quartz.CGContextSetAllowsAntialiasing(context, True)

            self.assertArgHasType(Quartz.CGContextSetShouldSmoothFonts, 1, objc._C_BOOL)
            Quartz.CGContextSetShouldSmoothFonts(context, True)

            self.assertArgHasType(
                Quartz.CGContextSetAllowsFontSmoothing, 1, objc._C_BOOL
            )
            Quartz.CGContextSetAllowsFontSmoothing(context, True)

            self.assertArgHasType(
                Quartz.CGContextSetAllowsFontSubpixelQuantization, 1, objc._C_BOOL
            )
            Quartz.CGContextSetAllowsFontSubpixelQuantization(context, True)

            Quartz.CGContextBeginTransparencyLayer(context, None)
            Quartz.CGContextEndTransparencyLayer(context)

            tf = Quartz.CGContextGetUserSpaceToDeviceSpaceTransform(context)
            self.assertIsInstance(tf, Quartz.CGAffineTransform)

            pt = Quartz.CGContextConvertPointToDeviceSpace(context, (10.5, 11.9))
            self.assertIsInstance(pt, Quartz.CGPoint)

            pt = Quartz.CGContextConvertPointToUserSpace(context, (10.5, 11.9))
            self.assertIsInstance(pt, Quartz.CGPoint)

            sz = Quartz.CGContextConvertSizeToDeviceSpace(context, (10.5, 11.9))
            self.assertIsInstance(sz, Quartz.CGSize)

            sz = Quartz.CGContextConvertSizeToUserSpace(context, (10.5, 11.9))
            self.assertIsInstance(sz, Quartz.CGSize)

            box = Quartz.CGContextConvertRectToDeviceSpace(
                context, ((10.5, 11.9), (55.6, 39.3))
            )
            self.assertIsInstance(box, Quartz.CGRect)
            box = Quartz.CGContextConvertRectToUserSpace(
                context, ((10.5, 11.9), (55.6, 39.3))
            )
            self.assertIsInstance(box, Quartz.CGRect)

            myInfo = object()

            def drawPattern(info, context):
                pass

            pattern = Quartz.CGPatternCreate(
                myInfo,
                Quartz.CGRectMake(0, 0, 10, 10),
                Quartz.CGAffineTransformIdentity,
                10.0,
                10.0,
                Quartz.kCGPatternTilingConstantSpacing,
                True,
                drawPattern,
            )
            self.assertIsInstance(pattern, Quartz.CGPatternRef)

            Quartz.CGContextSetFillColorSpace(
                context, Quartz.CGColorSpaceCreatePattern(None)
            )
            Quartz.CGContextSetStrokeColorSpace(
                context, Quartz.CGColorSpaceCreatePattern(None)
            )
            Quartz.CGContextSetFillPattern(context, pattern, (1.0, 1.0, 1.0, 1.0))
            Quartz.CGContextSetStrokePattern(context, pattern, (1.0, 1.0, 1.0, 1.0))

            fn = "/System/Library/CoreServices/DefaultDesktop.jpg"
            if not os.path.exists(fn):
                fn = "/System/Library/Automator/Apply ColorSync Profile to Images.action/Contents/Resources/A-1075-normal.jpg"
                if not os.path.exists(fn):
                    fn = "/System/Library/CoreServices//RemoteManagement/ARDAgent.app/Contents/Resources/Lock.jpg"

            with open(fn, "rb") as fp:
                data = fp.read()
            provider = Quartz.CGDataProviderCreateWithCFData(data)
            image = Quartz.CGImageCreateWithJPEGDataProvider(
                provider, None, True, Quartz.kCGRenderingIntentDefault
            )
            self.assertIsInstance(image, Quartz.CGImageRef)

            Quartz.CGContextDrawImage(context, ((0, 0), (70, 50)), image)

            provider = Quartz.CGDataProviderCreateWithCFData(b"1" * 4 * 20 * 10)
            mask = Quartz.CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
            self.assertIsInstance(mask, Quartz.CGImageRef)

            Quartz.CGContextClipToMask(context, Quartz.CGRectMake(0, 0, 50, 90), mask)

        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testGlyphFunctions(self):
        self.assertArgHasType(Quartz.CGContextShowGlyphsAtPositions, 1, b"n^S")
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphsAtPositions, 1, 3)
        self.assertArgHasType(
            Quartz.CGContextShowGlyphsAtPositions, 2, b"n^" + Quartz.CGPoint.__typestr__
        )
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphsAtPositions, 2, 3)

        self.assertArgHasType(Quartz.CGContextShowGlyphs, 1, b"n^S")
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphs, 1, 2)

        self.assertArgHasType(Quartz.CGContextShowGlyphsAtPoint, 1, objc._C_CGFloat)
        self.assertArgHasType(Quartz.CGContextShowGlyphsAtPoint, 2, objc._C_CGFloat)
        self.assertArgHasType(Quartz.CGContextShowGlyphsAtPoint, 3, b"n^S")
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphsAtPoint, 3, 4)

        self.assertArgHasType(Quartz.CGContextShowGlyphsWithAdvances, 1, b"n^S")
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphsWithAdvances, 1, 3)
        self.assertArgHasType(
            Quartz.CGContextShowGlyphsWithAdvances, 2, b"n^" + Quartz.CGSize.__typestr__
        )
        self.assertArgSizeInArg(Quartz.CGContextShowGlyphsWithAdvances, 2, 3)

        self.assertArgHasType(Quartz.CGContextDrawPDFPage, 0, b"^{CGContext=}")
        self.assertArgHasType(Quartz.CGContextDrawPDFPage, 1, b"^{CGPDFPage=}")

        self.assertArgHasType(Quartz.CGContextDrawPDFDocument, 0, b"^{CGContext=}")
        self.assertArgHasType(
            Quartz.CGContextDrawPDFDocument, 1, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(Quartz.CGContextDrawPDFDocument, 2, b"^{CGPDFDocument=}")
        self.assertArgHasType(Quartz.CGContextDrawPDFDocument, 3, objc._C_INT)

    @min_os_level("10.5")
    def testContextManager10_5(self):
        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        try:
            Quartz.CGContextBeginPage(context, objc.NULL)

            # XXX: This need actual tests, this at least tests that
            # the contextmanagers can be used
            with Quartz.CGTransparencyLayer(context, None):
                pass

            with Quartz.CGTransparencyLayer(context, None, ((10, 10), (200, 200))):
                pass

        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testContextManager(self):
        """
        Tests for some additional functionality
        """
        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        try:
            Quartz.CGContextBeginPage(context, objc.NULL)
            transform = Quartz.CGContextGetCTM(context)
            newTransform = Quartz.CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)

            with Quartz.CGSavedGState(context):
                Quartz.CGContextConcatCTM(context, newTransform)
                tf = Quartz.CGContextGetCTM(context)
                self.assertNotEqual(tf, transform)

            tf = Quartz.CGContextGetCTM(context)
            self.assertEqual(tf, transform)

            Quartz.CGContextEndPage(context)
            with Quartz.CGContextPage(context):
                pass

            with Quartz.CGContextPage(context, Quartz.CGRectMake(0, 0, 500, 500)):
                pass

            Quartz.CGContextBeginPage(context, None)

        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

    def testFunctions_n(self):
        Quartz.CGContextResetClip

    @min_os_level("14.0")
    def test_functions14_0(self):
        Quartz.CGContextDrawConicGradient
