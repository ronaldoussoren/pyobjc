from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCVMetalTexture(TestCase):
    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertIsInstance(Quartz.CVMetalTextureGetTypeID(), int)

        Quartz.CVMetalTextureGetTexture
        self.assertResultIsBOOL(Quartz.CVMetalTextureIsFlipped)

        self.assertArgIsOut(Quartz.CVMetalTextureGetCleanTexCoords, 1)
        self.assertArgIsOut(Quartz.CVMetalTextureGetCleanTexCoords, 2)
        self.assertArgIsOut(Quartz.CVMetalTextureGetCleanTexCoords, 3)
        self.assertArgIsOut(Quartz.CVMetalTextureGetCleanTexCoords, 4)

        self.assertArgIsFixedSize(Quartz.CVMetalTextureGetCleanTexCoords, 1, 2)
        self.assertArgIsFixedSize(Quartz.CVMetalTextureGetCleanTexCoords, 2, 2)
        self.assertArgIsFixedSize(Quartz.CVMetalTextureGetCleanTexCoords, 3, 2)
        self.assertArgIsFixedSize(Quartz.CVMetalTextureGetCleanTexCoords, 4, 2)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Quartz.kCVMetalTextureStorageMode, str)
