
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGraphics (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSCompositeClear, 0)
        self.failUnlessEqual(NSCompositeCopy, 1)
        self.failUnlessEqual(NSCompositeSourceOver, 2)
        self.failUnlessEqual(NSCompositeSourceIn, 3)
        self.failUnlessEqual(NSCompositeSourceOut, 4)
        self.failUnlessEqual(NSCompositeSourceAtop, 5)
        self.failUnlessEqual(NSCompositeDestinationOver, 6)
        self.failUnlessEqual(NSCompositeDestinationIn, 7)
        self.failUnlessEqual(NSCompositeDestinationOut, 8)
        self.failUnlessEqual(NSCompositeDestinationAtop, 9)
        self.failUnlessEqual(NSCompositeXOR, 10)
        self.failUnlessEqual(NSCompositePlusDarker, 11)
        self.failUnlessEqual(NSCompositeHighlight, 12)
        self.failUnlessEqual(NSCompositePlusLighter, 13)
        self.failUnlessEqual(NSBackingStoreRetained, 0)
        self.failUnlessEqual(NSBackingStoreNonretained, 1)
        self.failUnlessEqual(NSBackingStoreBuffered, 2)
        self.failUnlessEqual(NSWindowAbove,  1)
        self.failUnlessEqual(NSWindowBelow, -1)
        self.failUnlessEqual(NSWindowOut,  0)
        self.failUnlessEqual(NSFocusRingOnly, 0)
        self.failUnlessEqual(NSFocusRingBelow, 1)
        self.failUnlessEqual(NSFocusRingAbove, 2)
        self.failUnlessEqual(NSFocusRingTypeDefault, 0)
        self.failUnlessEqual(NSFocusRingTypeNone, 1)
        self.failUnlessEqual(NSFocusRingTypeExterior, 2)

        self.failUnlessIsInstance(NSCalibratedWhiteColorSpace, unicode)
        self.failUnlessIsInstance(NSCalibratedBlackColorSpace, unicode)
        self.failUnlessIsInstance(NSCalibratedRGBColorSpace, unicode)
        self.failUnlessIsInstance(NSDeviceWhiteColorSpace, unicode)
        self.failUnlessIsInstance(NSDeviceBlackColorSpace, unicode)
        self.failUnlessIsInstance(NSDeviceRGBColorSpace, unicode)
        self.failUnlessIsInstance(NSDeviceCMYKColorSpace, unicode)
        self.failUnlessIsInstance(NSNamedColorSpace, unicode)
        self.failUnlessIsInstance(NSPatternColorSpace, unicode)
        self.failUnlessIsInstance(NSCustomColorSpace, unicode)
        self.failUnlessIsInstance(NSWhite, float)
        self.failUnlessIsInstance(NSLightGray, float)
        self.failUnlessIsInstance(NSDarkGray, float)
        self.failUnlessIsInstance(NSBlack, float)

        self.failUnlessIsInstance(NSDeviceResolution, unicode)
        self.failUnlessIsInstance(NSDeviceColorSpaceName, unicode)
        self.failUnlessIsInstance(NSDeviceBitsPerSample, unicode)
        self.failUnlessIsInstance(NSDeviceIsScreen, unicode)
        self.failUnlessIsInstance(NSDeviceIsPrinter, unicode)
        self.failUnlessIsInstance(NSDeviceSize, unicode)
        self.failUnlessEqual(NSAnimationEffectDisappearingItemDefault, 0)
        self.failUnlessEqual(NSAnimationEffectPoof, 10)


    def testFunctions(self):
        app = NSApplication.sharedApplication()

        self.failUnlessArgHasType(NSBestDepth, 4, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsBOOL(NSBestDepth, 3)
        d, e = NSBestDepth(NSDeviceRGBColorSpace, 8, 32, False, None)
        self.failUnlessIsInstance(d, (int, long))
        self.failUnlessIsInstance(e, bool)

        self.failUnlessResultIsBOOL(NSPlanarFromDepth)
        self.failUnlessIsInstance(NSPlanarFromDepth(0), bool)

        self.failUnlessIsInstance(NSColorSpaceFromDepth(0), unicode)
        self.failUnlessIsInstance(NSBitsPerSampleFromDepth(0), (int, long))
        self.failUnlessIsInstance(NSBitsPerPixelFromDepth(0), (int, long))
        self.failUnlessIsInstance(NSNumberOfColorComponents(NSDeviceRGBColorSpace), (int, long))

        v = NSAvailableWindowDepths()
        self.failUnlessIsInstance(v, tuple)
        self.failIfEqual(len(v), 0)
        self.failUnlessIsInstance(v[0], int)

        img = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(
                None, 255, 255, 8, 4, True, False, NSCalibratedRGBColorSpace, 0, 0, 0)
        context = NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        current = NSGraphicsContext.currentContext()
        try:
            NSGraphicsContext.setCurrentContext_(context)
            NSRectFill(((0, 0), (1, 2)))

            self.failUnlessArgSizeInArg(NSRectFillList, 0, 1)
            NSRectFillList([((0, 0), (1, 2)), ((10, 50), (9, 9))], 2)

            self.failUnlessArgSizeInArg(NSRectFillListWithGrays, 0, 2)
            self.failUnlessArgSizeInArg(NSRectFillListWithGrays, 1, 2)
            NSRectFillListWithGrays([((0, 0), (1, 2)), ((10, 50), (9, 9))], (0.5, 0.6), 2)

            self.failUnlessArgSizeInArg(NSRectFillListWithColors, 0, 2)
            self.failUnlessArgSizeInArg(NSRectFillListWithColors, 1, 2)
            NSRectFillListWithColors([((0, 0), (1, 2)), ((10, 50), (9, 9))], (NSColor.blueColor(), NSColor.redColor()), 2)

            NSRectFillUsingOperation(((0, 0), (1, 2)), NSCompositeSourceOver)

            self.failUnlessArgSizeInArg(NSRectFillListUsingOperation, 0, 1)
            NSRectFillListUsingOperation([((0, 0), (1, 2)), ((10, 50), (9, 9))], 2, NSCompositeSourceOver)

            self.failUnlessArgSizeInArg(NSRectFillListWithColorsUsingOperation, 0, 2)
            self.failUnlessArgSizeInArg(NSRectFillListWithColorsUsingOperation, 1, 2)
            NSRectFillListWithColorsUsingOperation([((0, 0), (1, 2)), ((10, 50), (9, 9))], (NSColor.blueColor(), NSColor.redColor()), 2, NSCompositeSourceOver)

            NSFrameRect(((5, 5), (20, 30)))
            NSFrameRectWithWidth(((5, 5), (20, 30)), 4)
            NSFrameRectWithWidthUsingOperation(((5, 5), (20, 30)), 4, NSCompositeSourceOver)

            NSRectClip(((5, 5), (200, 200)))
            self.failUnlessArgSizeInArg(NSRectClipList, 0, 1)
            NSRectClipList([((5, 5), (200, 200)), ((50, 50), (90, 100))], 2)

            color = NSReadPixel((5, 5))
            self.failUnlessIsInstance(color, NSColor)

            self.failUnlessArgSizeInArg(NSDrawTiledRects, 2, 4)
            self.failUnlessArgSizeInArg(NSDrawTiledRects, 3, 4)
            self.failUnlessArgIsIn(NSDrawTiledRects, 2)
            self.failUnlessArgIsIn(NSDrawTiledRects, 3)
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

            self.failUnlessArgIsOut(NSGetWindowServerMemory, 1)
            self.failUnlessArgIsOut(NSGetWindowServerMemory, 2)
            self.failUnlessArgIsOut(NSGetWindowServerMemory, 3)
            r = NSGetWindowServerMemory(0, None, None, None)
            self.failUnlessIsInstance(r[0], (int, long))
            self.failUnlessIsInstance(r[1], (int, long))
            self.failUnlessIsInstance(r[2], (int, long))

            self.failUnlessArgSizeInArg(NSDrawColorTiledRects, 2, 4)
            self.failUnlessArgSizeInArg(NSDrawColorTiledRects, 3, 4)
            self.failUnlessArgIsIn(NSDrawColorTiledRects, 2)
            self.failUnlessArgIsIn(NSDrawColorTiledRects, 3)
            NSDrawColorTiledRects(((10, 10), (50, 50)), ((15, 15), (10, 10)),  [NSMinXEdge, NSMaxXEdge], [NSColor.redColor(), NSColor.blueColor()], 2)

            #self.failUnlessArgIsBOOL(NSDrawBitmap, 7)
            #self.failUnlessArgIsBOOL(NSDrawBitmap, 8)
            #NSDrawBitmap(((0, 0), (10, 10)), 10, 20, 8, 4, 32, 40, False, True, 
            #        NSDeviceRGBColorSpace, [' '*4*10*20, '', '', '', ''])

            self.failUnlessArgSizeInArg(NSWindowList, 1, 0)
            self.failUnlessArgIsOut(NSWindowList, 1)
            v = NSWindowList(5, None)
            self.failUnlessIsInstance(v, tuple)
            self.failUnlessEqual(len(v), 5)
            self.failUnlessIsInstance(v[0], (int, long))

            self.failUnlessArgIsOut(NSCountWindowsForContext, 1)
            v = NSCountWindowsForContext(1, None)
            self.failUnlessIsInstance(v, (int, long))

            self.failUnlessArgIsOut(NSWindowListForContext, 2)
            self.failUnlessArgSizeInArg(NSWindowListForContext, 2, 1)
            v = NSWindowListForContext(0, 5, None)
            self.failUnlessIsInstance(v, tuple)
            self.failUnlessEqual(len(v), 5)
            self.failUnlessIsInstance(v[0], (int, long))




        NSBeep()
        count = NSCountWindows(None)
        self.failUnlessIsInstance(count, (int, long))

        try:
            NSDisableScreenUpdates()
        except objc.error:
            pass

        try:
            NSEnableScreenUpdates()
        except objc.error:
            pass

        self.failUnlessArgIsSEL(NSShowAnimationEffect, 4, 'v@:^v')
        self.failUnlessArgHasType(NSShowAnimationEffect, 5, '^v')
        try:
            NSShowAnimationEffect(NSAnimationEffectPoof, (10, 10), (20, 30), None, None, None)
        except objc.error:
            pass


if __name__ == "__main__":
    main()
