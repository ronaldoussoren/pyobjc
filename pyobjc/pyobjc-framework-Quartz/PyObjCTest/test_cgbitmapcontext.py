
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import array

class TestCGBitmapContext (TestCase):
    def testFunctions(self):
        bytes = array.array('B', (0 for i in xrange(100*80*4)))
        self.assertIsInstance(bytes, array.array)
        self.assertEqual(len(bytes), 100*80*4)
        ctx = CGBitmapContextCreate(bytes, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast)
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


    def testFunctions106_(self):
        self.fail("CGBitmapContextCreateWithData: manual wrapper")


if __name__ == "__main__":
    main()
