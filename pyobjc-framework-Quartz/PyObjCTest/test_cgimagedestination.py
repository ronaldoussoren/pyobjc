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
        dest = CGImageDestinationCreateWithURL(url, v[0], 2, None)
        self.failUnlessIsInstance(dest, CGImageDestinationRef)

        CGImageDestinationSetProperties(dest, {u'key': u'value'})

        #img = ...
        CGImageDestinationAddImage(dest, img)

        #isrc = ...
        CGImageDestinationAddImageFromSource(dest,  isrc, 0, None)

        self.failUnlessResultHasType(CGImageDestinationFinalize, objc._C_BOOL)
        v = CGImageDestinationFinalize(dest)
        self.failUnless(v is True)

        self.fail("CGImageDestinationCreateWithDataConsumer")

    def testIncomplete(self):
        self.fail("Add header tests for <ImageIO/CGImageDestination.h>")

if __name__ == "__main__":
    main()
