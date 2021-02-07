from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCVOpenGLBufferPool(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CVOpenGLBufferPoolRef)

    def testConstants(self):
        self.assertIsInstance(Quartz.kCVOpenGLBufferPoolMinimumBufferCountKey, str)
        self.assertIsInstance(Quartz.kCVOpenGLBufferPoolMaximumBufferAgeKey, str)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CVOpenGLBufferPoolGetTypeID(), int)

        # FIXME: find some good creation parameters
        self.assertArgIsOut(Quartz.CVOpenGLBufferPoolCreate, 3)
        self.assertArgIsCFRetained(Quartz.CVOpenGLBufferPoolCreate, 3)
        rv, pool = Quartz.CVOpenGLBufferPoolCreate(
            None,
            {
                Quartz.kCVOpenGLBufferPoolMinimumBufferCountKey: 1,
                Quartz.kCVOpenGLBufferPoolMaximumBufferAgeKey: 42.0,
            },
            {},
            None,
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, Quartz.CVOpenGLBufferPoolRef)

        v = Quartz.CVOpenGLBufferPoolRetain(pool)
        self.assertTrue(v is pool)
        Quartz.CVOpenGLBufferPoolRelease(v)

        v = Quartz.CVOpenGLBufferPoolGetAttributes(pool)
        self.assertIsInstance(v, (dict, Quartz.CFDictionaryRef))

        v = Quartz.CVOpenGLBufferPoolGetOpenGLBufferAttributes(pool)
        self.assertIsInstance(v, (dict, Quartz.CFDictionaryRef))

        self.assertArgIsOut(Quartz.CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        self.assertArgIsCFRetained(Quartz.CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        rv, buf = Quartz.CVOpenGLBufferPoolCreateOpenGLBuffer(None, pool, None)
        self.assertIsInstance(rv, int)
        if rv == 0:
            self.assertIsInstance(buf, Quartz.CVOpenGLBufferRef)
        else:
            self.assertTrue(buf is None)
