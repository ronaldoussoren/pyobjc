from PyObjCTools.TestSupport import *
from Quartz import *

from CoreFoundation import CFArrayRef
from Foundation import NSMutableData

import sys

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')



class TestCGImageDestination (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGImageDestinationRef)

    def testConstants(self):
        self.assertIsInstance(kCGImageDestinationLossyCompressionQuality, unicode)
        self.assertIsInstance(kCGImageDestinationBackgroundColor, unicode)

    def testFunctions(self):
        self.assertIsInstance(CGImageDestinationGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CGImageDestinationCopyTypeIdentifiers)
        v = CGImageDestinationCopyTypeIdentifiers()
        self.assertIsInstance(v, CFArrayRef)
        if v:
            self.assertIsInstance(v[0], unicode)

        data = NSMutableData.data() 
        self.assertResultIsCFRetained(CGImageDestinationCreateWithData)
        dest = CGImageDestinationCreateWithData(data, v[0], 1, None)
        self.assertIsInstance(dest, CGImageDestinationRef)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertResultIsCFRetained(CGImageDestinationCreateWithURL)
        dest = CGImageDestinationCreateWithURL(url, "public.tiff", 2, None)
        self.assertIsInstance(dest, CGImageDestinationRef)

        CGImageDestinationSetProperties(dest, {u'key': u'value'})

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 100 * 80))
        img = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), 
                kCGImageAlphaPremultipliedLast, provider, None, False, kCGRenderingIntentDefault)
        self.assertIsInstance(img, CGImageRef)

        CGImageDestinationAddImage(dest, img, None)

        url = CFURLCreateWithFileSystemPath(None,
            "/System/Library//ColorSync/Calibrators/Display Calibrator.app/Contents/Resources/bullet.tif", 
            kCFURLPOSIXPathStyle, False)

        isrc = CGImageSourceCreateWithURL(url, None)
        CGImageDestinationAddImageFromSource(dest,  isrc, 0, None)

        self.assertResultHasType(CGImageDestinationFinalize, objc._C_BOOL)
        v = CGImageDestinationFinalize(dest)
        self.assertTrue(v is True)

        dta = NSMutableData.alloc().init()
        cons = CGDataConsumerCreateWithCFData(dta)

        self.assertResultIsCFRetained(CGImageDestinationCreateWithDataConsumer)
        c = CGImageDestinationCreateWithDataConsumer(cons, 'public.tiff', 1, None)
        self.assertIsInstance(c, CGImageDestinationRef)

if __name__ == "__main__":
    main()
