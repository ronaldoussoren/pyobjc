
from PyObjCTools.TestSupport import *
from Quartz import *

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
        self.assertIsInstance(CVOpenGLTextureCacheGetTypeID, (int, long))
        CVOpenGLTextureCacheRetain
        CVOpenGLTextureCacheRelease

        self.assertArgIsOut(CVOpenGLTextureCacheCreate, 5)
        self.assertArgIsCFRetained(CVOpenGLTextureCacheCreate, 5)

        self.assertArgIsOut(CVOpenGLTextureCacheCreateTextureFromImage, 4)
        self.assertArgIsCFRetained(CVOpenGLTextureCacheCreateTextureFromImage, 4)

        CVOpenGLTextureCacheFlush

if __name__ == "__main__":
    main()
