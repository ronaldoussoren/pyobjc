from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCVOpenGLBuffer(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.kCVOpenGLBufferWidth, str)
        self.assertIsInstance(Quartz.kCVOpenGLBufferHeight, str)
        self.assertIsInstance(Quartz.kCVOpenGLBufferTarget, str)
        self.assertIsInstance(Quartz.kCVOpenGLBufferInternalFormat, str)
        self.assertIsInstance(Quartz.kCVOpenGLBufferMaximumMipmapLevel, str)

    def testTypes(self):
        self.assertIsCFType(Quartz.CVOpenGLBufferRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CVOpenGLBufferGetTypeID(), int)

        self.assertArgIsOut(Quartz.CVOpenGLBufferCreate, 4)
        self.assertArgIsCFRetained(Quartz.CVOpenGLBufferCreate, 4)
        rv, buf = Quartz.CVOpenGLBufferCreate(None, 100, 100, {"a": "b"}, None)
        if rv == 0:
            self.assertIsInstance(buf, Quartz.CVOpenGLBufferRef)

            v = Quartz.CVOpenGLBufferRetain(buf)
            self.assertTrue(v is buf)

            Quartz.CVOpenGLBufferRelease(v)

            v = Quartz.CVOpenGLBufferGetAttributes(buf)
            self.assertIsInstance(v, (dict, Quartz.CFDictionaryRef))

            # FIXME: actual test
            self.assertArgHasType(Quartz.CVOpenGLBufferAttach, 0, b"^{__CVBuffer=}")
