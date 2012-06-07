
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestCVBuffer (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCVBufferPropagatedAttachmentsKey, unicode)
        self.assertIsInstance(kCVBufferNonPropagatedAttachmentsKey, unicode)
        self.assertIsInstance(kCVBufferMovieTimeKey, unicode)
        self.assertIsInstance(kCVBufferTimeValueKey, unicode)
        self.assertIsInstance(kCVBufferTimeScaleKey, unicode)

        self.assertEqual(kCVAttachmentMode_ShouldNotPropagate, 0)
        self.assertEqual(kCVAttachmentMode_ShouldPropagate, 1)

    def testFunctions(self):
        rv, buf = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(buf, CVOpenGLBufferRef)

        rv, buf2 = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(buf2, CVOpenGLBufferRef)

        v = CVBufferRetain(buf)
        self.assertTrue(v is buf)
        CVBufferRelease(v)

        ctx = object()

        self.assertArgHasType(CVBufferSetAttachment, 2, b'@')
        self.assertArgHasType(CVBufferSetAttachment, 0,  b'^{__CVBuffer=}')
        CVBufferSetAttachment(buf, b"pyobjc.test".decode('latin1'),  ctx, kCVAttachmentMode_ShouldPropagate)

        self.assertArgHasType(CVBufferGetAttachment, 0,  b'^{__CVBuffer=}')
        self.assertResultHasType(CVBufferGetAttachment, b'@')
        self.assertArgIsOut(CVBufferGetAttachment, 2)
        v, mode = CVBufferGetAttachment(buf, b"pyobjc.test".decode('latin1'), None)
        self.assertTrue(v is ctx)
        self.assertEqual(mode, kCVAttachmentMode_ShouldPropagate)

        self.assertArgHasType(CVBufferGetAttachments, 0,  b'^{__CVBuffer=}')
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertTrue("pyobjc.test" in v)

        self.assertArgHasType(CVBufferSetAttachments, 0,  b'^{__CVBuffer=}')
        CVBufferSetAttachments(buf, {
            "pyobjc.test2": 42,
            "pyobjc.test3": b"hello".decode('latin1')
        }, kCVAttachmentMode_ShouldPropagate)

        self.assertArgHasType(CVBufferPropagateAttachments, 0,  b'^{__CVBuffer=}')
        self.assertArgHasType(CVBufferPropagateAttachments, 1,  b'^{__CVBuffer=}')
        CVBufferPropagateAttachments(buf, buf2)

        v = CVBufferGetAttachments(buf2, kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertTrue("pyobjc.test2" in v)

        self.assertArgHasType(CVBufferRemoveAttachment, 0,  b'^{__CVBuffer=}')
        CVBufferRemoveAttachment(buf, "pyobjc.test")
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertFalse("pyobjc.test" in v)

        self.assertArgHasType(CVBufferRemoveAllAttachments, 0,  b'^{__CVBuffer=}')
        CVBufferRemoveAllAttachments(buf)
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertFalse("pyobjc.test2" in v)


if __name__ == "__main__":
    main()
