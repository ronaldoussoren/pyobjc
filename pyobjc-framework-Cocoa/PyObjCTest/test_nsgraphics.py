import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSGraphics(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSColorSpaceName, str)
        self.assertIsTypedEnum(AppKit.NSDeviceDescriptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSAnimationEffect)
        self.assertIsEnumType(AppKit.NSBackingStoreType)
        self.assertIsEnumType(AppKit.NSColorRenderingIntent)
        self.assertIsEnumType(AppKit.NSCompositingOperation)
        self.assertIsEnumType(AppKit.NSDisplayGamut)
        self.assertIsEnumType(AppKit.NSFocusRingPlacement)
        self.assertIsEnumType(AppKit.NSFocusRingType)
        self.assertIsEnumType(AppKit.NSWindowDepth)
        self.assertIsEnumType(AppKit.NSWindowOrderingMode)

    def testConstants(self):
        self.assertEqual(AppKit.NSCompositeClear, 0)
        self.assertEqual(AppKit.NSCompositeCopy, 1)
        self.assertEqual(AppKit.NSCompositeSourceOver, 2)
        self.assertEqual(AppKit.NSCompositeSourceIn, 3)
        self.assertEqual(AppKit.NSCompositeSourceOut, 4)
        self.assertEqual(AppKit.NSCompositeSourceAtop, 5)
        self.assertEqual(AppKit.NSCompositeDestinationOver, 6)
        self.assertEqual(AppKit.NSCompositeDestinationIn, 7)
        self.assertEqual(AppKit.NSCompositeDestinationOut, 8)
        self.assertEqual(AppKit.NSCompositeDestinationAtop, 9)
        self.assertEqual(AppKit.NSCompositeXOR, 10)
        self.assertEqual(AppKit.NSCompositePlusDarker, 11)
        self.assertEqual(AppKit.NSCompositeHighlight, 12)
        self.assertEqual(AppKit.NSCompositePlusLighter, 13)
        self.assertEqual(AppKit.NSCompositeMultiply, 14)
        self.assertEqual(AppKit.NSCompositeScreen, 15)
        self.assertEqual(AppKit.NSCompositeOverlay, 16)
        self.assertEqual(AppKit.NSCompositeDarken, 17)
        self.assertEqual(AppKit.NSCompositeLighten, 18)
        self.assertEqual(AppKit.NSCompositeColorDodge, 19)
        self.assertEqual(AppKit.NSCompositeColorBurn, 20)
        self.assertEqual(AppKit.NSCompositeSoftLight, 21)
        self.assertEqual(AppKit.NSCompositeHardLight, 22)
        self.assertEqual(AppKit.NSCompositeDifference, 23)
        self.assertEqual(AppKit.NSCompositeExclusion, 24)
        self.assertEqual(AppKit.NSCompositeHue, 25)
        self.assertEqual(AppKit.NSCompositeSaturation, 26)
        self.assertEqual(AppKit.NSCompositeColor, 27)
        self.assertEqual(AppKit.NSCompositeLuminosity, 28)

        self.assertEqual(AppKit.NSCompositingOperationClear, 0)
        self.assertEqual(AppKit.NSCompositingOperationCopy, 1)
        self.assertEqual(AppKit.NSCompositingOperationSourceOver, 2)
        self.assertEqual(AppKit.NSCompositingOperationSourceIn, 3)
        self.assertEqual(AppKit.NSCompositingOperationSourceOut, 4)
        self.assertEqual(AppKit.NSCompositingOperationSourceAtop, 5)
        self.assertEqual(AppKit.NSCompositingOperationDestinationOver, 6)
        self.assertEqual(AppKit.NSCompositingOperationDestinationIn, 7)
        self.assertEqual(AppKit.NSCompositingOperationDestinationOut, 8)
        self.assertEqual(AppKit.NSCompositingOperationDestinationAtop, 9)
        self.assertEqual(AppKit.NSCompositingOperationXOR, 10)
        self.assertEqual(AppKit.NSCompositingOperationPlusDarker, 11)
        self.assertEqual(AppKit.NSCompositingOperationHighlight, 12)
        self.assertEqual(AppKit.NSCompositingOperationPlusLighter, 13)
        self.assertEqual(AppKit.NSCompositingOperationMultiply, 14)
        self.assertEqual(AppKit.NSCompositingOperationScreen, 15)
        self.assertEqual(AppKit.NSCompositingOperationOverlay, 16)
        self.assertEqual(AppKit.NSCompositingOperationDarken, 17)
        self.assertEqual(AppKit.NSCompositingOperationLighten, 18)
        self.assertEqual(AppKit.NSCompositingOperationColorDodge, 19)
        self.assertEqual(AppKit.NSCompositingOperationColorBurn, 20)
        self.assertEqual(AppKit.NSCompositingOperationSoftLight, 21)
        self.assertEqual(AppKit.NSCompositingOperationHardLight, 22)
        self.assertEqual(AppKit.NSCompositingOperationDifference, 23)
        self.assertEqual(AppKit.NSCompositingOperationExclusion, 24)
        self.assertEqual(AppKit.NSCompositingOperationHue, 25)
        self.assertEqual(AppKit.NSCompositingOperationSaturation, 26)
        self.assertEqual(AppKit.NSCompositingOperationColor, 27)
        self.assertEqual(AppKit.NSCompositingOperationLuminosity, 28)

        self.assertEqual(AppKit.NSBackingStoreRetained, 0)
        self.assertEqual(AppKit.NSBackingStoreNonretained, 1)
        self.assertEqual(AppKit.NSBackingStoreBuffered, 2)

        self.assertEqual(AppKit.NSWindowAbove, 1)
        self.assertEqual(AppKit.NSWindowBelow, -1)
        self.assertEqual(AppKit.NSWindowOut, 0)

        self.assertEqual(AppKit.NSFocusRingOnly, 0)
        self.assertEqual(AppKit.NSFocusRingBelow, 1)
        self.assertEqual(AppKit.NSFocusRingAbove, 2)

        self.assertEqual(AppKit.NSFocusRingTypeDefault, 0)
        self.assertEqual(AppKit.NSFocusRingTypeNone, 1)
        self.assertEqual(AppKit.NSFocusRingTypeExterior, 2)

        self.assertIsInstance(AppKit.NSCalibratedWhiteColorSpace, str)
        self.assertIsInstance(AppKit.NSCalibratedBlackColorSpace, str)
        self.assertIsInstance(AppKit.NSCalibratedRGBColorSpace, str)
        self.assertIsInstance(AppKit.NSDeviceWhiteColorSpace, str)
        self.assertIsInstance(AppKit.NSDeviceBlackColorSpace, str)
        self.assertIsInstance(AppKit.NSDeviceRGBColorSpace, str)
        self.assertIsInstance(AppKit.NSDeviceCMYKColorSpace, str)
        self.assertIsInstance(AppKit.NSNamedColorSpace, str)
        self.assertIsInstance(AppKit.NSPatternColorSpace, str)
        self.assertIsInstance(AppKit.NSCustomColorSpace, str)
        self.assertIsInstance(AppKit.NSWhite, float)
        self.assertIsInstance(AppKit.NSLightGray, float)
        self.assertIsInstance(AppKit.NSDarkGray, float)
        self.assertIsInstance(AppKit.NSBlack, float)

        self.assertIsInstance(AppKit.NSDeviceResolution, str)
        self.assertIsInstance(AppKit.NSDeviceColorSpaceName, str)
        self.assertIsInstance(AppKit.NSDeviceBitsPerSample, str)
        self.assertIsInstance(AppKit.NSDeviceIsScreen, str)
        self.assertIsInstance(AppKit.NSDeviceIsPrinter, str)
        self.assertIsInstance(AppKit.NSDeviceSize, str)
        self.assertEqual(AppKit.NSAnimationEffectDisappearingItemDefault, 0)
        self.assertEqual(AppKit.NSAnimationEffectPoof, 10)

        self.assertEqual(AppKit.NSDisplayGamutSRGB, 1)
        self.assertEqual(AppKit.NSDisplayGamutP3, 2)

    def testFunctions(self):
        app = AppKit.NSApplication.sharedApplication()  # noqa: F841

        self.assertArgHasType(AppKit.NSBestDepth, 4, b"o^" + objc._C_NSBOOL)
        self.assertArgIsBOOL(AppKit.NSBestDepth, 3)
        d, e = AppKit.NSBestDepth(AppKit.NSDeviceRGBColorSpace, 8, 32, False, None)
        self.assertIsInstance(d, int)
        self.assertIsInstance(e, bool)

        self.assertResultIsBOOL(AppKit.NSPlanarFromDepth)
        self.assertIsInstance(AppKit.NSPlanarFromDepth(0), bool)

        self.assertIsInstance(AppKit.NSColorSpaceFromDepth(0), str)
        self.assertIsInstance(AppKit.NSBitsPerSampleFromDepth(0), int)
        self.assertIsInstance(AppKit.NSBitsPerPixelFromDepth(0), int)
        self.assertIsInstance(
            AppKit.NSNumberOfColorComponents(AppKit.NSDeviceRGBColorSpace), int
        )

        v = AppKit.NSAvailableWindowDepths()
        self.assertIsInstance(v, tuple)
        self.assertNotEqual(len(v), 0)
        self.assertIsInstance(v[0], int)

        img = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None, 255, 255, 8, 4, True, False, AppKit.NSCalibratedRGBColorSpace, 0, 0, 0
        )

        context = AppKit.NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        current = AppKit.NSGraphicsContext.currentContext()
        try:
            AppKit.NSGraphicsContext.setCurrentContext_(context)
            AppKit.NSRectFill(((0, 0), (1, 2)))

            self.assertArgSizeInArg(AppKit.NSRectFillList, 0, 1)
            AppKit.NSRectFillList([((0, 0), (1, 2)), ((10, 50), (9, 9))], 2)

            self.assertArgSizeInArg(AppKit.NSRectFillListWithGrays, 0, 2)
            self.assertArgSizeInArg(AppKit.NSRectFillListWithGrays, 1, 2)
            AppKit.NSRectFillListWithGrays(
                [((0, 0), (1, 2)), ((10, 50), (9, 9))], (0.5, 0.6), 2
            )

            self.assertArgSizeInArg(AppKit.NSRectFillListWithColors, 0, 2)
            self.assertArgSizeInArg(AppKit.NSRectFillListWithColors, 1, 2)
            AppKit.NSRectFillListWithColors(
                [((0, 0), (1, 2)), ((10, 50), (9, 9))],
                (AppKit.NSColor.blueColor(), AppKit.NSColor.redColor()),
                2,
            )

            AppKit.NSRectFillUsingOperation(
                ((0, 0), (1, 2)), AppKit.NSCompositeSourceOver
            )

            self.assertArgSizeInArg(AppKit.NSRectFillListUsingOperation, 0, 1)
            AppKit.NSRectFillListUsingOperation(
                [((0, 0), (1, 2)), ((10, 50), (9, 9))], 2, AppKit.NSCompositeSourceOver
            )

            self.assertArgSizeInArg(AppKit.NSRectFillListWithColorsUsingOperation, 0, 2)
            self.assertArgSizeInArg(AppKit.NSRectFillListWithColorsUsingOperation, 1, 2)
            AppKit.NSRectFillListWithColorsUsingOperation(
                [((0, 0), (1, 2)), ((10, 50), (9, 9))],
                (AppKit.NSColor.blueColor(), AppKit.NSColor.redColor()),
                2,
                AppKit.NSCompositeSourceOver,
            )

            AppKit.NSFrameRect(((5, 5), (20, 30)))
            AppKit.NSFrameRectWithWidth(((5, 5), (20, 30)), 4)
            AppKit.NSFrameRectWithWidthUsingOperation(
                ((5, 5), (20, 30)), 4, AppKit.NSCompositeSourceOver
            )

            AppKit.NSRectClip(((5, 5), (200, 200)))
            self.assertArgSizeInArg(AppKit.NSRectClipList, 0, 1)
            AppKit.NSRectClipList([((5, 5), (200, 200)), ((50, 50), (90, 100))], 2)

            color = AppKit.NSReadPixel((5, 5))
            self.assertIsInstance(color, AppKit.NSColor)

            self.assertArgSizeInArg(AppKit.NSDrawTiledRects, 2, 4)
            self.assertArgSizeInArg(AppKit.NSDrawTiledRects, 3, 4)
            self.assertArgIsIn(AppKit.NSDrawTiledRects, 2)
            self.assertArgIsIn(AppKit.NSDrawTiledRects, 3)
            AppKit.NSDrawTiledRects(
                ((10, 10), (50, 50)),
                ((15, 15), (10, 10)),
                [AppKit.NSMinXEdge, AppKit.NSMaxXEdge],
                [0.8, 0.9],
                2,
            )

            AppKit.NSDrawGrayBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSDrawGroove(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSDrawWhiteBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSDrawButton(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSEraseRect(((0, 0), (10, 10)))
            AppKit.NSCopyBits(0, ((10, 10), (50, 50)), (50, 50))
            AppKit.NSHighlightRect(((10, 10), (50, 50)))
            AppKit.NSDrawDarkBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSDrawLightBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            AppKit.NSDottedFrameRect(((10, 10), (50, 50)))
            AppKit.NSDrawWindowBackground(((10, 10), (50, 50)))

        finally:
            AppKit.NSGraphicsContext.setCurrentContext_(current)

            AppKit.NSSetFocusRingStyle(AppKit.NSFocusRingAbove)

            self.assertArgIsOut(AppKit.NSGetWindowServerMemory, 1)
            self.assertArgIsOut(AppKit.NSGetWindowServerMemory, 2)
            self.assertArgIsOut(AppKit.NSGetWindowServerMemory, 3)
            r = AppKit.NSGetWindowServerMemory(0, None, None, None)
            self.assertIsInstance(r[0], int)
            self.assertIsInstance(r[1], int)
            self.assertIsInstance(r[2], int)

            self.assertArgSizeInArg(AppKit.NSDrawColorTiledRects, 2, 4)
            self.assertArgSizeInArg(AppKit.NSDrawColorTiledRects, 3, 4)
            self.assertArgIsIn(AppKit.NSDrawColorTiledRects, 2)
            self.assertArgIsIn(AppKit.NSDrawColorTiledRects, 3)
            AppKit.NSDrawColorTiledRects(
                ((10, 10), (50, 50)),
                ((15, 15), (10, 10)),
                [AppKit.NSMinXEdge, AppKit.NSMaxXEdge],
                [AppKit.NSColor.redColor(), AppKit.NSColor.blueColor()],
                2,
            )

            # self.assertArgIsBOOL(AppKit.NSDrawBitmap, 7)
            # self.assertArgIsBOOL(AppKit.NSDrawBitmap, 8)
            # AppKit.NSDrawBitmap(((0, 0), (10, 10)), 10, 20, 8, 4, 32, 40, False, True,
            #        AppKit.NSDeviceRGBColorSpace, [' '*4*10*20, '', '', '', ''])

            self.assertArgSizeInArg(AppKit.NSWindowList, 1, 0)
            self.assertArgIsOut(AppKit.NSWindowList, 1)
            v = AppKit.NSWindowList(5, None)
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 5)
            self.assertIsInstance(v[0], int)

            self.assertArgIsOut(AppKit.NSCountWindowsForContext, 1)
            v = AppKit.NSCountWindowsForContext(1, None)
            self.assertIsInstance(v, int)

            self.assertArgIsOut(AppKit.NSWindowListForContext, 2)
            self.assertArgSizeInArg(AppKit.NSWindowListForContext, 2, 1)
            v = AppKit.NSWindowListForContext(0, 5, None)
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 5)
            self.assertIsInstance(v[0], int)

        del img
        del context
        AppKit.NSBeep()
        count = AppKit.NSCountWindows(None)
        self.assertIsInstance(count, int)

        try:
            AppKit.NSDisableScreenUpdates()
        except objc.error:
            pass

        try:
            AppKit.NSEnableScreenUpdates()
        except objc.error:
            pass
        self.assertArgIsSEL(AppKit.NSShowAnimationEffect, 4, b"v@:^v")
        self.assertArgHasType(AppKit.NSShowAnimationEffect, 5, b"^v")
        try:
            AppKit.NSShowAnimationEffect(
                AppKit.NSAnimationEffectPoof, (10, 10), (20, 30), None, None, None
            )
        except objc.error:
            pass

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSColorRenderingIntentDefault, 0)
        self.assertEqual(AppKit.NSColorRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(AppKit.NSColorRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(AppKit.NSColorRenderingIntentPerceptual, 3)
        self.assertEqual(AppKit.NSColorRenderingIntentSaturation, 4)

        self.assertEqual(AppKit.NSImageInterpolationDefault, 0)
        self.assertEqual(AppKit.NSImageInterpolationNone, 1)
        self.assertEqual(AppKit.NSImageInterpolationLow, 2)
        self.assertEqual(AppKit.NSImageInterpolationHigh, 3)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSWindowDepthTwentyfourBitRGB, 0x208)
        self.assertEqual(AppKit.NSWindowDepthSixtyfourBitRGB, 0x210)
        self.assertEqual(AppKit.NSWindowDepthOnehundredtwentyeightBitRGB, 0x220)

        self.assertEqual(AppKit.NSImageInterpolationMedium, 4)

    AppKit.NSApplication.sharedApplication()
