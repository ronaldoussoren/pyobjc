
from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
from Foundation import NSMutableData
import os

try:
    long
except NameError:
    long = int

class TestCGDataConsumer (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGDataConsumerRef)

    def testFunctions(self):
        self.assertIsInstance(CGDataConsumerGetTypeID(), (int, long))

        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        try:
            consumer = CGDataConsumerCreateWithURL(url)
            self.assertIsInstance(consumer, CGDataConsumerRef)

            data = NSMutableData.data()
            self.assertIsInstance(data, CFMutableDataRef)

            consumer = CGDataConsumerCreateWithCFData(data)
            self.assertIsInstance(consumer, CGDataConsumerRef)

            v = CGDataConsumerRetain(consumer)
            self.assertTrue(v is consumer)
            CGDataConsumerRelease(consumer)

        finally:
            del url
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        def putBytes(info, buffer, bufsize):
            self.assertIsInstance(buffer, bytes)
            self.assertEqual(len(buffer), bufsize)
            info.append(buffer)
            return bufsize

        def release(info):
            released.append(info)


        output = []
        released = []
        consumer = CGDataConsumerCreate(output, (putBytes, release))
        self.assertIsInstance(consumer, CGDataConsumerRef)

        ctx = CGPDFContextCreate(consumer, CGRectMake(0, 0, 500, 500), None)
        self.assertIsInstance(ctx, CGContextRef)
        CGContextBeginPage(ctx, None)
        CGContextFillRect(ctx, ((10, 10), (50, 30)))
        CGContextEndPage(ctx)
        CGContextFlush(ctx)
        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(ctx)

        del ctx
        del consumer

        self.assertNotEqual(len(output), 0)
        self.assertNotEqual(len(released), 0)


if __name__ == "__main__":
    main()
