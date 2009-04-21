
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVOpenGLTextureCache (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CVOpenGLTextureCacheRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCVOpenGLTextureCacheChromaSamplingModeKey, unicode)
        self.failUnlessIsInstance(kCVOpenGLTextureCacheChromaSamplingModeAutomatic, unicode)
        self.failUnlessIsInstance(kCVOpenGLTextureCacheChromaSamplingModeHighestQuality, unicode)
        self.failUnlessIsInstance(kCVOpenGLTextureCacheChromaSamplingModeBestPerformance, unicode)

    def testFunctions(self):

        self.fail("Create CGLContext and CGLFormat")
        self.failUnlessArgIsOut(CVOpenGLTextureCacheCreate, 5)
        rv, cache = CVOpenGLTextureCacheCreate(None,  None, cglCtx, cglFmt, None, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(cache, CVOpenGLTextureCacheRef)

        v = CVOpenGLTextureCacheRetain(cache)
        self.failUnless(v is cache)
        CVOpenGLTextureCacheRelease(v)

        self.fail("Create CVImageBufferRef")
        rv, texture = CVOpenGLTextureCacheCreateTextureFromImage(None, cache, img, None, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(cache, CVOpenGLTextureRef)

        CVOpenGLTextureCacheFlush(cache, 0)

if __name__ == "__main__":
    main()
