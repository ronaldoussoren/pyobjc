from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz


class TestCVOpenGLTexture(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CVOpenGLTextureRef)

    @expectedFailure
    def test_functions(self):
        self.assertIsInstance(Quartz.CVOpenGLTextureGetTypeID(), int)

        Quartz.CVOpenGLTextureRetain
        Quartz.CVOpenGLTextureRelease
        Quartz.CVOpenGLTextureGetTarget
        Quartz.CVOpenGLTextureGetName
        self.assertResultIsBOOL(Quartz.CVOpenGLTextureIsFlipped)

        self.assertArgIsOut(Quartz.CVOpenGLTextureGetCleanTexCoords, 1)
        self.assertArgIsOut(Quartz.CVOpenGLTextureGetCleanTexCoords, 2)
        self.assertArgIsOut(Quartz.CVOpenGLTextureGetCleanTexCoords, 3)
        self.assertArgIsOut(Quartz.CVOpenGLTextureGetCleanTexCoords, 4)

        self.assertArgIsFixedSize(Quartz.CVOpenGLTextureGetCleanTexCoords, 1, 2)
        self.assertArgIsFixedSize(Quartz.CVOpenGLTextureGetCleanTexCoords, 2, 2)
        self.assertArgIsFixedSize(Quartz.CVOpenGLTextureGetCleanTexCoords, 3, 2)
        self.assertArgIsFixedSize(Quartz.CVOpenGLTextureGetCleanTexCoords, 4, 2)
