
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVBuffer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCVBufferPropagatedAttachmentsKey, unicode)
        self.failUnlessIsInstance(kCVBufferNonPropagatedAttachmentsKey, unicode)
        self.failUnlessIsInstance(kCVBufferMovieTimeKey, unicode)
        self.failUnlessIsInstance(kCVBufferTimeValueKey, unicode)
        self.failUnlessIsInstance(kCVBufferTimeScaleKey, unicode)

        self.failUnlessEqual(kCVAttachmentMode_ShouldNotPropagate, 0)
        self.failUnlessEqual(kCVAttachmentMode_ShouldPropagate, 1)

    def testTypes(self):
        try:
            CVBufferRef

            self.fail("CVBufferRef exists as a type")
        except NameError:
            pass

    def testFunctions(self):
        rv, buf = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(buf, CVOpenGLBufferRef)

        rv, buf2 = CVOpenGLBufferCreate(None, 100, 100, {"a":"b"}, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(buf2, CVOpenGLBufferRef)

        v = CVBufferRetain(buf)
        self.failUnless(v is buf)
        CVBufferRelease(v)

        ctx = object()

        self.failUnlessArgHasType(CVBufferSetAttachment, 2, '@')
        self.failUnlessArgHasType(CVBufferSetAttachment, 0,  '@')
        CVBufferSetAttachment(buf, u"pyobjc.test",  ctx, kCVAttachmentMode_ShouldPropagate)

        self.failUnlessArgHasType(CVBufferGetAttachment, 0,  '@')
        self.failUnlessResultHasType(CVBufferGetAttachment, '@')
        self.failUnlessArgIsOut(CVBufferGetAttachment, 2)
        v, mode = CVBufferGetAttachment(buf, u"pyobjc.test", None)
        self.failUnless(v is ctx)
        self.failUnlessEqual(mode, kCVAttachmentMode_ShouldPropagate)

        self.failUnlessArgHasType(CVBufferGetAttachments, 0,  '@')
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failUnless("pyobjc.test" in v)

        self.failUnlessArgHasType(CVBufferSetAttachments, 0,  '@')
        CVBufferSetAttachments(buf, {
            "pyobjc.test2": 42,
            "pyobjc.test3": u"hello"
        }, kCVAttachmentMode_ShouldPropagate)

        self.failUnlessArgHasType(CVBufferPropagateAttachments, 0,  '@')
        self.failUnlessArgHasType(CVBufferPropagateAttachments, 1,  '@')
        CVBufferPropagateAttachments(buf, buf2)

        v = CVBufferGetAttachments(buf2, kCVAttachmentMode_ShouldPropagate)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failUnless("pyobjc.test2" in v)

        self.failUnlessArgHasType(CVBufferRemoveAttachment, 0,  '@')
        CVBufferRemoveAttachment(buf, "pyobjc.test")
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failIf("pyobjc.test" in v)

        self.failUnlessArgHasType(CVBufferRemoveAllAttachments, 0,  '@')
        CVBufferRemoveAllAttachments(buf)
        v = CVBufferGetAttachments(buf, kCVAttachmentMode_ShouldPropagate)
        self.failUnlessIsInstance(v, CFDictionaryRef)
        self.failIf("pyobjc.test2" in v)


if __name__ == "__main__":
    main()
