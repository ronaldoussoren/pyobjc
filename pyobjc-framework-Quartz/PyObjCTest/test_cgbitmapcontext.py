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

    def test_constants(self):
        self.assertIsEnumType(Quartz.CGColorModel)
        self.assertEqual(Quartz.kCGColorModelNoColorant, 0 << 0)
        self.assertEqual(Quartz.kCGColorModelGray, 1 << 0)
        self.assertEqual(Quartz.kCGColorModelRGB, 1 << 1)
        self.assertEqual(Quartz.kCGColorModelCMYK, 1 << 2)
        self.assertEqual(Quartz.kCGColorModelLab, 1 << 3)
        self.assertEqual(Quartz.kCGColorModelDeviceN, 1 << 4)

        self.assertIsEnumType(Quartz.CGComponent)
        self.assertEqual(Quartz.kCGComponentUnknown, 0)
        self.assertEqual(Quartz.kCGComponentInteger8Bit, 1)
        self.assertEqual(Quartz.kCGComponentInteger10Bit, 6)
        self.assertEqual(Quartz.kCGComponentInteger16Bit, 2)
        self.assertEqual(Quartz.kCGComponentInteger32Bit, 3)
        self.assertEqual(Quartz.kCGComponentFloat16Bit, 5)
        self.assertEqual(Quartz.kCGComponentFloat32Bit, 4)

        self.assertIsEnumType(Quartz.CGBitmapLayout)
        self.assertEqual(Quartz.kCGBitmapLayoutAlphaOnly, 0)
        self.assertEqual(Quartz.kCGBitmapLayoutGray, 1)
        self.assertEqual(Quartz.kCGBitmapLayoutGrayAlpha, 2)
        self.assertEqual(Quartz.kCGBitmapLayoutRGBA, 3)
        self.assertEqual(Quartz.kCGBitmapLayoutARGB, 4)
        self.assertEqual(Quartz.kCGBitmapLayoutRGBX, 5)
        self.assertEqual(Quartz.kCGBitmapLayoutXRGB, 6)
        self.assertEqual(Quartz.kCGBitmapLayoutBGRA, 7)
        self.assertEqual(Quartz.kCGBitmapLayoutBGRX, 8)
        self.assertEqual(Quartz.kCGBitmapLayoutABGR, 9)
        self.assertEqual(Quartz.kCGBitmapLayoutXBGR, 10)
        self.assertEqual(Quartz.kCGBitmapLayoutCMYK, 11)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(Quartz.kCGAdaptiveMaximumBitDepth, str)

    def test_structs(self):
        v = Quartz.CGContentInfo()
        self.assertIsInstance(v.deepestImageComponent, int)
        self.assertIsInstance(v.contentColorModels, int)
        self.assertIsInstance(v.hasWideGamut, bool)
        self.assertIsInstance(v.hasTransparency, bool)
        self.assertIsInstance(v.largestContentHeadroom, float)

        v = Quartz.CGBitmapParameters()
        self.assertIsInstance(v.width, int)
        self.assertIsInstance(v.height, int)
        self.assertIsInstance(v.bytesPerPixel, int)
        self.assertIsInstance(v.alignedBytesPerRow, int)
        self.assertIsInstance(v.component, int)
        self.assertIsInstance(v.layout, int)
        self.assertIsInstance(v.format, int)
        self.assertIs(v.colorSpace, None)
        self.assertIsInstance(v.hasPremultipliedAlpha, bool)
        self.assertIsInstance(v.byteOrder, int)
        self.assertIsInstance(v.edrTargetHeadroom, float)

    @min_os_level("26.0")
    def test_functions26_0(self):
        self.assertResultIsCFRetained(Quartz.CGBitmapContextCreateAdaptive)
        # XXX: Add pass-by-reference annotations
        self.assertArgIsBlock(
            Quartz.CGBitmapContextCreateAdaptive,
            3,
            b"BN^"
            + Quartz.CGContentInfo.__typestr__
            + b"N^"
            + Quartz.CGBitmapParameters.__typestr__,
        )
        self.assertArgIsBlock(
            Quartz.CGBitmapContextCreateAdaptive,
            4,
            b"^{CGRenderingBufferProvider=}^"
            + Quartz.CGContentInfo.__typestr__
            + b"^"
            + Quartz.CGBitmapParameters.__typestr__,
        )
        self.assertArgIsBlock(
            Quartz.CGBitmapContextCreateAdaptive,
            5,
            b"v^{CGRenderingBufferProvider=}^"
            + Quartz.CGContentInfo.__typestr__
            + b"^"
            + Quartz.CGBitmapParameters.__typestr__,
        )
        self.assertArgIsBlock(
            Quartz.CGBitmapContextCreateAdaptive,
            6,
            b"v^{__CFError=}^"
            + Quartz.CGContentInfo.__typestr__
            + b"^"
            + Quartz.CGBitmapParameters.__typestr__,
        )
