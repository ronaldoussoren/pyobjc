
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVOpenGLBuffer (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCVOpenGLBufferWidth, unicode)
        self.assertIsInstance(kCVOpenGLBufferHeight, unicode)
        self.assertIsInstance(kCVOpenGLBufferTarget, unicode)
        self.assertIsInstance(kCVOpenGLBufferInternalFormat, unicode)
        self.assertIsInstance(kCVOpenGLBufferMaximumMipmapLevel, unicode)

    def testTypes(self):
        self.assertIsCFType(CVOpenGLBufferRef)

    def testFunctions(self):
        self.assertIsInstance(CVOpenGLBufferGetTypeID(), (int, long))

        self.assertArgIsOut(CVOpenGLBufferCreate, 4)
        self.assertArgIsCFRetained(CVOpenGLBufferCreate, 4)
        rv, buf = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(buf, CVOpenGLBufferRef)

        v = CVOpenGLBufferRetain(buf)
        self.assertTrue(v is buf)

        CVOpenGLBufferRelease(v)

        v = CVOpenGLBufferGetAttributes(buf)
        self.assertIsInstance(v, CFDictionaryRef)

        # FIXME: actual test
        self.assertArgHasType(CVOpenGLBufferAttach, 0, b'@')

if __name__ == "__main__":
    main()
