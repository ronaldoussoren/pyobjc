import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level


class TestNSOpenGL(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSOpenGLGOFormatCacheSize, 501)
        self.assertEqual(AppKit.NSOpenGLGOClearFormatCache, 502)
        self.assertEqual(AppKit.NSOpenGLGORetainRenderers, 503)
        self.assertEqual(AppKit.NSOpenGLGOResetLibrary, 504)
        self.assertEqual(AppKit.NSOpenGLGOUseBuildCache, 506)

        self.assertEqual(AppKit.NSOpenGLPFAAllRenderers, 1)
        self.assertEqual(AppKit.NSOpenGLPFATripleBuffer, 3)
        self.assertEqual(AppKit.NSOpenGLPFADoubleBuffer, 5)
        self.assertEqual(AppKit.NSOpenGLPFAStereo, 6)
        self.assertEqual(AppKit.NSOpenGLPFAAuxBuffers, 7)
        self.assertEqual(AppKit.NSOpenGLPFAColorSize, 8)
        self.assertEqual(AppKit.NSOpenGLPFAAlphaSize, 11)
        self.assertEqual(AppKit.NSOpenGLPFADepthSize, 12)
        self.assertEqual(AppKit.NSOpenGLPFAStencilSize, 13)
        self.assertEqual(AppKit.NSOpenGLPFAAccumSize, 14)
        self.assertEqual(AppKit.NSOpenGLPFAMinimumPolicy, 51)
        self.assertEqual(AppKit.NSOpenGLPFAMaximumPolicy, 52)
        self.assertEqual(AppKit.NSOpenGLPFAOffScreen, 53)
        self.assertEqual(AppKit.NSOpenGLPFAFullScreen, 54)
        self.assertEqual(AppKit.NSOpenGLPFASampleBuffers, 55)
        self.assertEqual(AppKit.NSOpenGLPFASamples, 56)
        self.assertEqual(AppKit.NSOpenGLPFAAuxDepthStencil, 57)
        self.assertEqual(AppKit.NSOpenGLPFAColorFloat, 58)
        self.assertEqual(AppKit.NSOpenGLPFAMultisample, 59)
        self.assertEqual(AppKit.NSOpenGLPFASupersample, 60)
        self.assertEqual(AppKit.NSOpenGLPFASampleAlpha, 61)
        self.assertEqual(AppKit.NSOpenGLPFARendererID, 70)
        self.assertEqual(AppKit.NSOpenGLPFASingleRenderer, 71)
        self.assertEqual(AppKit.NSOpenGLPFANoRecovery, 72)
        self.assertEqual(AppKit.NSOpenGLPFAAccelerated, 73)
        self.assertEqual(AppKit.NSOpenGLPFAClosestPolicy, 74)
        self.assertEqual(AppKit.NSOpenGLPFARobust, 75)
        self.assertEqual(AppKit.NSOpenGLPFABackingStore, 76)
        self.assertEqual(AppKit.NSOpenGLPFAMPSafe, 78)
        self.assertEqual(AppKit.NSOpenGLPFAWindow, 80)
        self.assertEqual(AppKit.NSOpenGLPFAMultiScreen, 81)
        self.assertEqual(AppKit.NSOpenGLPFACompliant, 83)
        self.assertEqual(AppKit.NSOpenGLPFAScreenMask, 84)
        self.assertEqual(AppKit.NSOpenGLPFAPixelBuffer, 90)
        self.assertEqual(AppKit.NSOpenGLPFAVirtualScreenCount, 128)

        self.assertEqual(AppKit.NSOpenGLCPSwapRectangle, 200)
        self.assertEqual(AppKit.NSOpenGLCPSwapRectangleEnable, 201)
        self.assertEqual(AppKit.NSOpenGLCPRasterizationEnable, 221)
        self.assertEqual(AppKit.NSOpenGLCPSwapInterval, 222)
        self.assertEqual(AppKit.NSOpenGLCPSurfaceOrder, 235)
        self.assertEqual(AppKit.NSOpenGLCPSurfaceOpacity, 236)
        self.assertEqual(AppKit.NSOpenGLCPStateValidation, 301)
        self.assertEqual(AppKit.NSOpenGLCPSurfaceBackingSize, 304)
        self.assertEqual(AppKit.NSOpenGLCPReclaimResources, 308)
        self.assertEqual(AppKit.NSOpenGLCPCurrentRendererID, 309)
        self.assertEqual(AppKit.NSOpenGLCPGPUVertexProcessing, 310)
        self.assertEqual(AppKit.NSOpenGLCPGPUFragmentProcessing, 311)
        self.assertEqual(AppKit.NSOpenGLCPHasDrawable, 314)
        self.assertEqual(AppKit.NSOpenGLCPMPSwapsInFlight, 315)
        self.assertEqual(AppKit.NSOpenGLCPSurfaceSurfaceVolatile, 306)

        self.assertEqual(AppKit.NSOpenGLContextParameterSwapInterval, 222)
        self.assertEqual(AppKit.NSOpenGLContextParameterSurfaceOrder, 235)
        self.assertEqual(AppKit.NSOpenGLContextParameterSurfaceOpacity, 236)
        self.assertEqual(AppKit.NSOpenGLContextParameterSurfaceBackingSize, 304)
        self.assertEqual(AppKit.NSOpenGLContextParameterReclaimResources, 308)
        self.assertEqual(AppKit.NSOpenGLContextParameterCurrentRendererID, 309)
        self.assertEqual(AppKit.NSOpenGLContextParameterGPUVertexProcessing, 310)
        self.assertEqual(AppKit.NSOpenGLContextParameterGPUFragmentProcessing, 311)
        self.assertEqual(AppKit.NSOpenGLContextParameterHasDrawable, 314)
        self.assertEqual(AppKit.NSOpenGLContextParameterMPSwapsInFlight, 315)
        self.assertEqual(AppKit.NSOpenGLContextParameterSwapRectangle, 200)
        self.assertEqual(AppKit.NSOpenGLContextParameterSwapRectangleEnable, 201)
        self.assertEqual(AppKit.NSOpenGLContextParameterRasterizationEnable, 221)
        self.assertEqual(AppKit.NSOpenGLContextParameterStateValidation, 301)
        self.assertEqual(AppKit.NSOpenGLContextParameterSurfaceSurfaceVolatile, 306)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSOpenGLPFAAllowOfflineRenderers, 96)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSOpenGLPFAOpenGLProfile, 99)
        self.assertEqual(AppKit.NSOpenGLProfileVersionLegacy, 0x1000)
        self.assertEqual(AppKit.NSOpenGLProfileVersion3_2Core, 0x3200)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NSOpenGLProfileVersion4_1Core, 0x4100)

    def testFunctions(self):
        major, minor = AppKit.NSOpenGLGetVersion(None, None)
        self.assertIsInstance(major, int)
        self.assertIsInstance(minor, int)

        self.assertArgIsOut(AppKit.NSOpenGLGetOption, 1)
        v = AppKit.NSOpenGLGetOption(AppKit.NSOpenGLGOFormatCacheSize, None)
        self.assertIsInstance(v, int)

        AppKit.NSOpenGLSetOption(AppKit.NSOpenGLGOFormatCacheSize, v)

    def testMethods(self):
        self.assertArgIsNullTerminated(
            AppKit.NSOpenGLPixelFormat.initWithAttributes_, 0
        )
        self.assertArgIsIn(AppKit.NSOpenGLPixelFormat.initWithAttributes_, 0)

        o = AppKit.NSOpenGLPixelFormat.alloc().initWithAttributes_(
            [AppKit.NSOpenGLPFANoRecovery, AppKit.NSOpenGLPFAAuxBuffers, 2]
        )
        self.assertIsInstance(o, AppKit.NSOpenGLPixelFormat)

        # FIXME: I'm not entirely sure this test is correct.
        self.assertArgIsOut(
            AppKit.NSOpenGLPixelFormat.getValues_forAttribute_forVirtualScreen_, 0
        )
        v = o.getValues_forAttribute_forVirtualScreen_(
            None, AppKit.NSOpenGLPFANoRecovery, 0
        )
        self.assertIsInstance(v, int)

        self.assertResultHasType(
            AppKit.NSOpenGLPixelFormat.CGLPixelFormatObj, b"^{_CGLPixelFormatObject}"
        )

        self.assertResultHasType(
            AppKit.NSOpenGLContext.CGLContextObj, b"^{_CGLContextObj}"
        )

        self.assertArgIsIn(AppKit.NSOpenGLContext.setValues_forParameter_, 0)
        self.assertArgIsVariableSize(AppKit.NSOpenGLContext.setValues_forParameter_, 0)

        self.assertArgIsIn(AppKit.NSOpenGLContext.setValues_forParameter_, 0)
        self.assertArgIsVariableSize(AppKit.NSOpenGLContext.setValues_forParameter_, 0)

        self.assertArgIsIn(
            AppKit.NSOpenGLContext.setOffScreen_width_height_rowbytes_, 0
        )
        self.assertArgIsVariableSize(
            AppKit.NSOpenGLContext.setOffScreen_width_height_rowbytes_, 0
        )

    @min_os_level("10.6")
    @max_os_level("10.14")
    def testMethods10_6(self):
        self.assertArgHasType(
            AppKit.NSOpenGLPixelFormat.initWithCGLPixelFormatObj_,
            0,
            b"^{_CGLPixelFormatObject=}",
        )
        self.assertArgHasType(
            AppKit.NSOpenGLPixelFormat.initWithCGLBufferObj_, 0, b"^{_CGLBufferObject=}"
        )
        self.assertResultHasType(
            AppKit.NSOpenGLPixelFormat.CGLBufferObj_, b"^{_CGLBufferObject=}"
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSOpenGLPFARemotePixelBuffer, 91)
        self.assertEqual(AppKit.NSOpenGLPFAAcceleratedCompute, 97)
