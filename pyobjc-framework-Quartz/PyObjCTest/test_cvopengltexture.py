
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    long
except NameError:
    long = int

class TestCVOpenGLTexture (TestCase):
    def testTypes(self):
        self.assertIsCFType(CVOpenGLTextureRef)

    @expectedFailure
    def testFunctions(self):
        self.assertIsInstance(CVOpenGLTextureGetTypeID(), (int, long))

        self.fail("Create texture here")


        v = CVOpenGLTextureRetain(texture)
        self.assertTrue(v is texture)
        CVOpenGLTextureRelease(v)

        v = CVOpenGLTextureGetTarget(texture)
        self.assertIsInstance(v, (int, long))

        v = CVOpenGLTextureGetName(texture)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsBOOL(CVOpenGLTextureIsFlipped)
        v = CVOpenGLTextureIsFlipped(texture)
        self.assertIsInstance(v, bool)

        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 1)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 1, 2)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 2)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 2, 2)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 3)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 3, 2)
        self.assertArgIsOut(CVOpenGLTextureGetCleanTexCoords, 4)
        self.assertArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 4, 2)
        ll, lr, ur, ul = CVOpenGLTextureGetCleanTexCoords(texture, None, None, None, None)
        self.assertIsInstance(ll, tuple)
        self.assertIsEqual(len(ll), 2)
        self.assertIsInstance(ll[0], float)
        self.assertIsInstance(ll[1], float)
        self.assertIsInstance(lr, tuple)
        self.assertIsEqual(len(lr), 2)
        self.assertIsInstance(lr[0], float)
        self.assertIsInstance(lr[1], float)
        self.assertIsInstance(ur, tuple)
        self.assertIsEqual(len(ur), 2)
        self.assertIsInstance(ur[0], float)
        self.assertIsInstance(ur[1], float)
        self.assertIsInstance(ul, tuple)
        self.assertIsEqual(len(ul), 2)
        self.assertIsInstance(ul[0], float)
        self.assertIsInstance(ul[1], float)

if __name__ == "__main__":
    main()
