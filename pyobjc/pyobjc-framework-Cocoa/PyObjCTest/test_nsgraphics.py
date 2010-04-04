
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGraphics (TestCase):
    def testConstants(self):
        self.assertEqual(NSCompositeClear, 0)
        self.assertEqual(NSCompositeCopy, 1)
        self.assertEqual(NSCompositeSourceOver, 2)
        self.assertEqual(NSCompositeSourceIn, 3)
        self.assertEqual(NSCompositeSourceOut, 4)
        self.assertEqual(NSCompositeSourceAtop, 5)
        self.assertEqual(NSCompositeDestinationOver, 6)
        self.assertEqual(NSCompositeDestinationIn, 7)
        self.assertEqual(NSCompositeDestinationOut, 8)
        self.assertEqual(NSCompositeDestinationAtop, 9)
        self.assertEqual(NSCompositeXOR, 10)
        self.assertEqual(NSCompositePlusDarker, 11)
        self.assertEqual(NSCompositeHighlight, 12)
        self.assertEqual(NSCompositePlusLighter, 13)
        self.assertEqual(NSBackingStoreRetained, 0)
        self.assertEqual(NSBackingStoreNonretained, 1)
        self.assertEqual(NSBackingStoreBuffered, 2)
        self.assertEqual(NSWindowAbove,  1)
        self.assertEqual(NSWindowBelow, -1)
        self.assertEqual(NSWindowOut,  0)
        self.assertEqual(NSFocusRingOnly, 0)
        self.assertEqual(NSFocusRingBelow, 1)
        self.assertEqual(NSFocusRingAbove, 2)
        self.assertEqual(NSFocusRingTypeDefault, 0)
        self.assertEqual(NSFocusRingTypeNone, 1)
        self.assertEqual(NSFocusRingTypeExterior, 2)

        self.assertIsInstance(NSCalibratedWhiteColorSpace, unicode)
        self.assertIsInstance(NSCalibratedBlackColorSpace, unicode)
        self.assertIsInstance(NSCalibratedRGBColorSpace, unicode)
        self.assertIsInstance(NSDeviceWhiteColorSpace, unicode)
        self.assertIsInstance(NSDeviceBlackColorSpace, unicode)
        self.assertIsInstance(NSDeviceRGBColorSpace, unicode)
        self.assertIsInstance(NSDeviceCMYKColorSpace, unicode)
        self.assertIsInstance(NSNamedColorSpace, unicode)
        self.assertIsInstance(NSPatternColorSpace, unicode)
        self.assertIsInstance(NSCustomColorSpace, unicode)
        self.assertIsInstance(NSWhite, float)
        self.assertIsInstance(NSLightGray, float)
        self.assertIsInstance(NSDarkGray, float)
        self.assertIsInstance(NSBlack, float)

        self.assertIsInstance(NSDeviceResolution, unicode)
        self.assertIsInstance(NSDeviceColorSpaceName, unicode)
        self.assertIsInstance(NSDeviceBitsPerSample, unicode)
        self.assertIsInstance(NSDeviceIsScreen, unicode)
        self.assertIsInstance(NSDeviceIsPrinter, unicode)
        self.assertIsInstance(NSDeviceSize, unicode)
        self.assertEqual(NSAnimationEffectDisappearingItemDefault, 0)
        self.assertEqual(NSAnimationEffectPoof, 10)


    def testFunctions(self):
        app = NSApplication.sharedApplication()

        self.assertArgHasType(NSBestDepth, 4, b'o^' + objc._C_NSBOOL)
        self.assertArgIsBOOL(NSBestDepth, 3)
        d, e = NSBestDepth(NSDeviceRGBColorSpace, 8, 32, False, None)
        self.assertIsInstance(d, (int, long))
        self.assertIsInstance(e, bool)

        self.assertResultIsBOOL(NSPlanarFromDepth)
        self.assertIsInstance(NSPlanarFromDepth(0), bool)

        self.assertIsInstance(NSColorSpaceFromDepth(0), unicode)
        self.assertIsInstance(NSBitsPerSampleFromDepth(0), (int, long))
        self.assertIsInstance(NSBitsPerPixelFromDepth(0), (int, long))
        self.assertIsInstance(NSNumberOfColorComponents(NSDeviceRGBColorSpace), (int, long))

        v = NSAvailableWindowDepths()
        self.assertIsInstance(v, tuple)
        self.assertNotEqual(len(v), 0)
        self.assertIsInstance(v[0], int)

        img = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(
                None, 255, 255, 8, 4, True, False, NSCalibratedRGBColorSpace, 0, 0, 0)
        context = NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        current = NSGraphicsContext.currentContext()
        try:
            NSGraphicsContext.setCurrentContext_(context)
            NSRectFill(((0, 0), (1, 2)))

            self.assertArgSizeInArg(NSRectFillList, 0, 1)
            NSRectFillList([((0, 0), (1, 2)), ((10, 50), (9, 9))], 2)

            self.assertArgSizeInArg(NSRectFillListWithGrays, 0, 2)
            self.assertArgSizeInArg(NSRectFillListWithGrays, 1, 2)
            NSRectFillListWithGrays([((0, 0), (1, 2)), ((10, 50), (9, 9))], (0.5, 0.6), 2)

            self.assertArgSizeInArg(NSRectFillListWithColors, 0, 2)
            self.assertArgSizeInArg(NSRectFillListWithColors, 1, 2)
            NSRectFillListWithColors([((0, 0), (1, 2)), ((10, 50), (9, 9))], (NSColor.blueColor(), NSColor.redColor()), 2)

            NSRectFillUsingOperation(((0, 0), (1, 2)), NSCompositeSourceOver)

            self.assertArgSizeInArg(NSRectFillListUsingOperation, 0, 1)
            NSRectFillListUsingOperation([((0, 0), (1, 2)), ((10, 50), (9, 9))], 2, NSCompositeSourceOver)

            self.assertArgSizeInArg(NSRectFillListWithColorsUsingOperation, 0, 2)
            self.assertArgSizeInArg(NSRectFillListWithColorsUsingOperation, 1, 2)
            NSRectFillListWithColorsUsingOperation([((0, 0), (1, 2)), ((10, 50), (9, 9))], (NSColor.blueColor(), NSColor.redColor()), 2, NSCompositeSourceOver)

            NSFrameRect(((5, 5), (20, 30)))
            NSFrameRectWithWidth(((5, 5), (20, 30)), 4)
            NSFrameRectWithWidthUsingOperation(((5, 5), (20, 30)), 4, NSCompositeSourceOver)

            NSRectClip(((5, 5), (200, 200)))
            self.assertArgSizeInArg(NSRectClipList, 0, 1)
            NSRectClipList([((5, 5), (200, 200)), ((50, 50), (90, 100))], 2)

            color = NSReadPixel((5, 5))
            self.assertIsInstance(color, NSColor)

            self.assertArgSizeInArg(NSDrawTiledRects, 2, 4)
            self.assertArgSizeInArg(NSDrawTiledRects, 3, 4)
            self.assertArgIsIn(NSDrawTiledRects, 2)
            self.assertArgIsIn(NSDrawTiledRects, 3)
            NSDrawTiledRects(((10, 10), (50, 50)), ((15, 15), (10, 10)),  [NSMinXEdge, NSMaxXEdge], [0.8, 0.9], 2)

            NSDrawGrayBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSDrawGroove(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSDrawWhiteBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSDrawButton(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSEraseRect(((0, 0), (10, 10)))
            NSCopyBits(0, ((10, 10), (50, 50)), (50, 50))
            NSHighlightRect(((10, 10), (50, 50)))
            NSDrawDarkBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSDrawLightBezel(((0, 0), (10, 10)), ((0, 0), (50, 50)))
            NSDottedFrameRect(((10, 10), (50, 50)))
            NSDrawWindowBackground(((10, 10), (50, 50)))

        finally:
            NSGraphicsContext.setCurrentContext_(current)

            NSSetFocusRingStyle(NSFocusRingAbove)

            self.assertArgIsOut(NSGetWindowServerMemory, 1)
            self.assertArgIsOut(NSGetWindowServerMemory, 2)
            self.assertArgIsOut(NSGetWindowServerMemory, 3)
            r = NSGetWindowServerMemory(0, None, None, None)
            self.assertIsInstance(r[0], (int, long))
            self.assertIsInstance(r[1], (int, long))
            self.assertIsInstance(r[2], (int, long))

            self.assertArgSizeInArg(NSDrawColorTiledRects, 2, 4)
            self.assertArgSizeInArg(NSDrawColorTiledRects, 3, 4)
            self.assertArgIsIn(NSDrawColorTiledRects, 2)
            self.assertArgIsIn(NSDrawColorTiledRects, 3)
            NSDrawColorTiledRects(((10, 10), (50, 50)), ((15, 15), (10, 10)),  [NSMinXEdge, NSMaxXEdge], [NSColor.redColor(), NSColor.blueColor()], 2)

            #self.assertArgIsBOOL(NSDrawBitmap, 7)
            #self.assertArgIsBOOL(NSDrawBitmap, 8)
            #NSDrawBitmap(((0, 0), (10, 10)), 10, 20, 8, 4, 32, 40, False, True, 
            #        NSDeviceRGBColorSpace, [' '*4*10*20, '', '', '', ''])

            self.assertArgSizeInArg(NSWindowList, 1, 0)
            self.assertArgIsOut(NSWindowList, 1)
            v = NSWindowList(5, None)
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 5)
            self.assertIsInstance(v[0], (int, long))

            self.assertArgIsOut(NSCountWindowsForContext, 1)
            v = NSCountWindowsForContext(1, None)
            self.assertIsInstance(v, (int, long))

            self.assertArgIsOut(NSWindowListForContext, 2)
            self.assertArgSizeInArg(NSWindowListForContext, 2, 1)
            v = NSWindowListForContext(0, 5, None)
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 5)
            self.assertIsInstance(v[0], (int, long))




        NSBeep()
        count = NSCountWindows(None)
        self.assertIsInstance(count, (int, long))

        try:
            NSDisableScreenUpdates()
        except objc.error:
            pass

        try:
            NSEnableScreenUpdates()
        except objc.error:
            pass

        self.assertArgIsSEL(NSShowAnimationEffect, 4, b'v@:^v')
        self.assertArgHasType(NSShowAnimationEffect, 5, b'^v')
        try:
            NSShowAnimationEffect(NSAnimationEffectPoof, (10, 10), (20, 30), None, None, None)
        except objc.error:
            pass

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(NSColorRenderingIntentDefault, 0)
        self.assertEqual(NSColorRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(NSColorRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(NSColorRenderingIntentPerceptual, 3)
        self.assertEqual(NSColorRenderingIntentSaturation, 4)

        self.assertEqual(NSImageInterpolationDefault, 0)
        self.assertEqual(NSImageInterpolationNone, 1)
        self.assertEqual(NSImageInterpolationLow, 2)
        self.assertEqual(NSImageInterpolationHigh, 3)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSWindowDepthTwentyfourBitRGB, 0x208)
        self.assertEqual(NSWindowDepthSixtyfourBitRGB, 0x210)
        self.assertEqual(NSWindowDepthOnehundredtwentyeightBitRGB, 0x220)

        self.assertEqual(NSImageInterpolationMedium, 4)


if __name__ == "__main__":
    NSApplication.sharedApplication()
    main()
