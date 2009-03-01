
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Foundation import NSMutableData
import os

class TestCGDataConsumer (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGDataConsumerRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CGDataConsumerGetTypeID(), (int, long))

        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        try:
            consumer = CGDataConsumerCreateWithURL(url)
            self.failUnlessIsInstance(consumer, CGDataConsumerRef)

            data = NSMutableData.data()
            self.failUnlessIsInstance(data, CFMutableDataRef)

            consumer = CGDataConsumerCreateWithCFData(data)
            self.failUnlessIsInstance(consumer, CGDataConsumerRef)

            v = CGDataConsumerRetain(consumer)
            self.failUnless(v is consumer)
            CGDataConsumerRelease(consumer)

        finally:
            del url
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        def putBytes(info, buffer, bufsize):
            self.failUnlessIsInstance(buffer, str)
            self.failUnlessEqual(len(buffer), bufsize)
            info.append(buffer)
            return bufsize

        def release(info):
            released.append(info)


        output = []
        released = []
        consumer = CGDataConsumerCreate(output, (putBytes, release))
        self.failUnlessIsInstance(consumer, CGDataConsumerRef)

        ctx = CGPDFContextCreate(consumer, CGRectMake(0, 0, 500, 500), None)
        self.failUnlessIsInstance(ctx, CGContextRef)
        CGContextBeginPage(ctx, None)
        CGContextFillRect(ctx, ((10, 10), (50, 30)))
        CGContextEndPage(ctx)
        CGContextFlush(ctx)
        CGPDFContextClose(ctx)

        del ctx
        del consumer

        self.failIfEqual(len(output), 0)
        self.failIfEqual(len(released), 0)


if __name__ == "__main__":
    main()
