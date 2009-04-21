
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVPixelBufferPool (TestCase):
    def testIncomplete(self):
        self.fail("Add header tests for <CoreVideo/CVPixelBufferPool.h>")

    def testTypes(self):
        self.failUnlessIsCFType(CVPixelBufferPoolRef)

    def testContants(self):
        self.failUnlessIsInstance(kCVPixelBufferPoolMinimumBufferCountKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferPoolMaximumBufferAgeKey, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CVPixelBufferPoolGetTypeID(), (int, long))

        self.failUnlessArgIsCFRetained(CVPixelBufferPoolCreate, 3)
        self.failUnlessArgIsOut(CVPixelBufferPoolCreate, 3)
        rv, pool = CVPixelBufferPoolCreate(None, {
            kCVPixelBufferPoolMinimumBufferCountKey: 1,
            kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            }, {
                kCVPixelBufferWidthKey: 100,
                kCVPixelBufferHeightKey: 100,
                kCVPixelBufferPixelFormatTypeKey: kCVPixelFormatType_32ARGB,
            }, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(pool, CVPixelBufferPoolRef)


        v = CVPixelBufferPoolRetain(pool)
        self.failUnless(v is pool)
        CVPixelBufferPoolRelease(pool)

        v = CVPixelBufferPoolGetAttributes(pool)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = CVPixelBufferPoolGetPixelBufferAttributes(pool)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessArgIsOut(CVPixelBufferPoolCreatePixelBuffer, 2)
        rv, image = CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(image, CVPixelBufferRef)



if __name__ == "__main__":
    main()
