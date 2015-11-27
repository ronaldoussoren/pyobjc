
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVPixelBufferPool (TestCase):

    def testTypes(self):
        self.assertIsCFType(CVPixelBufferPoolRef)

    def testContants(self):
        self.assertIsInstance(kCVPixelBufferPoolMinimumBufferCountKey, unicode)
        self.assertIsInstance(kCVPixelBufferPoolMaximumBufferAgeKey, unicode)


    @min_os_level('10.7')
    def testContants10_7(self):
        self.assertIsInstance(kCVPixelBufferPoolAllocationThresholdKey, unicode)
        self.assertIsInstance(kCVPixelBufferPoolFreeBufferNotification, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(kCVPixelBufferPoolFlushExcessBuffers, 1)

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
        self.assertIsInstance(v, (dict, CFDictionaryRef))

        v = CVPixelBufferPoolGetPixelBufferAttributes(pool)
        self.assertIsInstance(v, (dict, CFDictionaryRef))

        self.assertArgIsOut(CVPixelBufferPoolCreatePixelBuffer, 2)
        rv, image = CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(image, CVPixelBufferRef)


    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertArgIsOut(CVPixelBufferPoolCreatePixelBufferWithAuxAttributes, 3)
        self.assertArgIsCFRetained(CVPixelBufferPoolCreatePixelBufferWithAuxAttributes, 3)

    @min_os_level('10.11')
    def testFunctions10_11(self):
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

        CVPixelBufferPoolFlush(pool, 0)

if __name__ == "__main__":
    main()
