
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVOpenGLTexture (TestCase):
    def testTypes(self):
        self.assertIsCFType(CVOpenGLTextureRef)

    @expectedFailure
    def testFunctions(self):
        self.assertIsInstance(CVOpenGLTextureGetTypeID(), (int, long))

        CVOpenGLTextureRetain
        CVOpenGLTextureRelease
        CVOpenGLTextureGetTarget
        CVOpenGLTextureGetName
        self.assertResultIsBOOL(CVOpenGLTextureIsFlipped)

        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 1)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 2)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 3)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 4)

        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 1, 2)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 2, 2)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 3, 2)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 4, 2)

if __name__ == "__main__":
    main()
