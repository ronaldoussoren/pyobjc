
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz import CoreGraphics

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestCGDirectDisplay (TestCase):

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCGDisplayShowDuplicateLowResolutionModes, unicode)

    @min_os_level('10.8')
    def testFunctions10_8(self):
        mainID = CGMainDisplayID()
        mode = CGDisplayCopyDisplayMode(mainID)
        self.assertIsInstance(mode, CGDisplayModeRef)

        w = CGDisplayModeGetPixelWidth(mode)
        self.assertIsInstance(w, (int, long))

        h = CGDisplayModeGetPixelHeight(mode)
        self.assertIsInstance(h, (int, long))

    def testConstants(self):
        self.assertEqual(kCGNullDirectDisplay, 0)

        self.assertEqual(kCGDisplayWidth, "Width")
        self.assertEqual(kCGDisplayHeight, "Height")
        self.assertEqual(kCGDisplayMode, "Mode")
        self.assertEqual(kCGDisplayBitsPerPixel, "BitsPerPixel")
        self.assertEqual(kCGDisplayBitsPerSample, "BitsPerSample")
        self.assertEqual(kCGDisplaySamplesPerPixel, "SamplesPerPixel")
        self.assertEqual(kCGDisplayRefreshRate, "RefreshRate")
        self.assertEqual(kCGDisplayModeUsableForDesktopGUI, "UsableForDesktopGUI")
        self.assertEqual(kCGDisplayIOFlags, "IOFlags")
        self.assertEqual(kCGDisplayBytesPerRow, "kCGDisplayBytesPerRow")
        self.assertEqual(kCGIODisplayModeID, "IODisplayModeID")

        self.assertEqual(kCGDisplayModeIsSafeForHardware, "kCGDisplayModeIsSafeForHardware")
        self.assertEqual(kCGDisplayModeIsInterlaced, "kCGDisplayModeIsInterlaced")
        self.assertEqual(kCGDisplayModeIsStretched, "kCGDisplayModeIsStretched")
        self.assertEqual(kCGDisplayModeIsTelevisionOutput, "kCGDisplayModeIsTelevisionOutput" )

        self.assertEqual(kCGCaptureNoOptions, 0)
        self.assertEqual(kCGCaptureNoFill, 1)

        self.assertNotHasAttr(CoreGraphics, 'kCGDirectMainDisplay')

    def testFunctions(self):
        self.assertIsInstance(CGMainDisplayID(), (int, long))

        self.assertArgIsOut(CGGetDisplaysWithPoint, 2)
        self.assertArgIsOut(CGGetDisplaysWithPoint, 3)
        v, ids, cnt = CGGetDisplaysWithPoint((0, 0), 10, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(cnt, (int, long))
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], (int, long))

        self.assertArgIsOut(CGGetDisplaysWithRect, 2)
        self.assertArgIsOut(CGGetDisplaysWithRect, 3)
        v, ids, cnt = CGGetDisplaysWithRect(((0, 0), (400, 500)),
                10, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(cnt, (int, long))
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], (int, long))


        self.assertArgIsOut(CGGetDisplaysWithOpenGLDisplayMask, 2)
        self.assertArgIsOut(CGGetDisplaysWithOpenGLDisplayMask, 3)
        v, ids, cnt = CGGetDisplaysWithOpenGLDisplayMask(0xff,
                10, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(cnt, (int, long))
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], (int, long))

        self.assertArgIsOut(CGGetActiveDisplayList, 1)
        self.assertArgIsOut(CGGetActiveDisplayList, 2)
        v, ids, cnt = CGGetActiveDisplayList(10, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(cnt, (int, long))
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], (int, long))

        self.assertArgIsOut(CGGetOnlineDisplayList, 1)
        self.assertArgIsOut(CGGetOnlineDisplayList, 2)
        v, ids, cnt = CGGetOnlineDisplayList(10, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(cnt, (int, long))
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], (int, long))

        v = CGDisplayIDToOpenGLDisplayMask(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))
        self.assertNotEqual(v, 0)

        id = CGOpenGLDisplayMaskToDisplayID(v)
        self.assertIsInstance(id, (int, long))
        self.assertEqual(id, CGMainDisplayID())

        box = CGDisplayBounds(CGMainDisplayID())
        self.assertIsInstance(box, CGRect)

        v = CGDisplayPixelsWide(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))
        v = CGDisplayPixelsHigh(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        modes = CGDisplayAvailableModes(CGMainDisplayID())
        self.assertIsInstance(modes, CFArrayRef)
        self.assertTrue(len(modes) > 0)
        self.assertIsInstance(modes[0], CFDictionaryRef)

        v, exact = CGDisplayBestModeForParameters(CGMainDisplayID(),
                32, 800, 600, None)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIsInstance(exact, (int, long))

        v, exact = CGDisplayBestModeForParametersAndRefreshRate(
                CGMainDisplayID(), 32, 800, 600, 70, None)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIsInstance(exact, (int, long))

        v, exact = CGDisplayBestModeForParametersAndRefreshRateWithProperty(
                CGMainDisplayID(), 32, 800, 600, 70,
                kCGDisplayModeIsSafeForHardware, None)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIsInstance(exact, (int, long))

        cur = CGDisplayCurrentMode(CGMainDisplayID())
        self.assertIsInstance(cur, CFDictionaryRef)

        v = CGDisplaySwitchToMode(CGMainDisplayID(), v)
        self.assertEqual(v, 0)
        v = CGDisplaySwitchToMode(CGMainDisplayID(), cur)
        self.assertEqual(v, 0)

        v = CGDisplayBitsPerPixel(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayBitsPerSample(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplaySamplesPerPixel(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayBytesPerRow(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        self.assertArgIsOut(CGGetDisplayTransferByFormula, 1)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 2)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 3)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 4)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 5)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 6)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 7)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 8)
        self.assertArgIsOut(CGGetDisplayTransferByFormula, 9)
        v = CGGetDisplayTransferByFormula(CGMainDisplayID(),
                None, None, None, None, None, None, None, None, None)
        self.assertIsInstance(v[0], (int, long))
        for i in range(9):
            self.assertIsInstance(v[i+1], float)


        v = CGSetDisplayTransferByFormula(CGMainDisplayID(), *v[1:])
        self.assertEqual(v, 0)


        tablen = CGDisplayGammaTableCapacity(CGMainDisplayID())
        self.assertIsInstance(tablen, (int, long))

        err, red, green, blue, count = CGGetDisplayTransferByTable(
                CGMainDisplayID(), tablen, None, None, None, None)
        self.assertIsInstance(err, (int, long))
        self.assertIsInstance(count, (int, long))
        self.assertEqual(err, 0)
        self.failIfEqual(count, 0)


        err = CGSetDisplayTransferByTable(CGMainDisplayID(), count,
                red, green, blue)
        self.assertEqual(err, 0)

        err, red, green, blue, count = CGGetDisplayTransferByTable(
                CGMainDisplayID(), tablen, None, None, None, None)
        self.assertIsInstance(err, (int, long))
        self.assertIsInstance(count, (int, long))
        self.assertEqual(err, 0)
        self.failIfEqual(count, 0)

        err = CGSetDisplayTransferByTable(CGMainDisplayID(), count,
                red, green, blue)
        self.assertEqual(err, 0)

        CGDisplayRestoreColorSyncSettings()

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.assertIsInstance(v, int)
        self.failIf(v)

        err = CGDisplayCapture(CGMainDisplayID())
        self.assertEqual(err, 0)

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.assertTrue(v)

        err = CGDisplayRelease(CGMainDisplayID())
        self.assertEqual(err, 0)

        v = CGDisplayIsCaptured(CGMainDisplayID())
        self.failIf(v)

        err = CGDisplayCaptureWithOptions(CGMainDisplayID(), 0)
        self.assertEqual(err, 0)

        err = CGDisplayRelease(CGMainDisplayID())
        self.assertEqual(err, 0)

        err = CGCaptureAllDisplays()
        self.assertEqual(err, 0)

        ctx = CGDisplayGetDrawingContext(CGMainDisplayID())
        self.assertIsInstance(ctx, CGContextRef)

        err = CGReleaseAllDisplays()
        self.assertEqual(err, 0)

        err = CGCaptureAllDisplaysWithOptions(0)
        self.assertEqual(err, 0)

        err = CGReleaseAllDisplays()
        self.assertEqual(err, 0)

        v = CGShieldingWindowID(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGShieldingWindowLevel()
        self.assertIsInstance(v, (int, long))

        v = CGDisplayBaseAddress(CGMainDisplayID())
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], bytes)

        v = CGDisplayAddressForPosition(CGMainDisplayID(), 100, 100)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], str)

        err = CGDisplayHideCursor(CGMainDisplayID())
        self.assertEqual(err, 0)

        err = CGDisplayShowCursor(CGMainDisplayID())
        self.assertEqual(err, 0)

        err = CGDisplayMoveCursorToPoint(CGMainDisplayID(), (100, 100))

        dX, dY = CGGetLastMouseDelta(None, None)
        self.assertIsInstance(dX, (int, long))
        self.assertIsInstance(dY, (int, long))

        v = CGDisplayCanSetPalette(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        err = CGDisplayWaitForBeamPositionOutsideLines(CGMainDisplayID(), 200, 400)
        self.assertEqual(err, 0)

        v = CGDisplayBeamPosition(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        palette = CGPaletteCreateDefaultColorPalette()
        self.assertIsInstance(palette, CGDirectPaletteRef)

        err = CGDisplaySetPalette(CGMainDisplayID(), palette)
        self.assertIsInstance(err, (int, long))

        # Don't actually call CGSetDisplayTransferByByteTable, it might have
        # permanent effects.
        self.assertResultHasType(CGSetDisplayTransferByByteTable, objc._C_INT)
        self.assertArgHasType(CGSetDisplayTransferByByteTable, 0, objc._C_UINT)
        self.assertArgHasType(CGSetDisplayTransferByByteTable, 1, objc._C_UINT)
        self.assertArgHasType(CGSetDisplayTransferByByteTable, 2, b'n^' + objc._C_CHAR_AS_INT)
        self.assertArgSizeInArg(CGSetDisplayTransferByByteTable, 2, 1)
        self.assertArgHasType(CGSetDisplayTransferByByteTable, 3, b'n^' + objc._C_CHAR_AS_INT)
        self.assertArgSizeInArg(CGSetDisplayTransferByByteTable, 3, 1)
        self.assertArgHasType(CGSetDisplayTransferByByteTable, 4, b'n^' + objc._C_CHAR_AS_INT)
        self.assertArgSizeInArg(CGSetDisplayTransferByByteTable, 4, 1)

    @min_os_level('10.6')
    def testTypes10_6(self):
        self.assertIsCFType(CGDisplayModeRef)

    @min_os_level('10.6')
    def testFunction10_6(self):
        mainID = CGMainDisplayID()

        self.assertResultIsCFRetained(CGDisplayCopyAllDisplayModes)
        v = CGDisplayCopyAllDisplayModes(mainID, None)
        self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(CGDisplayCopyDisplayMode)
        mode = CGDisplayCopyDisplayMode(mainID)
        self.assertIsInstance(mode, CGDisplayModeRef)

        v = CGDisplaySetDisplayMode(mainID, mode, None)
        self.assertIsInstance(v, (int, long))

        v = CGDisplayModeGetWidth(mode)
        self.assertIsInstance(v, (int, long))
        v = CGDisplayModeGetHeight(mode)
        self.assertIsInstance(v, (int, long))
        v = CGDisplayModeCopyPixelEncoding(mode)
        self.assertIsInstance(v, unicode)
        v = CGDisplayModeGetRefreshRate(mode)
        self.assertIsInstance(v, float)
        v = CGDisplayModeGetIOFlags(mode)
        self.assertIsInstance(v, (int, long))
        v = CGDisplayModeGetIODisplayModeID(mode)
        self.assertIsInstance(v, (int, long))
        v = CGDisplayModeIsUsableForDesktopGUI(mode)
        self.assertIsInstance(v, bool)
        v = CGDisplayModeGetTypeID()
        self.assertIsInstance(v, (int, long))
        v = CGDisplayModeRetain(mode)
        self.assertTrue(v is mode)
        CGDisplayModeRelease(mode)

        self.assertResultIsCFRetained(CGDisplayCreateImage)
        v = CGDisplayCreateImage(mainID)
        self.assertIsInstance(v, CGImageRef)
        self.assertResultIsCFRetained(CGDisplayCreateImageForRect)
        v = CGDisplayCreateImageForRect(mainID, ((0, 0), (100, 100)))
        self.assertIsInstance(v, CGImageRef)




if __name__ == "__main__":
    main()
