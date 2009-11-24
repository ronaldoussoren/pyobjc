
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Foundation import NSData

class TestCGDataProvider (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGDataProviderRef) 

    def testFunctions(self):
        provider = CGDataProviderCreateWithCFData(buffer("data"))
        self.failUnlessIsInstance(provider, CGDataProviderRef)

        url = CFURLCreateWithFileSystemPath(None,
                "/Library/Documentation/Acknowledgements.rtf", 
                kCFURLPOSIXPathStyle, False)

        provider = CGDataProviderCreateWithURL(url)
        self.failUnlessIsInstance(provider, CGDataProviderRef)

        v = CGDataProviderRetain(provider)
        self.failUnless(v is provider)
        CGDataProviderRelease(provider)

        data = CGDataProviderCopyData(provider)
        self.failUnlessIsInstance(data, CFDataRef)

        info = ["hello world", False]
        def release(info):
            info[-1] = True
        provider = CGDataProviderCreateWithData(info, info[0], len(info[0]), release)
        self.failUnlessIsInstance(provider, CGDataProviderRef)
        del provider

        self.failUnless(info[-1])



    def testMissing(self):
        self.fail("CGDataProviderCreateSequential") # + callbacks
        self.fail("CGDataProviderCreateDirect") # + callbacks
        self.fail("CGDataProviderCreate") # + callbacks
        self.fail("CGDataProviderCreateDirectAccess") # + callbacks

if __name__ == "__main__":
    main()
