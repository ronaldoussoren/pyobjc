from PyObjCTools.TestSupport import *
from Quartz import *

from CoreFoundation import CFArrayRef
from Foundation import NSMutableData

class TestCGImageDestination (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGImageDestinationRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCGImageDestinationLossyCompressionQuality, unicode)
        self.failUnlessIsInstance(kCGImageDestinationBackgroundColor, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CGImageDestinationGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CGImageDestinationCopyTypeIdentifiers)
        v = CGImageDestinationCopyTypeIdentifiers()
        self.failUnlessIsInstance(v, CFArrayRef)
        if v:
            self.failUnlessIsInstance(v[0], unicode)

        data = NSMutableData.data() 
        self.failUnlessResultIsCFRetained(CGImageDestinationCreateWithData)
        dest = CGImageDestinationCreateWithData(data, v[0], 1, None)
        self.failUnlessIsInstance(dest, CGImageDestinationRef)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessResultIsCFRetained(CGImageDestinationCreateWithURL)
        dest = CGImageDestinationCreateWithURL(url, "public.tiff", 2, None)
        self.failUnlessIsInstance(dest, CGImageDestinationRef)

        CGImageDestinationSetProperties(dest, {u'key': u'value'})

        provider = CGDataProviderCreateWithCFData(buffer("1" * 4 * 100 * 80))
        img = CGImageCreate(100, 80, 8, 32, 400, CGColorSpaceCreateDeviceRGB(), 
                kCGImageAlphaPremultipliedLast, provider, None, False, kCGRenderingIntentDefault)
        self.failUnlessIsInstance(img, CGImageRef)

        CGImageDestinationAddImage(dest, img, None)

        url = CFURLCreateWithFileSystemPath(None,
            "/System/Library//ColorSync/Calibrators/Display Calibrator.app/Contents/Resources/bullet.tif", 
            kCFURLPOSIXPathStyle, False)

        isrc = CGImageSourceCreateWithURL(url, None)
        CGImageDestinationAddImageFromSource(dest,  isrc, 0, None)

        self.failUnlessResultHasType(CGImageDestinationFinalize, objc._C_BOOL)
        v = CGImageDestinationFinalize(dest)
        self.failUnless(v is True)

        dta = NSMutableData.alloc().init()
        cons = CGDataConsumerCreateWithCFData(dta)

        self.failUnlessResultIsCFRetained(CGImageDestinationCreateWithDataConsumer)
        c = CGImageDestinationCreateWithDataConsumer(cons, 'public.tiff', 1, None)
        self.failUnlessIsInstance(c, CGImageDestinationRef)

if __name__ == "__main__":
    main()
