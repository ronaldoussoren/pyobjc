from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGDirectDisplay(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.kCGDisplayShowDuplicateLowResolutionModes, str)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        mainID = Quartz.CGMainDisplayID()
        mode = Quartz.CGDisplayCopyDisplayMode(mainID)
        self.assertIsInstance(mode, Quartz.CGDisplayModeRef)

        w = Quartz.CGDisplayModeGetPixelWidth(mode)
        self.assertIsInstance(w, int)

        h = Quartz.CGDisplayModeGetPixelHeight(mode)
        self.assertIsInstance(h, int)

    def testConstants(self):
        self.assertEqual(Quartz.kCGNullDirectDisplay, 0)

        self.assertEqual(Quartz.kCGDisplayWidth, "Width")
        self.assertEqual(Quartz.kCGDisplayHeight, "Height")
        self.assertEqual(Quartz.kCGDisplayMode, "Mode")
        self.assertEqual(Quartz.kCGDisplayBitsPerPixel, "BitsPerPixel")
        self.assertEqual(Quartz.kCGDisplayBitsPerSample, "BitsPerSample")
        self.assertEqual(Quartz.kCGDisplaySamplesPerPixel, "SamplesPerPixel")
        self.assertEqual(Quartz.kCGDisplayRefreshRate, "RefreshRate")
        self.assertEqual(
            Quartz.kCGDisplayModeUsableForDesktopGUI, "UsableForDesktopGUI"
        )
        self.assertEqual(Quartz.kCGDisplayIOFlags, "IOFlags")
        self.assertEqual(Quartz.kCGDisplayBytesPerRow, "kCGDisplayBytesPerRow")
        self.assertEqual(Quartz.kCGIODisplayModeID, "IODisplayModeID")

        self.assertEqual(
            Quartz.kCGDisplayModeIsSafeForHardware, "kCGDisplayModeIsSafeForHardware"
        )
        self.assertEqual(
            Quartz.kCGDisplayModeIsInterlaced, "kCGDisplayModeIsInterlaced"
        )
        self.assertEqual(Quartz.kCGDisplayModeIsStretched, "kCGDisplayModeIsStretched")
        self.assertEqual(
            Quartz.kCGDisplayModeIsTelevisionOutput, "kCGDisplayModeIsTelevisionOutput"
        )

        self.assertEqual(Quartz.kCGCaptureNoOptions, 0)
        self.assertEqual(Quartz.kCGCaptureNoFill, 1)

        self.assertNotHasAttr(Quartz, "kCGDirectMainDisplay")

        self.assertEqual(Quartz.CGDisplayNoErr, Quartz.kCGErrorSuccess)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGMainDisplayID(), int)

        self.assertArgIsOut(Quartz.CGGetDisplaysWithPoint, 2)
        self.assertArgIsOut(Quartz.CGGetDisplaysWithPoint, 3)
        v, ids, cnt = Quartz.CGGetDisplaysWithPoint((0, 0), 10, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(cnt, int)
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], int)

        self.assertArgIsOut(Quartz.CGGetDisplaysWithRect, 2)
        self.assertArgIsOut(Quartz.CGGetDisplaysWithRect, 3)
        v, ids, cnt = Quartz.CGGetDisplaysWithRect(((0, 0), (400, 500)), 10, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(cnt, int)
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], int)

        self.assertArgIsOut(Quartz.CGGetDisplaysWithOpenGLDisplayMask, 2)
        self.assertArgIsOut(Quartz.CGGetDisplaysWithOpenGLDisplayMask, 3)
        v, ids, cnt = Quartz.CGGetDisplaysWithOpenGLDisplayMask(0xFF, 10, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(cnt, int)
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], int)

        self.assertArgIsOut(Quartz.CGGetActiveDisplayList, 1)
        self.assertArgIsOut(Quartz.CGGetActiveDisplayList, 2)
        v, ids, cnt = Quartz.CGGetActiveDisplayList(10, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(cnt, int)
        # self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], int)

        self.assertArgIsOut(Quartz.CGGetOnlineDisplayList, 1)
        self.assertArgIsOut(Quartz.CGGetOnlineDisplayList, 2)
        v, ids, cnt = Quartz.CGGetOnlineDisplayList(10, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(cnt, int)
        self.assertTrue(cnt)
        self.assertEqual(len(ids), cnt)
        self.assertIsInstance(ids[0], int)

        v = Quartz.CGDisplayIDToOpenGLDisplayMask(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)
        self.assertNotEqual(v, 0)

        display_id = Quartz.CGOpenGLDisplayMaskToDisplayID(v)
        self.assertIsInstance(display_id, int)
        self.assertEqual(display_id, Quartz.CGMainDisplayID())

        box = Quartz.CGDisplayBounds(Quartz.CGMainDisplayID())
        self.assertIsInstance(box, Quartz.CGRect)

        v = Quartz.CGDisplayPixelsWide(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayPixelsHigh(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        modes = Quartz.CGDisplayAvailableModes(Quartz.CGMainDisplayID())
        self.assertIsInstance(modes, Quartz.CFArrayRef)
        self.assertTrue(len(modes) > 0)
        self.assertIsInstance(modes[0], Quartz.CFDictionaryRef)

        v, exact = Quartz.CGDisplayBestModeForParameters(
            Quartz.CGMainDisplayID(), 32, 800, 600, None
        )
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertIsInstance(exact, int)

        v, exact = Quartz.CGDisplayBestModeForParametersAndRefreshRate(
            Quartz.CGMainDisplayID(), 32, 800, 600, 70, None
        )
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertIsInstance(exact, int)

        v, exact = Quartz.CGDisplayBestModeForParametersAndRefreshRateWithProperty(
            Quartz.CGMainDisplayID(),
            32,
            800,
            600,
            70,
            Quartz.kCGDisplayModeIsSafeForHardware,
            None,
        )
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertIsInstance(exact, int)

        cur = Quartz.CGDisplayCurrentMode(Quartz.CGMainDisplayID())
        self.assertIsInstance(cur, Quartz.CFDictionaryRef)

        v = Quartz.CGDisplaySwitchToMode(Quartz.CGMainDisplayID(), v)
        self.assertEqual(v, 0)
        v = Quartz.CGDisplaySwitchToMode(Quartz.CGMainDisplayID(), cur)
        self.assertEqual(v, 0)

        v = Quartz.CGDisplayBitsPerPixel(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayBitsPerSample(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplaySamplesPerPixel(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayBytesPerRow(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 1)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 2)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 3)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 4)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 5)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 6)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 7)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 8)
        self.assertArgIsOut(Quartz.CGGetDisplayTransferByFormula, 9)
        v = Quartz.CGGetDisplayTransferByFormula(
            Quartz.CGMainDisplayID(),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        )
        self.assertIsInstance(v[0], int)
        for i in range(9):
            self.assertIsInstance(v[i + 1], float)

        v = Quartz.CGSetDisplayTransferByFormula(Quartz.CGMainDisplayID(), *v[1:])
        # self.assertEqual(v, 0)

        tablen = Quartz.CGDisplayGammaTableCapacity(Quartz.CGMainDisplayID())
        self.assertIsInstance(tablen, int)

        err, red, green, blue, count = Quartz.CGGetDisplayTransferByTable(
            Quartz.CGMainDisplayID(), tablen, None, None, None, None
        )
        self.assertIsInstance(err, int)
        self.assertIsInstance(count, int)
        self.assertEqual(err, 0)
        self.assertNotEqual(count, 0)

        err = Quartz.CGSetDisplayTransferByTable(
            Quartz.CGMainDisplayID(), count, red, green, blue
        )
        self.assertEqual(err, 0)

        err, red, green, blue, count = Quartz.CGGetDisplayTransferByTable(
            Quartz.CGMainDisplayID(), tablen, None, None, None, None
        )
        self.assertIsInstance(err, int)
        self.assertIsInstance(count, int)
        self.assertEqual(err, 0)
        self.assertNotEqual(count, 0)

        err = Quartz.CGSetDisplayTransferByTable(
            Quartz.CGMainDisplayID(), count, red, green, blue
        )
        self.assertEqual(err, 0)

        Quartz.CGDisplayRestoreColorSyncSettings()

        v = Quartz.CGDisplayIsCaptured(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)
        self.assertFalse(v)

        err = Quartz.CGDisplayCapture(Quartz.CGMainDisplayID())
        self.assertEqual(err, 0)

        v = Quartz.CGDisplayIsCaptured(Quartz.CGMainDisplayID())
        self.assertTrue(v)

        err = Quartz.CGDisplayRelease(Quartz.CGMainDisplayID())
        self.assertEqual(err, 0)

        v = Quartz.CGDisplayIsCaptured(Quartz.CGMainDisplayID())
        self.assertFalse(v)

        err = Quartz.CGDisplayCaptureWithOptions(Quartz.CGMainDisplayID(), 0)
        self.assertEqual(err, 0)

        err = Quartz.CGDisplayRelease(Quartz.CGMainDisplayID())
        self.assertEqual(err, 0)

        err = Quartz.CGCaptureAllDisplays()
        self.assertEqual(err, 0)

        ctx = Quartz.CGDisplayGetDrawingContext(Quartz.CGMainDisplayID())
        if ctx is not None:
            self.assertIsInstance(ctx, Quartz.CGContextRef)

        err = Quartz.CGReleaseAllDisplays()
        self.assertEqual(err, 0)

        err = Quartz.CGCaptureAllDisplaysWithOptions(0)
        self.assertEqual(err, 0)

        err = Quartz.CGReleaseAllDisplays()
        self.assertEqual(err, 0)

        v = Quartz.CGShieldingWindowID(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGShieldingWindowLevel()
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayBaseAddress(Quartz.CGMainDisplayID())
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], bytes)

        v = Quartz.CGDisplayAddressForPosition(Quartz.CGMainDisplayID(), 100, 100)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], bytes)

        err = Quartz.CGDisplayHideCursor(Quartz.CGMainDisplayID())
        self.assertEqual(err, 0)

        err = Quartz.CGDisplayShowCursor(Quartz.CGMainDisplayID())
        self.assertEqual(err, 0)

        err = Quartz.CGDisplayMoveCursorToPoint(Quartz.CGMainDisplayID(), (100, 100))

        dX, dY = Quartz.CGGetLastMouseDelta(None, None)
        self.assertIsInstance(dX, int)
        self.assertIsInstance(dY, int)

        v = Quartz.CGDisplayCanSetPalette(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        err = Quartz.CGDisplayWaitForBeamPositionOutsideLines(
            Quartz.CGMainDisplayID(), 200, 400
        )
        self.assertEqual(err, 0)

        v = Quartz.CGDisplayBeamPosition(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        palette = Quartz.CGPaletteCreateDefaultColorPalette()
        self.assertIsInstance(palette, Quartz.CGDirectPaletteRef)

        err = Quartz.CGDisplaySetPalette(Quartz.CGMainDisplayID(), palette)
        self.assertIsInstance(err, int)

        # Don't actually call Quartz.CGSetDisplayTransferByByteTable, it might have
        # permanent effects.
        self.assertResultHasType(Quartz.CGSetDisplayTransferByByteTable, objc._C_INT)
        self.assertArgHasType(Quartz.CGSetDisplayTransferByByteTable, 0, objc._C_UINT)
        self.assertArgHasType(Quartz.CGSetDisplayTransferByByteTable, 1, objc._C_UINT)
        self.assertArgHasType(
            Quartz.CGSetDisplayTransferByByteTable, 2, b"n^" + objc._C_CHAR_AS_INT
        )
        self.assertArgSizeInArg(Quartz.CGSetDisplayTransferByByteTable, 2, 1)
        self.assertArgHasType(
            Quartz.CGSetDisplayTransferByByteTable, 3, b"n^" + objc._C_CHAR_AS_INT
        )
        self.assertArgSizeInArg(Quartz.CGSetDisplayTransferByByteTable, 3, 1)
        self.assertArgHasType(
            Quartz.CGSetDisplayTransferByByteTable, 4, b"n^" + objc._C_CHAR_AS_INT
        )
        self.assertArgSizeInArg(Quartz.CGSetDisplayTransferByByteTable, 4, 1)

    @min_os_level("10.6")
    def testTypes10_6(self):
        self.assertIsCFType(Quartz.CGDisplayModeRef)

    @min_os_level("10.6")
    def testFunction10_6(self):
        mainID = Quartz.CGMainDisplayID()

        self.assertResultIsCFRetained(Quartz.CGDisplayCopyAllDisplayModes)
        v = Quartz.CGDisplayCopyAllDisplayModes(mainID, None)
        self.assertIsInstance(v, Quartz.CFArrayRef)

        self.assertResultIsCFRetained(Quartz.CGDisplayCopyDisplayMode)
        mode = Quartz.CGDisplayCopyDisplayMode(mainID)
        self.assertIsInstance(mode, Quartz.CGDisplayModeRef)

        v = Quartz.CGDisplaySetDisplayMode(mainID, mode, None)
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayModeGetWidth(mode)
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayModeGetHeight(mode)
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayModeCopyPixelEncoding(mode)
        self.assertIsInstance(v, str)
        v = Quartz.CGDisplayModeGetRefreshRate(mode)
        self.assertIsInstance(v, float)
        v = Quartz.CGDisplayModeGetIOFlags(mode)
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayModeGetIODisplayModeID(mode)
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayModeIsUsableForDesktopGUI(mode)
        self.assertIsInstance(v, bool)
        v = Quartz.CGDisplayModeGetTypeID()
        self.assertIsInstance(v, int)
        v = Quartz.CGDisplayModeRetain(mode)
        self.assertTrue(v is mode)
        Quartz.CGDisplayModeRelease(mode)

        self.assertResultIsCFRetained(Quartz.CGDisplayCreateImage)
        # FIXME: Crashes on an OSX 10.6  test VM
        # v = Quartz.CGDisplayCreateImage(mainID)
        # self.assertIsInstance(v, Quartz.CGImageRef)
        self.assertResultIsCFRetained(Quartz.CGDisplayCreateImageForRect)
        # v = Quartz.CGDisplayCreateImageForRect(mainID, ((0, 0), (100, 100)))
        # self.assertIsInstance(v, Quartz.CGImageRef)
