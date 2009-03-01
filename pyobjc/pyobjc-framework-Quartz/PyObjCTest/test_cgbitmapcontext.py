
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import array

class TestCGBitmapContext (TestCase):
    def testFunctions(self):
        bytes = array.array('B', (0 for i in xrange(100*80*4)))
        self.failUnlessIsInstance(bytes, array.array)
        self.failUnlessEqual(len(bytes), 100*80*4)
        ctx = CGBitmapContextCreate(bytes, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast)
        self.failUnlessIsInstance(ctx, CGContextRef)

        buf = CGBitmapContextGetData(ctx)
        self.failUnlessIsInstance(buf, objc.varlist)
        self.failUnlessIsInstance(buf[0], str)

        self.failUnlessEqual(CGBitmapContextGetWidth(ctx), 100)
        self.failUnlessEqual(CGBitmapContextGetHeight(ctx), 80)
        self.failUnlessEqual(CGBitmapContextGetBitsPerComponent(ctx), 8)
        self.failUnlessEqual(CGBitmapContextGetBitsPerPixel(ctx), 32)
        self.failUnlessEqual(CGBitmapContextGetBytesPerRow(ctx), 400)

        v = CGBitmapContextGetColorSpace(ctx)
        self.failUnlessIsInstance(v, CGColorSpaceRef)

        v = CGBitmapContextGetAlphaInfo(ctx)
        self.failUnlessIsInstance(v, (int, long))

        v = CGBitmapContextGetBitmapInfo(ctx)
        self.failUnlessIsInstance(v, (int, long))

        img = CGBitmapContextCreateImage(ctx)
        self.failUnlessIsInstance(img, CGImageRef)


if __name__ == "__main__":
    main()
