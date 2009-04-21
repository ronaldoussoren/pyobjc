
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVOpenGLBufferPool (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CVOpenGLBufferPoolRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCVOpenGLBufferPoolMinimumBufferCountKey, unicode)
        self.failUnlessIsInstance(kCVOpenGLBufferPoolMaximumBufferAgeKey, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CVOpenGLBufferPoolGetTypeID(), (int, long))

        # FIXME: find some good creation parameters
        self.failUnlessArgIsOut(CVOpenGLBufferPoolCreate, 3)
        self.failUnlessArgIsCFRetained(CVOpenGLBufferPoolCreate, 3)
        rv, pool = CVOpenGLBufferPoolCreate(None, {
            kCVOpenGLBufferPoolMinimumBufferCountKey: 1,
            kCVOpenGLBufferPoolMaximumBufferAgeKey: 42.0,
            }, {}, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(pool, CVOpenGLBufferPoolRef)

        v = CVOpenGLBufferPoolRetain(pool)
        self.failUnless(v is pool)
        CVOpenGLBufferPoolRelease(v)

        v = CVOpenGLBufferPoolGetAttributes(pool)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = CVOpenGLBufferPoolGetOpenGLBufferAttributes(pool)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessArgIsOut(CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        self.failUnlessArgIsCFRetained(CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        rv, buf = CVOpenGLBufferPoolCreateOpenGLBuffer(None, pool, None)
        self.failUnlessIsInstance(rv, (int, long))
        if rv == 0:
            self.failUnlessIsInstance(buf, CVOpenGLBufferRef)
        else:
            self.failUnless(buf is None)

if __name__ == "__main__":
    main()
