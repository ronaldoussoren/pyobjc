
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import array

try:
    long
except NameError:
    long = int

class TestCGBitmapContext (TestCase):
    def testFunctions(self):
        bytes_val = array.array('B', (0 for i in range(100*80*4)))
        self.assertIsInstance(bytes_val, array.array)
        self.assertEqual(len(bytes_val), 100*80*4)
        ctx = CGBitmapContextCreate(bytes_val, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast)
        self.assertIsInstance(ctx, CGContextRef)

        buf = CGBitmapContextGetData(ctx)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], bytes)

        self.assertEqual(CGBitmapContextGetWidth(ctx), 100)
        self.assertEqual(CGBitmapContextGetHeight(ctx), 80)
        self.assertEqual(CGBitmapContextGetBitsPerComponent(ctx), 8)
        self.assertEqual(CGBitmapContextGetBitsPerPixel(ctx), 32)
        self.assertEqual(CGBitmapContextGetBytesPerRow(ctx), 400)

        v = CGBitmapContextGetColorSpace(ctx)
        self.assertIsInstance(v, CGColorSpaceRef)

        v = CGBitmapContextGetAlphaInfo(ctx)
        self.assertIsInstance(v, (int, long))

        v = CGBitmapContextGetBitmapInfo(ctx)
        self.assertIsInstance(v, (int, long))

        img = CGBitmapContextCreateImage(ctx)
        self.assertIsInstance(img, CGImageRef)


    @min_os_level('10.6')
    def testFunctions10_6(self):
        bytes_val = array.array('B', (0 for i in range(100*80*4)))
        ctx = CGBitmapContextCreateWithData(bytes_val, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast, None, None)
        self.assertIsInstance(ctx, CGContextRef)
        del ctx

        list = []
        release_info = object()
        def callback(info, data):
            list.append((info, data))

        ctx = CGBitmapContextCreateWithData(bytes_val, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast, callback, release_info)
        self.assertIsInstance(ctx, CGContextRef)
        del ctx

        self.assertEquals(len(list), 1)
        self.assertIs(list[0][0], release_info)
        self.assertIs(list[0][1], bytes_val)


if __name__ == "__main__":
    main()
