from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz


class TestCVOpenGLTextureCache(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CVOpenGLTextureCacheRef)

    def testConstants(self):
        self.assertIsInstance(Quartz.kCVOpenGLTextureCacheChromaSamplingModeKey, str)
        self.assertIsInstance(
            Quartz.kCVOpenGLTextureCacheChromaSamplingModeAutomatic, str
        )
        self.assertIsInstance(
            Quartz.kCVOpenGLTextureCacheChromaSamplingModeHighestQuality, str
        )
        self.assertIsInstance(
            Quartz.kCVOpenGLTextureCacheChromaSamplingModeBestPerformance, str
        )

    @expectedFailure
    def testFunctions(self):
        self.assertIsInstance(Quartz.CVOpenGLTextureCacheGetTypeID, int)
        Quartz.CVOpenGLTextureCacheRetain
        Quartz.CVOpenGLTextureCacheRelease

        self.assertArgIsOut(Quartz.CVOpenGLTextureCacheCreate, 5)
        self.assertArgIsCFRetained(Quartz.CVOpenGLTextureCacheCreate, 5)

        self.assertArgIsOut(Quartz.CVOpenGLTextureCacheCreateTextureFromImage, 4)
        self.assertArgIsCFRetained(Quartz.CVOpenGLTextureCacheCreateTextureFromImage, 4)

        Quartz.CVOpenGLTextureCacheFlush
