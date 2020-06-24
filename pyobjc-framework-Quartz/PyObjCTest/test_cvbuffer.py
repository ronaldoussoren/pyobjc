from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz


class TestCVBuffer(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.kCVBufferPropagatedAttachmentsKey, str)
        self.assertIsInstance(Quartz.kCVBufferNonPropagatedAttachmentsKey, str)
        self.assertIsInstance(Quartz.kCVBufferMovieTimeKey, str)
        self.assertIsInstance(Quartz.kCVBufferTimeValueKey, str)
        self.assertIsInstance(Quartz.kCVBufferTimeScaleKey, str)

        self.assertEqual(Quartz.kCVAttachmentMode_ShouldNotPropagate, 0)
        self.assertEqual(Quartz.kCVAttachmentMode_ShouldPropagate, 1)

    @expectedFailure
    def testTypes(self):
        # Needs work...
        self.assertIsCFType(Quartz.CVBufferRef)

    def testFunctions(self):
        rv, buf = Quartz.CVOpenGLBufferCreate(None, 100, 100, {"a": "b"}, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(buf, Quartz.CVOpenGLBufferRef)

        rv, buf2 = Quartz.CVOpenGLBufferCreate(None, 100, 100, {"a": "b"}, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(buf2, Quartz.CVOpenGLBufferRef)

        v = Quartz.CVBufferRetain(buf)
        self.assertTrue(v is buf)
        Quartz.CVBufferRelease(v)

        ctx = object()

        self.assertArgHasType(Quartz.CVBufferSetAttachment, 2, b"@")
        self.assertArgHasType(Quartz.CVBufferSetAttachment, 0, b"^{__CVBuffer=}")
        Quartz.CVBufferSetAttachment(
            buf,
            b"pyobjc.test".decode("latin1"),
            ctx,
            Quartz.kCVAttachmentMode_ShouldPropagate,
        )

        self.assertArgHasType(Quartz.CVBufferGetAttachment, 0, b"^{__CVBuffer=}")
        self.assertResultHasType(Quartz.CVBufferGetAttachment, b"@")
        self.assertArgIsOut(Quartz.CVBufferGetAttachment, 2)
        v, mode = Quartz.CVBufferGetAttachment(
            buf, b"pyobjc.test".decode("latin1"), None
        )
        self.assertTrue(v is ctx)
        self.assertEqual(mode, Quartz.kCVAttachmentMode_ShouldPropagate)

        self.assertArgHasType(Quartz.CVBufferGetAttachments, 0, b"^{__CVBuffer=}")
        v = Quartz.CVBufferGetAttachments(buf, Quartz.kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertTrue("pyobjc.test" in v)

        self.assertArgHasType(Quartz.CVBufferSetAttachments, 0, b"^{__CVBuffer=}")
        Quartz.CVBufferSetAttachments(
            buf,
            {"pyobjc.test2": 42, "pyobjc.test3": b"hello".decode("latin1")},
            Quartz.kCVAttachmentMode_ShouldPropagate,
        )

        self.assertArgHasType(Quartz.CVBufferPropagateAttachments, 0, b"^{__CVBuffer=}")
        self.assertArgHasType(Quartz.CVBufferPropagateAttachments, 1, b"^{__CVBuffer=}")
        Quartz.CVBufferPropagateAttachments(buf, buf2)

        v = Quartz.CVBufferGetAttachments(
            buf2, Quartz.kCVAttachmentMode_ShouldPropagate
        )
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertTrue("pyobjc.test2" in v)

        self.assertArgHasType(Quartz.CVBufferRemoveAttachment, 0, b"^{__CVBuffer=}")
        Quartz.CVBufferRemoveAttachment(buf, "pyobjc.test")
        v = Quartz.CVBufferGetAttachments(buf, Quartz.kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertFalse("pyobjc.test" in v)

        self.assertArgHasType(Quartz.CVBufferRemoveAllAttachments, 0, b"^{__CVBuffer=}")
        Quartz.CVBufferRemoveAllAttachments(buf)
        v = Quartz.CVBufferGetAttachments(buf, Quartz.kCVAttachmentMode_ShouldPropagate)
        self.assertIsInstance(v, Quartz.CFDictionaryRef)
        self.assertFalse("pyobjc.test2" in v)
