from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCVPixelBufferPool(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CVPixelBufferPoolRef)

    def testContants(self):
        self.assertIsInstance(Quartz.kCVPixelBufferPoolMinimumBufferCountKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferPoolMaximumBufferAgeKey, str)

    @min_os_level("10.7")
    def testContants10_7(self):
        self.assertIsInstance(Quartz.kCVPixelBufferPoolAllocationThresholdKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferPoolFreeBufferNotification, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(Quartz.kCVPixelBufferPoolFlushExcessBuffers, 1)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CVPixelBufferPoolGetTypeID(), int)

        self.assertArgIsCFRetained(Quartz.CVPixelBufferPoolCreate, 3)
        self.assertArgIsOut(Quartz.CVPixelBufferPoolCreate, 3)
        rv, pool = Quartz.CVPixelBufferPoolCreate(
            None,
            {
                Quartz.kCVPixelBufferPoolMinimumBufferCountKey: 1,
                Quartz.kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            },
            {
                Quartz.kCVPixelBufferWidthKey: 100,
                Quartz.kCVPixelBufferHeightKey: 100,
                Quartz.kCVPixelBufferPixelFormatTypeKey: Quartz.kCVPixelFormatType_32ARGB,
            },
            None,
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, Quartz.CVPixelBufferPoolRef)

        v = Quartz.CVPixelBufferPoolRetain(pool)
        self.assertTrue(v is pool)
        Quartz.CVPixelBufferPoolRelease(pool)

        v = Quartz.CVPixelBufferPoolGetAttributes(pool)
        self.assertIsInstance(v, (dict, Quartz.CFDictionaryRef))

        v = Quartz.CVPixelBufferPoolGetPixelBufferAttributes(pool)
        self.assertIsInstance(v, (dict, Quartz.CFDictionaryRef))

        self.assertArgIsOut(Quartz.CVPixelBufferPoolCreatePixelBuffer, 2)
        rv, image = Quartz.CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(image, Quartz.CVPixelBufferRef)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertArgIsOut(
            Quartz.CVPixelBufferPoolCreatePixelBufferWithAuxAttributes, 3
        )
        self.assertArgIsCFRetained(
            Quartz.CVPixelBufferPoolCreatePixelBufferWithAuxAttributes, 3
        )

    @min_os_level("10.11")
    def testFunctions10_11(self):
        rv, pool = Quartz.CVPixelBufferPoolCreate(
            None,
            {
                Quartz.kCVPixelBufferPoolMinimumBufferCountKey: 1,
                Quartz.kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            },
            {
                Quartz.kCVPixelBufferWidthKey: 100,
                Quartz.kCVPixelBufferHeightKey: 100,
                Quartz.kCVPixelBufferPixelFormatTypeKey: Quartz.kCVPixelFormatType_32ARGB,
            },
            None,
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, Quartz.CVPixelBufferPoolRef)

        Quartz.CVPixelBufferPoolFlush(pool, 0)
