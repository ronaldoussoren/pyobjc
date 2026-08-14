import os
import tempfile

import Quartz
from Foundation import NSMutableData
from PyObjCTools.TestSupport import TestCase


class TestCGDataConsumer(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CGDataConsumerRef)

    def test_functions(self):
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

        def write_pdf(consumer):
            ctx = Quartz.CGPDFContextCreate(
                consumer, Quartz.CGRectMake(0, 0, 500, 500), None
            )
            self.assertIsInstance(ctx, Quartz.CGContextRef)
            Quartz.CGContextBeginPage(ctx, None)
            Quartz.CGContextFillRect(ctx, ((10, 10), (50, 30)))
            Quartz.CGContextEndPage(ctx)
            Quartz.CGContextFlush(ctx)
            Quartz.CGPDFContextClose(ctx)

            del ctx

        output = []
        released = []
        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            Quartz.CGDataConsumerCreate()

        with self.assertRaisesRegex(
            TypeError, "callbacks must be a tuple of two callables"
        ):
            Quartz.CGDataConsumerCreate(output, 42)

        with self.assertRaisesRegex(
            TypeError, "callbacks must be a tuple of two callables"
        ):
            Quartz.CGDataConsumerCreate(output, ())

        with self.assertRaisesRegex(TypeError, "putBytes is not a callable$"):
            Quartz.CGDataConsumerCreate(output, (42, release))

        with self.assertRaisesRegex(TypeError, "release is not a callable or None"):
            Quartz.CGDataConsumerCreate(output, (putBytes, 42))

        consumer = Quartz.CGDataConsumerCreate(output, (putBytes, release))
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        write_pdf(consumer)

        del consumer

        self.assertNotEqual(len(output), 0)
        self.assertNotEqual(len(released), 0)

        def putBytes_raises(info, a_buffer, bufsize):
            raise RuntimeError("put bytes error")

        def putBytes_invalid(info, a_buffer, bufsize):
            return str(bufsize)

        def release_raises(info):
            raise RuntimeError("release error")

        output = []
        released = []
        consumer = Quartz.CGDataConsumerCreate(output, (putBytes_raises, None))
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        with self.assertRaisesRegex(RuntimeError, "put bytes error"):
            write_pdf(consumer)

        del consumer

        output = []
        released = []
        consumer = Quartz.CGDataConsumerCreate(output, (putBytes_invalid, None))
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            write_pdf(consumer)

        del consumer

        output = []
        released = []
        consumer = Quartz.CGDataConsumerCreate(output, (putBytes, release_raises))
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        write_pdf(consumer)

        orig_stderr = os.dup(2)
        with tempfile.TemporaryFile() as stream:
            os.dup2(stream.fileno(), 2)
            try:
                del consumer
            finally:
                os.dup2(orig_stderr, 2)

            stream.seek(0)
            stderr = stream.read().decode()

        self.assertIn(
            "PyObjC: Exception during dealloc of proxy: <class 'RuntimeError'>: release error",
            stderr,
        )

        self.assertNotEqual(len(output), 0)
        self.assertEqual(len(released), 0)
