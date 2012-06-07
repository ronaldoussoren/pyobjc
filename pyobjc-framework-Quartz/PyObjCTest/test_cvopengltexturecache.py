
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestCVOpenGLTextureCache (TestCase):
    def testTypes(self):
        self.assertIsCFType(CVOpenGLTextureCacheRef)

    def testConstants(self):
        self.assertIsInstance(kCVOpenGLTextureCacheChromaSamplingModeKey, unicode)
        self.assertIsInstance(kCVOpenGLTextureCacheChromaSamplingModeAutomatic, unicode)
        self.assertIsInstance(kCVOpenGLTextureCacheChromaSamplingModeHighestQuality, unicode)
        self.assertIsInstance(kCVOpenGLTextureCacheChromaSamplingModeBestPerformance, unicode)

    @expectedFailure
    def testFunctions(self):

        self.fail("Create CGLContext and CGLFormat")
        self.assertArgIsOut(CVOpenGLTextureCacheCreate, 5)
        rv, cache = CVOpenGLTextureCacheCreate(None,  None, cglCtx, cglFmt, None, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(cache, CVOpenGLTextureCacheRef)

        v = CVOpenGLTextureCacheRetain(cache)
        self.assertTrue(v is cache)
        CVOpenGLTextureCacheRelease(v)

        self.fail("Create CVImageBufferRef")
        rv, texture = CVOpenGLTextureCacheCreateTextureFromImage(None, cache, img, None, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(cache, CVOpenGLTextureRef)

        CVOpenGLTextureCacheFlush(cache, 0)

if __name__ == "__main__":
    main()
