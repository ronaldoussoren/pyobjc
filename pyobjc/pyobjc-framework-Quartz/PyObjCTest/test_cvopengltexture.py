
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVOpenGLTexture (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CVOpenGLTextureRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CVOpenGLTextureGetTypeID(), (int, long))

        self.fail("Create texture here")


        v = CVOpenGLTextureRetain(texture)
        self.failUnless(v is texture)
        CVOpenGLTextureRelease(v)

        v = CVOpenGLTextureGetTarget(texture)
        self.failUnlessIsInstance(v, (int, long))

        v = CVOpenGLTextureGetName(texture)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsBOOL(CVOpenGLTextureIsFlipped)
        v = CVOpenGLTextureIsFlipped(texture)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessArgIsOut(CVOpenGLTextureGetCleanTexCoords, 1)
        self.failUnlessArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 1, 2)
        self.failUnlessArgIsOut(CVOpenGLTextureGetCleanTexCoords, 2)
        self.failUnlessArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 2, 2)
        self.failUnlessArgIsOut(CVOpenGLTextureGetCleanTexCoords, 3)
        self.failUnlessArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 3, 2)
        self.failUnlessArgIsOut(CVOpenGLTextureGetCleanTexCoords, 4)
        self.failUnlessArgIsFixedSize(CVOpenGLTextureGetCleanTexCoords, 4, 2)
        ll, lr, ur, ul = CVOpenGLTextureGetCleanTexCoords(texture, None, None, None, None)
        self.failUnlessIsInstance(ll, tuple)
        self.failUnlessIsEqual(len(ll), 2)
        self.failUnlessIsInstance(ll[0], float)
        self.failUnlessIsInstance(ll[1], float)
        self.failUnlessIsInstance(lr, tuple)
        self.failUnlessIsEqual(len(lr), 2)
        self.failUnlessIsInstance(lr[0], float)
        self.failUnlessIsInstance(lr[1], float)
        self.failUnlessIsInstance(ur, tuple)
        self.failUnlessIsEqual(len(ur), 2)
        self.failUnlessIsInstance(ur[0], float)
        self.failUnlessIsInstance(ur[1], float)
        self.failUnlessIsInstance(ul, tuple)
        self.failUnlessIsEqual(len(ul), 2)
        self.failUnlessIsInstance(ul[0], float)
        self.failUnlessIsInstance(ul[1], float)

if __name__ == "__main__":
    main()
