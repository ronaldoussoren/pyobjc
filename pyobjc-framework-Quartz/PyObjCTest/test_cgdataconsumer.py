import os

import Quartz
from Foundation import NSMutableData
from PyObjCTools.TestSupport import TestCase


class TestCGDataConsumer(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGDataConsumerRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGDataConsumerGetTypeID(), int)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        try:
            consumer = Quartz.CGDataConsumerCreateWithURL(url)
            self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

            data = NSMutableData.data()
            self.assertIsInstance(data, Quartz.CFMutableDataRef)

            consumer = Quartz.CGDataConsumerCreateWithCFData(data)
            self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

            v = Quartz.CGDataConsumerRetain(consumer)
            self.assertTrue(v is consumer)
            Quartz.CGDataConsumerRelease(consumer)

        finally:
            del url
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        def putBytes(info, a_buffer, bufsize):
            self.assertIsInstance(a_buffer, bytes)
            self.assertEqual(len(a_buffer), bufsize)
            info.append(a_buffer)
            return bufsize

        def release(info):
            released.append(info)

        output = []
        released = []
        consumer = Quartz.CGDataConsumerCreate(output, (putBytes, release))
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        ctx = Quartz.CGPDFContextCreate(
            consumer, Quartz.CGRectMake(0, 0, 500, 500), None
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)
        Quartz.CGContextBeginPage(ctx, None)
        Quartz.CGContextFillRect(ctx, ((10, 10), (50, 30)))
        Quartz.CGContextEndPage(ctx)
        Quartz.CGContextFlush(ctx)
        if hasattr(Quartz, "CGPDFContextClose"):
            Quartz.CGPDFContextClose(ctx)

        del ctx
        del consumer

        self.assertNotEqual(len(output), 0)
        self.assertNotEqual(len(released), 0)
