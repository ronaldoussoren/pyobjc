
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz import CoreGraphics

class TestCGDirectDisplay (TestCase):

    def testConstants(self):
        self.failUnlessEqual(kCGNullDirectDisplay, 0)

        self.failUnlessEqual(kCGDisplayWidth, "Width")
        self.failUnlessEqual(kCGDisplayHeight, "Height")
        self.failUnlessEqual(kCGDisplayMode, "Mode")
        self.failUnlessEqual(kCGDisplayBitsPerPixel, "BitsPerPixel")
        self.failUnlessEqual(kCGDisplayBitsPerSample, "BitsPerSample")
        self.failUnlessEqual(kCGDisplaySamplesPerPixel, "SamplesPerPixel")
        self.failUnlessEqual(kCGDisplayRefreshRate, "RefreshRate")
        self.failUnlessEqual(kCGDisplayModeUsableForDesktopGUI, "UsableForDesktopGUI")
        self.failUnlessEqual(kCGDisplayIOFlags, "IOFlags")
        self.failUnlessEqual(kCGDisplayBytesPerRow, "kCGDisplayBytesPerRow")
        self.failUnlessEqual(kCGIODisplayModeID, "IODisplayModeID")

        self.failUnlessEqual(kCGDisplayModeIsSafeForHardware, "kCGDisplayModeIsSafeForHardware")
        self.failUnlessEqual(kCGDisplayModeIsInterlaced, "kCGDisplayModeIsInterlaced") 
        self.failUnlessEqual(kCGDisplayModeIsStretched, "kCGDisplayModeIsStretched")
        self.failUnlessEqual(kCGDisplayModeIsTelevisionOutput, "kCGDisplayModeIsTelevisionOutput" )

        self.failUnlessEqual(kCGCaptureNoOptions, 0)
        self.failUnlessEqual(kCGCaptureNoFill, 1)




        self.failIf(hasattr(CoreGraphics, 'kCGDirectMainDisplay'))

    def testFunctions(self):
        self.failUnlessIsInstance(CGMainDisplayID(), (int, long))

        self.failUnlessArgIsOut(CGGetDisplaysWithPoint, 2)
        self.failUnlessArgIsOut(CGGetDisplaysWithPoint, 3)
        v, ids, cnt = CGGetDisplaysWithPoint((0, 0), 10, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt)
        self.failUnlessEqual(len(ids), cnt)
        self.failUnlessIsInstance(ids[0], (int, long))

        self.failUnlessArgIsOut(CGGetDisplaysWithRect, 2)
        self.failUnlessArgIsOut(CGGetDisplaysWithRect, 3)
        v, ids, cnt = CGGetDisplaysWithRect(((0, 0), (400, 500)), 
                10, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt)
        self.failUnlessEqual(len(ids), cnt)
        self.failUnlessIsInstance(ids[0], (int, long))


        self.failUnlessArgIsOut(CGGetDisplaysWithOpenGLDisplayMask, 2)
        self.failUnlessArgIsOut(CGGetDisplaysWithOpenGLDisplayMask, 3)
        v, ids, cnt = CGGetDisplaysWithOpenGLDisplayMask(0xff,
                10, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt)
        self.failUnlessEqual(len(ids), cnt)
        self.failUnlessIsInstance(ids[0], (int, long))

        self.failUnlessArgIsOut(CGGetActiveDisplayList, 1)
        self.failUnlessArgIsOut(CGGetActiveDisplayList, 2)
        v, ids, cnt = CGGetActiveDisplayList(10, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt)
        self.failUnlessEqual(len(ids), cnt)
        self.failUnlessIsInstance(ids[0], (int, long))

        self.failUnlessArgIsOut(CGGetOnlineDisplayList, 1)
        self.failUnlessArgIsOut(CGGetOnlineDisplayList, 2)
        v, ids, cnt = CGGetOnlineDisplayList(10, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt)
        self.failUnlessEqual(len(ids), cnt)
        self.failUnlessIsInstance(ids[0], (int, long))

        v = CGDisplayIDToOpenGLDisplayMask(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))
        self.failIfEqual(v, 0)

        id = CGOpenGLDisplayMaskToDisplayID(v)
        self.failUnlessIsInstance(id, (int, long))
        self.failUnlessEqual(id, CGMainDisplayID())

        box = CGDisplayBounds(CGMainDisplayID())
        self.failUnlessIsInstance(box, CGRect)

        v = CGDisplayPixelsWide(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))
        v = CGDisplayPixelsHigh(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        modes = CGDisplayAvailableModes(CGMainDisplayID())
        self.failUnlessIsInstance(modes, CFArrayRef)
        self.failUnless(len(modes) > 0)
        self.failUnlessIsInstance(modes[0], CFDictionaryRef)

        v, exact = CGDisplayBestModeForParameters(CGMainDisplayID(),
                32, 800, 600, None)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failUnlessIsInstance(exact, (int, long))

        v, exact = CGDisplayBestModeForParametersAndRefreshRate(
                CGMainDisplayID(), 32, 800, 600, 70, None)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failUnlessIsInstance(exact, (int, long))

        v, exact = CGDisplayBestModeForParametersAndRefreshRateWithProperty(
                CGMainDisplayID(), 32, 800, 600, 70,
                kCGDisplayModeIsSafeForHardware, None)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failUnlessIsInstance(exact, (int, long))

        cur = CGDisplayCurrentMode(CGMainDisplayID())
        self.failUnlessIsInstance(cur, CFDictionaryRef)

        v = CGDisplaySwitchToMode(CGMainDisplayID(), v)
        self.failUnlessEqual(v, 0)
        v = CGDisplaySwitchToMode(CGMainDisplayID(), cur)
        self.failUnlessEqual(v, 0)

        v = CGDisplayBitsPerPixel(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayBitsPerSample(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplaySamplesPerPixel(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayBytesPerRow(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 1)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 2)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 3)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 4)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 5)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 6)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 7)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 8)
        self.failUnlessArgIsOut(CGGetDisplayTransferByFormula, 9)
        v = CGGetDisplayTransferByFormula(CGMainDisplayID(),
                None, None, None, None, None, None, None, None, None)
        self.failUnlessIsInstance(v[0], (int, long))
        for i in range(9):
            self.failUnlessIsInstance(v[i+1], float)

        v = CGSetDisplayTransferByFormula(CGMainDisplayID(), *v[1:])
        self.failUnlessEqual(v, 0)

        tablen = CGDisplayGammaTableCapacity(CGMainDisplayID())
        self.failUnlessIsInstance(tablen, (int, long))

        err, red, green, blue, count = CGGetDisplayTransferByTable(
                CGMainDisplayID(), tablen, None, None, None, None)
        self.failUnlessIsInstance(err, (int, long))
        self.failUnlessIsInstance(count, (int, long))
        self.failUnlessEqual(err, 0)
        self.failIfEqual(count, 0)

        err = CGSetDisplayTransferByTable(CGMainDisplayID(), count,
                red, green, blue)
        self.failUnlessEqual(err, 0)

        err, red, green, blue, count = CGGetDisplayTransferByTable(
                CGMainDisplayID(), tablen, None, None, None, None)
        self.failUnlessIsInstance(err, (int, long))
        self.failUnlessIsInstance(count, (int, long))
        self.failUnlessEqual(err, 0)
        self.failIfEqual(count, 0)

        err = CGSetDisplayTransferByTable(CGMainDisplayID(), count,
                red, green, blue)
        self.failUnlessEqual(err, 0)

        CGDisplayRestoreColorSyncSettings()

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.failUnlessIsInstance(v, int)
        self.failIf(v)

        err = CGDisplayCapture(CGMainDisplayID())
        self.failUnlessEqual(err, 0)

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.failUnless(v)

        err = CGDisplayRelease(CGMainDisplayID())
        self.failUnlessEqual(err, 0)

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.failIf(v)

        err = CGDisplayCaptureWithOptions(CGMainDisplayID(), 0)
        self.failUnlessEqual(err, 0)

        err = CGDisplayRelease(CGMainDisplayID())
        self.failUnlessEqual(err, 0)

        err = CGCaptureAllDisplays()
        self.failUnlessEqual(err, 0)

        ctx = CGDisplayGetDrawingContext(CGMainDisplayID())
        self.failUnlessIsInstance(ctx, CGContextRef)

        err = CGReleaseAllDisplays()
        self.failUnlessEqual(err, 0)

        err = CGCaptureAllDisplaysWithOptions(0)
        self.failUnlessEqual(err, 0)

        err = CGReleaseAllDisplays()
        self.failUnlessEqual(err, 0)
        
        v = CGShieldingWindowID(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGShieldingWindowLevel()
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayBaseAddress(CGMainDisplayID())
        self.failUnlessIsInstance(v, objc.varlist)
        self.failUnlessIsInstance(v[0], str)

        v = CGDisplayAddressForPosition(CGMainDisplayID(), 100, 100)
        self.failUnlessIsInstance(v, objc.varlist)
        self.failUnlessIsInstance(v[0], str)

        err = CGDisplayHideCursor(CGMainDisplayID())
        self.failUnlessEqual(err, 0)

        err = CGDisplayShowCursor(CGMainDisplayID())
        self.failUnlessEqual(err, 0)

        err = CGDisplayMoveCursorToPoint(CGMainDisplayID(), (100, 100))

        dX, dY = CGGetLastMouseDelta(None, None)
        self.failUnlessIsInstance(dX, (int, long))
        self.failUnlessIsInstance(dY, (int, long))

        v = CGDisplayCanSetPalette(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        err = CGDisplayWaitForBeamPositionOutsideLines(CGMainDisplayID(), 200, 400)
        self.failUnlessEqual(err, 0)

        v = CGDisplayBeamPosition(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        palette = CGPaletteCreateDefaultColorPalette()
        self.failUnlessIsInstance(palette, CGDirectPaletteRef)

        err = CGDisplaySetPalette(CGMainDisplayID(), palette)
        self.failUnlessIsInstance(err, (int, long))

if __name__ == "__main__":
    main()
