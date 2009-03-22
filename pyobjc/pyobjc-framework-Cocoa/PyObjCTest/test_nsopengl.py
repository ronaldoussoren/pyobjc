
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSOpenGL (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSOpenGLGOFormatCacheSize, 501)
        self.failUnlessEqual(NSOpenGLGOClearFormatCache, 502)
        self.failUnlessEqual(NSOpenGLGORetainRenderers, 503)
        self.failUnlessEqual(NSOpenGLGOResetLibrary, 504)

        self.failUnlessEqual(NSOpenGLPFAAllRenderers,   1)
        self.failUnlessEqual(NSOpenGLPFADoubleBuffer,   5)
        self.failUnlessEqual(NSOpenGLPFAStereo,   6)
        self.failUnlessEqual(NSOpenGLPFAAuxBuffers,   7)
        self.failUnlessEqual(NSOpenGLPFAColorSize,   8)
        self.failUnlessEqual(NSOpenGLPFAAlphaSize,  11)
        self.failUnlessEqual(NSOpenGLPFADepthSize,  12)
        self.failUnlessEqual(NSOpenGLPFAStencilSize,  13)
        self.failUnlessEqual(NSOpenGLPFAAccumSize,  14)
        self.failUnlessEqual(NSOpenGLPFAMinimumPolicy,  51)
        self.failUnlessEqual(NSOpenGLPFAMaximumPolicy,  52)
        self.failUnlessEqual(NSOpenGLPFAOffScreen,  53)
        self.failUnlessEqual(NSOpenGLPFAFullScreen,  54)
        self.failUnlessEqual(NSOpenGLPFASampleBuffers,  55)
        self.failUnlessEqual(NSOpenGLPFASamples,  56)
        self.failUnlessEqual(NSOpenGLPFAAuxDepthStencil,  57)
        self.failUnlessEqual(NSOpenGLPFAColorFloat,  58)
        self.failUnlessEqual(NSOpenGLPFAMultisample,  59)
        self.failUnlessEqual(NSOpenGLPFASupersample,  60)
        self.failUnlessEqual(NSOpenGLPFASampleAlpha,  61)
        self.failUnlessEqual(NSOpenGLPFARendererID,  70)
        self.failUnlessEqual(NSOpenGLPFASingleRenderer,  71)
        self.failUnlessEqual(NSOpenGLPFANoRecovery,  72)
        self.failUnlessEqual(NSOpenGLPFAAccelerated,  73)
        self.failUnlessEqual(NSOpenGLPFAClosestPolicy,  74)
        self.failUnlessEqual(NSOpenGLPFARobust,  75)
        self.failUnlessEqual(NSOpenGLPFABackingStore,  76)
        self.failUnlessEqual(NSOpenGLPFAMPSafe,  78)
        self.failUnlessEqual(NSOpenGLPFAWindow,  80)
        self.failUnlessEqual(NSOpenGLPFAMultiScreen,  81)
        self.failUnlessEqual(NSOpenGLPFACompliant,  83)
        self.failUnlessEqual(NSOpenGLPFAScreenMask,  84)
        self.failUnlessEqual(NSOpenGLPFAPixelBuffer,  90)
        self.failUnlessEqual(NSOpenGLPFAVirtualScreenCount, 128)


        self.failUnlessEqual(NSOpenGLCPSwapRectangle, 200)
        self.failUnlessEqual(NSOpenGLCPSwapRectangleEnable, 201)
        self.failUnlessEqual(NSOpenGLCPRasterizationEnable, 221)
        self.failUnlessEqual(NSOpenGLCPSwapInterval, 222)
        self.failUnlessEqual(NSOpenGLCPSurfaceOrder, 235)
        self.failUnlessEqual(NSOpenGLCPSurfaceOpacity, 236)
        self.failUnlessEqual(NSOpenGLCPStateValidation, 301)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(NSOpenGLPFAAllowOfflineRenderers, 96)


    def testFunctions(self):
        major, minor = NSOpenGLGetVersion(None, None)
        self.failUnlessIsInstance(major, (int, long))
        self.failUnlessIsInstance(minor, (int, long))

        self.failUnlessArgIsOut(NSOpenGLGetOption, 1)
        v = NSOpenGLGetOption(NSOpenGLGOFormatCacheSize, None)
        self.failUnlessIsInstance(v, (int, long))

        NSOpenGLSetOption(NSOpenGLGOFormatCacheSize, v)

    def testMethods(self):
        self.failUnlessArgIsNullTerminated(NSOpenGLPixelFormat.initWithAttributes_, 0)
        self.failUnlessArgIsIn(NSOpenGLPixelFormat.initWithAttributes_, 0)

        o = NSOpenGLPixelFormat.alloc().initWithAttributes_([NSOpenGLPFANoRecovery, NSOpenGLPFAAuxBuffers, 2])
        self.failUnlessIsInstance(o, NSOpenGLPixelFormat)

        #FIXME: I'm not entirely sure this test is correct.
        self.failUnlessArgIsOut(NSOpenGLPixelFormat.getValues_forAttribute_forVirtualScreen_, 0)
        v = o.getValues_forAttribute_forVirtualScreen_(
                None, NSOpenGLPFANoRecovery, 0)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultHasType(NSOpenGLPixelFormat.CGLPixelFormatObj, 
                '^{_CGLPixelFormatObject}')

        self.failUnlessResultHasType(NSOpenGLContext.CGLContextObj, 
                '^{_CGLContextObj}')


if __name__ == "__main__":
    main()
