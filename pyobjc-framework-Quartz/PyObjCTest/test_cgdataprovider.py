import os

from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestCGDataProvider(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGDataProviderRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGDataProviderGetTypeID(), int)

        provider = Quartz.CGDataProviderCreateWithCFData(b"data")
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        fn = "/Library/Documentation/Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation/Airport Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"

        if not os.path.exists(fn):
            self.fail("Cannot find test file")

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, fn, Quartz.kCFURLPOSIXPathStyle, False
        )

        provider = Quartz.CGDataProviderCreateWithURL(url)
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        provider = Quartz.CGDataProviderCreateWithFilename(fn.encode("ascii"))
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        v = Quartz.CGDataProviderRetain(provider)
        self.assertTrue(v is provider)
        Quartz.CGDataProviderRelease(provider)

        data = Quartz.CGDataProviderCopyData(provider)
        self.assertIsInstance(data, Quartz.CFDataRef)

        info = [b"hello world", False]

        def release(info):
            info[-1] = True

        provider = Quartz.CGDataProviderCreateWithData(
            info, info[0], len(info[0]), release
        )
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)
        del provider

        self.assertTrue(info[-1])

    @expectedFailure
    def testMissing(self):
        self.fail("CGDataProviderCreateSequential")  # + callbacks
        self.fail("CGDataProviderCreateDirect")  # + callbacks
        self.fail("CGDataProviderCreate")  # + callbacks
        self.fail("CGDataProviderCreateDirectAccess")  # + callbacks

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGDataProviderGetInfo
