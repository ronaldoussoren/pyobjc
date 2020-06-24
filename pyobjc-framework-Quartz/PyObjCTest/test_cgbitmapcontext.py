import array
import objc

from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGBitmapContext(TestCase):
    def testFunctions(self):
        bytes_val = array.array("B", (0 for i in range(100 * 80 * 4)))
        self.assertIsInstance(bytes_val, array.array)
        self.assertEqual(len(bytes_val), 100 * 80 * 4)
        ctx = Quartz.CGBitmapContextCreate(
            bytes_val,
            100,
            80,
            8,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaPremultipliedLast,
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)

        buf = Quartz.CGBitmapContextGetData(ctx)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], bytes)

        self.assertEqual(Quartz.CGBitmapContextGetWidth(ctx), 100)
        self.assertEqual(Quartz.CGBitmapContextGetHeight(ctx), 80)
        self.assertEqual(Quartz.CGBitmapContextGetBitsPerComponent(ctx), 8)
        self.assertEqual(Quartz.CGBitmapContextGetBitsPerPixel(ctx), 32)
        self.assertEqual(Quartz.CGBitmapContextGetBytesPerRow(ctx), 400)

        v = Quartz.CGBitmapContextGetColorSpace(ctx)
        self.assertIsInstance(v, Quartz.CGColorSpaceRef)

        v = Quartz.CGBitmapContextGetAlphaInfo(ctx)
        self.assertIsInstance(v, int)

        v = Quartz.CGBitmapContextGetBitmapInfo(ctx)
        self.assertIsInstance(v, int)

        img = Quartz.CGBitmapContextCreateImage(ctx)
        self.assertIsInstance(img, Quartz.CGImageRef)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        bytes_val = array.array("B", (0 for i in range(100 * 80 * 4)))
        ctx = Quartz.CGBitmapContextCreateWithData(
            bytes_val,
            100,
            80,
            8,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaPremultipliedLast,
            None,
            None,
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)
        del ctx

        a_list = []
        release_info = object()

        def callback(info, data):
            a_list.append((info, data))

        ctx = Quartz.CGBitmapContextCreateWithData(
            bytes_val,
            100,
            80,
            8,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaPremultipliedLast,
            callback,
            release_info,
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)
        del ctx

        self.assertEqual(len(a_list), 1)
        self.assertIs(a_list[0][0], release_info)
        self.assertIs(a_list[0][1], bytes_val)
