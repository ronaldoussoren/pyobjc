from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCVMetalTextureCache(TestCase):
    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCVMetalTextureCacheMaximumTextureAgeKey, str)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertIsInstance(Quartz.CVMetalTextureCacheGetTypeID(), int)

        self.assertArgIsOut(Quartz.CVMetalTextureCacheCreate, 4)
        self.assertArgIsCFRetained(Quartz.CVMetalTextureCacheCreate, 4)
        self.assertArgIsOut(Quartz.CVMetalTextureCacheCreateTextureFromImage, 8)
        self.assertArgIsCFRetained(Quartz.CVMetalTextureCacheCreateTextureFromImage, 8)
        Quartz.CVMetalTextureCacheFlush
