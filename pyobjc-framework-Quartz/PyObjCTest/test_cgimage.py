import os
import sys

from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz

import objc


class TestCGImage(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGImagePixelFormatMask, 0xF0000)
        self.assertEqual(Quartz.kCGImagePixelFormatPacked, 0 << 16)
        self.assertEqual(Quartz.kCGImagePixelFormatRGB555, 1 << 16)
        self.assertEqual(Quartz.kCGImagePixelFormatRGB565, 2 << 16)
        self.assertEqual(Quartz.kCGImagePixelFormatRGB101010, 3 << 16)
        self.assertEqual(Quartz.kCGImagePixelFormatRGBCIF10, 4 << 16)

        self.assertEqual(Quartz.kCGImageAlphaNone, 0)
        self.assertEqual(Quartz.kCGImageAlphaPremultipliedLast, 1)
        self.assertEqual(Quartz.kCGImageAlphaPremultipliedFirst, 2)
        self.assertEqual(Quartz.kCGImageAlphaLast, 3)
        self.assertEqual(Quartz.kCGImageAlphaFirst, 4)
        self.assertEqual(Quartz.kCGImageAlphaNoneSkipLast, 5)
        self.assertEqual(Quartz.kCGImageAlphaNoneSkipFirst, 6)
        self.assertEqual(Quartz.kCGImageAlphaOnly, 7)

        self.assertEqual(Quartz.kCGBitmapAlphaInfoMask, 0x1F)
        self.assertEqual(Quartz.kCGBitmapFloatComponents, (1 << 8))
        self.assertEqual(Quartz.kCGBitmapByteOrderMask, 0x7000)
        self.assertEqual(Quartz.kCGBitmapByteOrderDefault, (0 << 12))
        self.assertEqual(Quartz.kCGBitmapByteOrder16Little, (1 << 12))
        self.assertEqual(Quartz.kCGBitmapByteOrder32Little, (2 << 12))
        self.assertEqual(Quartz.kCGBitmapByteOrder16Big, (3 << 12))
        self.assertEqual(Quartz.kCGBitmapByteOrder32Big, (4 << 12))

        if sys.byteorder == "big":
            self.assertEqual(
                Quartz.kCGBitmapByteOrder16Host, Quartz.kCGBitmapByteOrder16Big
            )
            self.assertEqual(
                Quartz.kCGBitmapByteOrder32Host, Quartz.kCGBitmapByteOrder32Big
            )
        else:
            self.assertEqual(
                Quartz.kCGBitmapByteOrder16Host, Quartz.kCGBitmapByteOrder16Little
            )
            self.assertEqual(
                Quartz.kCGBitmapByteOrder32Host, Quartz.kCGBitmapByteOrder32Little
            )

        self.assertEqual(Quartz.kCGImageByteOrderMask, 0x7000)
        self.assertEqual(Quartz.kCGImageByteOrderDefault, 0 << 12)
        self.assertEqual(Quartz.kCGImageByteOrder16Little, 1 << 12)
        self.assertEqual(Quartz.kCGImageByteOrder32Little, 2 << 12)
        self.assertEqual(Quartz.kCGImageByteOrder16Big, 3 << 12)
        self.assertEqual(Quartz.kCGImageByteOrder32Big, 4 << 12)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGImageGetTypeID(), int)

        provider = Quartz.CGDataProviderCreateWithCFData(b"1" * 4 * 100 * 80)
        self.assertArgHasType(Quartz.CGImageCreate, 9, objc._C_BOOL)
        self.assertResultIsCFRetained(Quartz.CGImageCreate)
        image = Quartz.CGImageCreate(
            100,
            80,
            8,
            32,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaPremultipliedLast,
            provider,
            None,
            False,
            Quartz.kCGRenderingIntentDefault,
        )
        self.assertIsInstance(image, Quartz.CGImageRef)

        image2 = Quartz.CGImageCreate(
            100,
            80,
            8,
            32,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaNoneSkipLast,
            provider,
            [0, 1, 0, 1, 0, 1],
            False,
            Quartz.kCGRenderingIntentDefault,
        )
        self.assertIsInstance(image2, Quartz.CGImageRef)

        provider = Quartz.CGDataProviderCreateWithCFData(b"1" * 4 * 20 * 10)
        self.assertArgHasType(Quartz.CGImageMaskCreate, 7, objc._C_BOOL)
        self.assertResultIsCFRetained(Quartz.CGImageMaskCreate)
        mask = Quartz.CGImageMaskCreate(20, 10, 8, 32, 80, provider, None, True)
        self.assertIsInstance(mask, Quartz.CGImageRef)

        self.assertResultIsCFRetained(Quartz.CGImageCreateCopy)
        v = Quartz.CGImageCreateCopy(image)
        self.assertIsInstance(v, Quartz.CGImageRef)

        fn = "/System/Library/CoreServices/DefaultDesktop.jpg"
        if not os.path.exists(fn):
            fn = "/System/Library/CoreServices/DefaultDesktopServer.jpg"
            if not os.path.exists(fn):
                fn = "/System/Library/CoreServices//RemoteManagement/ARDAgent.app/Contents/Resources/Lock.jpg"
        with open(fn, "rb") as fp:
            data = fp.read()
        provider = Quartz.CGDataProviderCreateWithCFData(data)
        self.assertResultIsCFRetained(Quartz.CGImageCreateWithJPEGDataProvider)
        self.assertArgHasType(Quartz.CGImageCreateWithJPEGDataProvider, 2, objc._C_BOOL)
        v = Quartz.CGImageCreateWithJPEGDataProvider(
            provider, None, True, Quartz.kCGRenderingIntentDefault
        )
        self.assertIsInstance(v, Quartz.CGImageRef)

        fname = "/System/Library//CoreServices/Installer.app/Contents/PlugIns/Summary.bundle/Contents/Resources/Success.png"
        if not os.path.exists(fname):
            fname = "/System/Library//Frameworks/Automator.framework/Versions/A/Resources/GearActionDisabled.png"
            if not os.path.exists(fname):
                fname = "/System/Library//Frameworks/Automator.framework/Versions/A/Resources/GlossyStatusViewMid.png"
        if not os.path.exists(fname):
            self.fail("test image doesn't exist")

        with open(fname, "rb") as fp:
            data = fp.read()
        provider = Quartz.CGDataProviderCreateWithCFData(data)
        self.assertResultIsCFRetained(Quartz.CGImageCreateWithPNGDataProvider)
        self.assertArgHasType(Quartz.CGImageCreateWithPNGDataProvider, 2, objc._C_BOOL)
        v = Quartz.CGImageCreateWithPNGDataProvider(
            provider, None, True, Quartz.kCGRenderingIntentDefault
        )
        self.assertIsInstance(v, Quartz.CGImageRef)

        self.assertResultIsCFRetained(Quartz.CGImageCreateWithImageInRect)
        v = Quartz.CGImageCreateWithImageInRect(image, ((10, 10), (30, 40)))
        self.assertIsInstance(v, Quartz.CGImageRef)

        self.assertResultIsCFRetained(Quartz.CGImageCreateWithMask)
        v = Quartz.CGImageCreateWithMask(image, mask)
        self.assertIsInstance(v, Quartz.CGImageRef)

        self.assertResultIsCFRetained(Quartz.CGImageCreateWithMaskingColors)
        v = Quartz.CGImageCreateWithMaskingColors(image2, [0, 255] * 4)
        self.assertIsInstance(v, Quartz.CGImageRef)

        self.assertResultIsCFRetained(Quartz.CGImageCreateCopyWithColorSpace)
        v = Quartz.CGImageCreateCopyWithColorSpace(
            image, Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceGenericRGB)
        )
        self.assertIsInstance(v, Quartz.CGImageRef)

        v = Quartz.CGImageRetain(image)
        self.assertTrue(v is image)
        Quartz.CGImageRelease(image)

        self.assertResultHasType(Quartz.CGImageIsMask, objc._C_BOOL)
        self.assertTrue(Quartz.CGImageIsMask(image) is False)
        self.assertTrue(Quartz.CGImageIsMask(mask) is True)

        v = Quartz.CGImageGetWidth(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetHeight(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetBitsPerComponent(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetBitsPerPixel(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetBytesPerRow(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetColorSpace(image)
        self.assertIsInstance(v, Quartz.CGColorSpaceRef)

        v = Quartz.CGImageGetAlphaInfo(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetDataProvider(image)
        self.assertIsInstance(v, Quartz.CGDataProviderRef)

        v = Quartz.CGImageGetDecode(image)
        self.assertTrue(v is objc.NULL)

        v = Quartz.CGImageGetDecode(image2)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertEqual(v[0], 0.0)
            self.assertEqual(v[1], 1.0)

        self.assertResultHasType(Quartz.CGImageGetShouldInterpolate, objc._C_BOOL)
        v = Quartz.CGImageGetShouldInterpolate(image)
        self.assertTrue(v is False)
        v = Quartz.CGImageGetShouldInterpolate(mask)
        self.assertTrue(v is True)

        v = Quartz.CGImageGetRenderingIntent(image)
        self.assertIsInstance(v, int)

        v = Quartz.CGImageGetBitmapInfo(image)
        self.assertIsInstance(v, int)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        fn = "/System/Library/CoreServices/DefaultDesktop.jpg"
        if not os.path.exists(fn):
            fn = "/System/Library/CoreServices/DefaultDesktopServer.jpg"
            if not os.path.exists(fn):
                fn = "/System/Library/CoreServices//RemoteManagement/ARDAgent.app/Contents/Resources/Lock.jpg"
        with open(fn, "rb") as fp:
            data = fp.read()
        provider = Quartz.CGDataProviderCreateWithCFData(data)
        self.assertResultIsCFRetained(Quartz.CGImageCreateWithJPEGDataProvider)
        self.assertArgHasType(Quartz.CGImageCreateWithJPEGDataProvider, 2, objc._C_BOOL)
        image = Quartz.CGImageCreateWithJPEGDataProvider(
            provider, None, True, Quartz.kCGRenderingIntentDefault
        )
        self.assertIsInstance(image, Quartz.CGImageRef)

        v = Quartz.CGImageGetUTType(image)
        self.assertIsInstance(v, str)

    @min_os_level("10.14")
    def testFunctions10_14(self):
        Quartz.CGImageGetByteOrderInfo
        Quartz.CGImageGetPixelFormatInfo
