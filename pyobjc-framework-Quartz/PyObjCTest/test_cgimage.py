
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import sys
import os

import sys

try:
    long
except NameError:
    long = int

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')


class TestCGImage (TestCase):
    def testConstants(self):
        self.assertEqual(kCGImageAlphaNone, 0)
        self.assertEqual(kCGImageAlphaPremultipliedLast, 1)
        self.assertEqual(kCGImageAlphaPremultipliedFirst, 2)
        self.assertEqual(kCGImageAlphaLast, 3)
        self.assertEqual(kCGImageAlphaFirst, 4)
        self.assertEqual(kCGImageAlphaNoneSkipLast, 5)
        self.assertEqual(kCGImageAlphaNoneSkipFirst, 6)
        self.assertEqual(kCGImageAlphaOnly, 7)

        self.assertEqual(kCGBitmapAlphaInfoMask, 0x1F)
        self.assertEqual(kCGBitmapFloatComponents, (1 << 8))
        self.assertEqual(kCGBitmapByteOrderMask, 0x7000)
        self.assertEqual(kCGBitmapByteOrderDefault, (0 << 12))
        self.assertEqual(kCGBitmapByteOrder16Little, (1 << 12))
        self.assertEqual(kCGBitmapByteOrder32Little, (2 << 12))
        self.assertEqual(kCGBitmapByteOrder16Big, (3 << 12))
        self.assertEqual(kCGBitmapByteOrder32Big, (4 << 12))

        if sys.byteorder == 'big':
            self.assertEqual(kCGBitmapByteOrder16Host, kCGBitmapByteOrder16Big)
            self.assertEqual(kCGBitmapByteOrder32Host, kCGBitmapByteOrder32Big)
        else:
            self.assertEqual(kCGBitmapByteOrder16Host, kCGBitmapByteOrder16Little)
            self.assertEqual(kCGBitmapByteOrder32Host, kCGBitmapByteOrder32Little)

    def testFunctions(self):
        self.assertIsInstance(CGImageGetTypeID(), (int, long))

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 100 * 80))
        self.assertArgHasType(CGImageCreate, 9, objc._C_BOOL)
        self.assertResultIsCFRetained(CGImageCreate)
        image = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast,
                provider, None, False, kCGRenderingIntentDefault)
        self.assertIsInstance(image, CGImageRef)

        image2 = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaNoneSkipLast,
                provider, [0, 1, 0, 1, 0, 1], False, kCGRenderingIntentDefault)
        self.assertIsInstance(image2, CGImageRef)

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 20 * 10))
        self.assertArgHasType(CGImageMaskCreate, 7, objc._C_BOOL)
        self.assertResultIsCFRetained(CGImageMaskCreate)
        mask = CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
        self.assertIsInstance(mask, CGImageRef)

        self.assertResultIsCFRetained(CGImageCreateCopy)
        v = CGImageCreateCopy(image)
        self.assertIsInstance(v, CGImageRef)

        fn = '/System/Library/CoreServices/DefaultDesktop.jpg'
        if not os.path.exists(fn):
            fn = '/System/Library/CoreServices/DefaultDesktopServer.jpg'
        with open(fn, 'rb') as fp:
            data = fp.read()
        provider = CGDataProviderCreateWithCFData(buffer(data))
        self.assertResultIsCFRetained(CGImageCreateWithJPEGDataProvider)
        self.assertArgHasType(CGImageCreateWithJPEGDataProvider, 2, objc._C_BOOL)
        v = CGImageCreateWithJPEGDataProvider(provider, None, True, kCGRenderingIntentDefault)
        self.assertIsInstance(v, CGImageRef)

        fname = '/System/Library//CoreServices/Installer.app/Contents/PlugIns/Summary.bundle/Contents/Resources/Success.png'
        if not os.path.exists(fname):
            fname = '/System/Library//Frameworks/Automator.framework/Versions/A/Resources/GearActionDisabled.png'
        if not os.path.exists(fname):
            self.fail("test image doesn't exist")
        with open(fname, 'rb') as fp:
            data = fp.read()
        provider = CGDataProviderCreateWithCFData(buffer(data))
        self.assertResultIsCFRetained(CGImageCreateWithPNGDataProvider)
        self.assertArgHasType(CGImageCreateWithPNGDataProvider, 2, objc._C_BOOL)
        v = CGImageCreateWithPNGDataProvider(provider, None, True, kCGRenderingIntentDefault)
        self.assertIsInstance(v, CGImageRef)

        self.assertResultIsCFRetained(CGImageCreateWithImageInRect)
        v = CGImageCreateWithImageInRect(image, ((10, 10), (30, 40)))
        self.assertIsInstance(v, CGImageRef)

        self.assertResultIsCFRetained(CGImageCreateWithMask)
        v = CGImageCreateWithMask(image, mask)
        self.assertIsInstance(v, CGImageRef)


        self.assertResultIsCFRetained(CGImageCreateWithMaskingColors)
        v = CGImageCreateWithMaskingColors(image2, [0,255]*4)
        self.assertIsInstance(v, CGImageRef)

        self.assertResultIsCFRetained(CGImageCreateCopyWithColorSpace)
        v = CGImageCreateCopyWithColorSpace(image, CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB))
        self.assertIsInstance(v, CGImageRef)

        v = CGImageRetain(image)
        self.assertTrue(v is image)
        CGImageRelease(image)

        self.assertResultHasType(CGImageIsMask, objc._C_BOOL)
        self.assertTrue(CGImageIsMask(image) is False)
        self.assertTrue(CGImageIsMask(mask) is True)

        v = CGImageGetWidth(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetHeight(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetBitsPerComponent(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetBitsPerPixel(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetBytesPerRow(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetColorSpace(image)
        self.assertIsInstance(v, CGColorSpaceRef)

        v = CGImageGetAlphaInfo(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetDataProvider(image)
        self.assertIsInstance(v, CGDataProviderRef)

        v = CGImageGetDecode(image)
        self.assertTrue(v is objc.NULL)

        v = CGImageGetDecode(image2)
        self.assertIsInstance(v, objc.varlist)
        self.assertEqual(v[0], 0.0)
        self.assertEqual(v[1], 1.0)

        self.assertResultHasType(CGImageGetShouldInterpolate, objc._C_BOOL)
        v = CGImageGetShouldInterpolate(image)
        self.assertTrue(v is False)
        v = CGImageGetShouldInterpolate(mask)
        self.assertTrue(v is True)

        v = CGImageGetRenderingIntent(image)
        self.assertIsInstance(v, (int, long))

        v = CGImageGetBitmapInfo(image)
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
