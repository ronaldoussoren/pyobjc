
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import sys

class TestCGImage (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGImageAlphaNone, 0)
        self.failUnlessEqual(kCGImageAlphaPremultipliedLast, 1)
        self.failUnlessEqual(kCGImageAlphaPremultipliedFirst, 2)
        self.failUnlessEqual(kCGImageAlphaLast, 3)
        self.failUnlessEqual(kCGImageAlphaFirst, 4)
        self.failUnlessEqual(kCGImageAlphaNoneSkipLast, 5)
        self.failUnlessEqual(kCGImageAlphaNoneSkipFirst, 6)
        self.failUnlessEqual(kCGImageAlphaOnly, 7)

        self.failUnlessEqual(kCGBitmapAlphaInfoMask, 0x1F)
        self.failUnlessEqual(kCGBitmapFloatComponents, (1 << 8))
        self.failUnlessEqual(kCGBitmapByteOrderMask, 0x7000)
        self.failUnlessEqual(kCGBitmapByteOrderDefault, (0 << 12))
        self.failUnlessEqual(kCGBitmapByteOrder16Little, (1 << 12))
        self.failUnlessEqual(kCGBitmapByteOrder32Little, (2 << 12))
        self.failUnlessEqual(kCGBitmapByteOrder16Big, (3 << 12))
        self.failUnlessEqual(kCGBitmapByteOrder32Big, (4 << 12))

        if sys.byteorder == 'big':
            self.failUnlessEqual(kCGBitmapByteOrder16Host, kCGBitmapByteOrder16Big)
            self.failUnlessEqual(kCGBitmapByteOrder32Host, kCGBitmapByteOrder32Big)
        else:
            self.failUnlessEqual(kCGBitmapByteOrder16Host, kCGBitmapByteOrder16Little)
            self.failUnlessEqual(kCGBitmapByteOrder32Host, kCGBitmapByteOrder32Little)

    def testFunctions(self):
        self.failUnlessIsInstance(CGImageGetTypeID(), (int, long))

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 100 * 80))
        self.failUnlessArgHasType(CGImageCreate, 9, objc._C_BOOL)
        self.failUnlessResultIsCFRetained(CGImageCreate)
        image = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast,
                provider, None, False, kCGRenderingIntentDefault)
        self.failUnlessIsInstance(image, CGImageRef)

        image2 = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaNoneSkipLast,
                provider, [0, 1, 0, 1, 0, 1], False, kCGRenderingIntentDefault)
        self.failUnlessIsInstance(image2, CGImageRef)

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 20 * 10))
        self.failUnlessArgHasType(CGImageMaskCreate, 7, objc._C_BOOL)
        self.failUnlessResultIsCFRetained(CGImageMaskCreate)
        mask = CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
        self.failUnlessIsInstance(mask, CGImageRef)

        self.failUnlessResultIsCFRetained(CGImageCreateCopy)
        v = CGImageCreateCopy(image)
        self.failUnlessIsInstance(v, CGImageRef)

        provider = CGDataProviderCreateWithCFData(buffer(
            open('/System/Library/CoreServices/DefaultDesktop.jpg', 'rb').read()))
        self.failUnlessResultIsCFRetained(CGImageCreateWithJPEGDataProvider)
        self.failUnlessArgHasType(CGImageCreateWithJPEGDataProvider, 2, objc._C_BOOL)
        v = CGImageCreateWithJPEGDataProvider(provider, None, True, kCGRenderingIntentDefault)
        self.failUnlessIsInstance(v, CGImageRef)

        provider = CGDataProviderCreateWithCFData(buffer(
            open('/System/Library//CoreServices/Installer.app/Contents/PlugIns/Summary.bundle/Contents/Resources/Success.png', 'rb').read()))
        self.failUnlessResultIsCFRetained(CGImageCreateWithPNGDataProvider)
        self.failUnlessArgHasType(CGImageCreateWithPNGDataProvider, 2, objc._C_BOOL)
        v = CGImageCreateWithPNGDataProvider(provider, None, True, kCGRenderingIntentDefault)
        self.failUnlessIsInstance(v, CGImageRef)

        self.failUnlessResultIsCFRetained(CGImageCreateWithImageInRect)
        v = CGImageCreateWithImageInRect(image, ((10, 10), (30, 40))) 
        self.failUnlessIsInstance(v, CGImageRef)

        self.failUnlessResultIsCFRetained(CGImageCreateWithMask)
        v = CGImageCreateWithMask(image, mask)
        self.failUnlessIsInstance(v, CGImageRef)

        
        self.failUnlessResultIsCFRetained(CGImageCreateWithMaskingColors)
        v = CGImageCreateWithMaskingColors(image2, [0,255]*4)
        self.failUnlessIsInstance(v, CGImageRef)

        self.failUnlessResultIsCFRetained(CGImageCreateCopyWithColorSpace)
        v = CGImageCreateCopyWithColorSpace(image, CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB))
        self.failUnlessIsInstance(v, CGImageRef)

        v = CGImageRetain(image)
        self.failUnless(v is image)
        CGImageRelease(image)

        self.failUnlessResultHasType(CGImageIsMask, objc._C_BOOL)
        self.failUnless(CGImageIsMask(image) is False)
        self.failUnless(CGImageIsMask(mask) is True)

        v = CGImageGetWidth(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetHeight(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetBitsPerComponent(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetBitsPerPixel(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetBytesPerRow(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetColorSpace(image)
        self.failUnlessIsInstance(v, CGColorSpaceRef)

        v = CGImageGetAlphaInfo(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetDataProvider(image)
        self.failUnlessIsInstance(v, CGDataProviderRef)

        v = CGImageGetDecode(image)
        self.failUnless(v is objc.NULL)

        v = CGImageGetDecode(image2)
        self.failUnlessIsInstance(v, objc.varlist)
        self.failUnlessEqual(v[0], 0.0)
        self.failUnlessEqual(v[1], 1.0)

        self.failUnlessResultHasType(CGImageGetShouldInterpolate, objc._C_BOOL)
        v = CGImageGetShouldInterpolate(image)
        self.failUnless(v is False)
        v = CGImageGetShouldInterpolate(mask)
        self.failUnless(v is True)

        v = CGImageGetRenderingIntent(image)
        self.failUnlessIsInstance(v, (int, long))

        v = CGImageGetBitmapInfo(image)
        self.failUnlessIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
