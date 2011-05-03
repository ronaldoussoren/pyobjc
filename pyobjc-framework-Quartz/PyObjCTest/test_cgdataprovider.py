
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Foundation import NSData

import sys

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')

class TestCGDataProvider (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGDataProviderRef) 

    def testFunctions(self):
        provider = CGDataProviderCreateWithCFData(buffer("data"))
        self.assertIsInstance(provider, CGDataProviderRef)

        url = CFURLCreateWithFileSystemPath(None,
                "/Library/Documentation/Acknowledgements.rtf", 
                kCFURLPOSIXPathStyle, False)

        provider = CGDataProviderCreateWithURL(url)
        self.assertIsInstance(provider, CGDataProviderRef)

        v = CGDataProviderRetain(provider)
        self.assertTrue(v is provider)
        CGDataProviderRelease(provider)

        data = CGDataProviderCopyData(provider)
        self.assertIsInstance(data, CFDataRef)

        info = [b"hello world", False]
        def release(info):
            info[-1] = True
        provider = CGDataProviderCreateWithData(info, info[0], len(info[0]), release)
        self.assertIsInstance(provider, CGDataProviderRef)
        del provider

        self.assertTrue(info[-1])



    def testMissing(self):
        self.fail("CGDataProviderCreateSequential") # + callbacks
        self.fail("CGDataProviderCreateDirect") # + callbacks
        self.fail("CGDataProviderCreate") # + callbacks
        self.fail("CGDataProviderCreateDirectAccess") # + callbacks

if __name__ == "__main__":
    main()
