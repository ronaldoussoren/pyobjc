
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    long
except NameError:
    long = int


class TestNSOpenGL (TestCase):
    def testConstants(self):
        self.assertEqual(NSOpenGLGOFormatCacheSize, 501)
        self.assertEqual(NSOpenGLGOClearFormatCache, 502)
        self.assertEqual(NSOpenGLGORetainRenderers, 503)
        self.assertEqual(NSOpenGLGOResetLibrary, 504)

        self.assertEqual(NSOpenGLPFAAllRenderers,   1)
        self.assertEqual(NSOpenGLPFADoubleBuffer,   5)
        self.assertEqual(NSOpenGLPFAStereo,   6)
        self.assertEqual(NSOpenGLPFAAuxBuffers,   7)
        self.assertEqual(NSOpenGLPFAColorSize,   8)
        self.assertEqual(NSOpenGLPFAAlphaSize,  11)
        self.assertEqual(NSOpenGLPFADepthSize,  12)
        self.assertEqual(NSOpenGLPFAStencilSize,  13)
        self.assertEqual(NSOpenGLPFAAccumSize,  14)
        self.assertEqual(NSOpenGLPFAMinimumPolicy,  51)
        self.assertEqual(NSOpenGLPFAMaximumPolicy,  52)
        self.assertEqual(NSOpenGLPFAOffScreen,  53)
        self.assertEqual(NSOpenGLPFAFullScreen,  54)
        self.assertEqual(NSOpenGLPFASampleBuffers,  55)
        self.assertEqual(NSOpenGLPFASamples,  56)
        self.assertEqual(NSOpenGLPFAAuxDepthStencil,  57)
        self.assertEqual(NSOpenGLPFAColorFloat,  58)
        self.assertEqual(NSOpenGLPFAMultisample,  59)
        self.assertEqual(NSOpenGLPFASupersample,  60)
        self.assertEqual(NSOpenGLPFASampleAlpha,  61)
        self.assertEqual(NSOpenGLPFARendererID,  70)
        self.assertEqual(NSOpenGLPFASingleRenderer,  71)
        self.assertEqual(NSOpenGLPFANoRecovery,  72)
        self.assertEqual(NSOpenGLPFAAccelerated,  73)
        self.assertEqual(NSOpenGLPFAClosestPolicy,  74)
        self.assertEqual(NSOpenGLPFARobust,  75)
        self.assertEqual(NSOpenGLPFABackingStore,  76)
        self.assertEqual(NSOpenGLPFAMPSafe,  78)
        self.assertEqual(NSOpenGLPFAWindow,  80)
        self.assertEqual(NSOpenGLPFAMultiScreen,  81)
        self.assertEqual(NSOpenGLPFACompliant,  83)
        self.assertEqual(NSOpenGLPFAScreenMask,  84)
        self.assertEqual(NSOpenGLPFAPixelBuffer,  90)
        self.assertEqual(NSOpenGLPFAVirtualScreenCount, 128)


        self.assertEqual(NSOpenGLCPSwapRectangle, 200)
        self.assertEqual(NSOpenGLCPSwapRectangleEnable, 201)
        self.assertEqual(NSOpenGLCPRasterizationEnable, 221)
        self.assertEqual(NSOpenGLCPSwapInterval, 222)
        self.assertEqual(NSOpenGLCPSurfaceOrder, 235)
        self.assertEqual(NSOpenGLCPSurfaceOpacity, 236)
        self.assertEqual(NSOpenGLCPStateValidation, 301)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(NSOpenGLPFAAllowOfflineRenderers, 96)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(NSOpenGLPFAOpenGLProfile, 99)
        self.assertEqual(NSOpenGLProfileVersionLegacy, 0x1000)
        self.assertEqual(NSOpenGLProfileVersion3_2Core, 0x3200)


    def testFunctions(self):
        major, minor = NSOpenGLGetVersion(None, None)
        self.assertIsInstance(major, (int, long))
        self.assertIsInstance(minor, (int, long))

        self.assertArgIsOut(NSOpenGLGetOption, 1)
        v = NSOpenGLGetOption(NSOpenGLGOFormatCacheSize, None)
        self.assertIsInstance(v, (int, long))

        NSOpenGLSetOption(NSOpenGLGOFormatCacheSize, v)

    def testMethods(self):
        self.assertArgIsNullTerminated(NSOpenGLPixelFormat.initWithAttributes_, 0)
        self.assertArgIsIn(NSOpenGLPixelFormat.initWithAttributes_, 0)

        o = NSOpenGLPixelFormat.alloc().initWithAttributes_([NSOpenGLPFANoRecovery, NSOpenGLPFAAuxBuffers, 2])
        self.assertIsInstance(o, NSOpenGLPixelFormat)

        #FIXME: I'm not entirely sure this test is correct.
        self.assertArgIsOut(NSOpenGLPixelFormat.getValues_forAttribute_forVirtualScreen_, 0)
        v = o.getValues_forAttribute_forVirtualScreen_(
                None, NSOpenGLPFANoRecovery, 0)
        self.assertIsInstance(v, (int, long))

        self.assertResultHasType(NSOpenGLPixelFormat.CGLPixelFormatObj,
                b'^{_CGLPixelFormatObject}')

        self.assertResultHasType(NSOpenGLContext.CGLContextObj,
                b'^{_CGLContextObj}')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSOpenGLPixelFormat.initWithCGLPixelFormatObj_, 0, b'^{_CGLPixelFormatObject}')
        self.assertArgHasType(NSOpenGLPixelFormat.initWithCGLBufferObj, 0, b'^{_CGLBufferObject}')
        self.assertResultHasType(NSOpenGLPixelFormat.CGLBufferObj, b'^{_CGLBufferObject}')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertEqual(NSOpenGLPFARemotePixelBuffer, 91)
        self.assertEqual(NSOpenGLPFAAcceleratedCompute, 97)


if __name__ == "__main__":
    main()
