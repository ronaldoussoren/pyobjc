
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVOpenGLBuffer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCVOpenGLBufferWidth, unicode)
        self.failUnlessIsInstance(kCVOpenGLBufferHeight, unicode)
        self.failUnlessIsInstance(kCVOpenGLBufferTarget, unicode)
        self.failUnlessIsInstance(kCVOpenGLBufferInternalFormat, unicode)
        self.failUnlessIsInstance(kCVOpenGLBufferMaximumMipmapLevel, unicode)

    def testTypes(self):
        self.failUnlessIsCFType(CVOpenGLBufferRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CVOpenGLBufferGetTypeID(), (int, long))

        self.failUnlessArgIsOut(CVOpenGLBufferCreate, 4)
        self.failUnlessArgIsCFRetained(CVOpenGLBufferCreate, 4)
        rv, buf = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(buf, CVOpenGLBufferRef)

        v = CVOpenGLBufferRetain(buf)
        self.failUnless(v is buf)

        CVOpenGLBufferRelease(v)

        v = CVOpenGLBufferGetAttributes(buf)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        # FIXME: actual test
        self.failUnlessArgHasType(CVOpenGLBufferAttach, 0, '@')

if __name__ == "__main__":
    main()
