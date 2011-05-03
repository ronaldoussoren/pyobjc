
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVPixelBufferPool (TestCase):

    def testTypes(self):
        self.assertIsCFType(CVPixelBufferPoolRef)

    def testContants(self):
        self.assertIsInstance(kCVPixelBufferPoolMinimumBufferCountKey, unicode)
        self.assertIsInstance(kCVPixelBufferPoolMaximumBufferAgeKey, unicode)

    def testFunctions(self):
        self.assertIsInstance(CVPixelBufferPoolGetTypeID(), (int, long))

        self.assertArgIsCFRetained(CVPixelBufferPoolCreate, 3)
        self.assertArgIsOut(CVPixelBufferPoolCreate, 3)
        rv, pool = CVPixelBufferPoolCreate(None, {
            kCVPixelBufferPoolMinimumBufferCountKey: 1,
            kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            }, {
                kCVPixelBufferWidthKey: 100,
                kCVPixelBufferHeightKey: 100,
                kCVPixelBufferPixelFormatTypeKey: kCVPixelFormatType_32ARGB,
            }, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, CVPixelBufferPoolRef)


        v = CVPixelBufferPoolRetain(pool)
        self.assertTrue(v is pool)
        CVPixelBufferPoolRelease(pool)

        v = CVPixelBufferPoolGetAttributes(pool)
        self.assertIsInstance(v, CFDictionaryRef)

        v = CVPixelBufferPoolGetPixelBufferAttributes(pool)
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertArgIsOut(CVPixelBufferPoolCreatePixelBuffer, 2)
        rv, image = CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(image, CVPixelBufferRef)



if __name__ == "__main__":
    main()
