from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLDownloadHelper (NSObject):
    def download_willResumeWithResponse_fromByte_(self, a, b, c): pass
    def download_didReceiveDataOfLength_(self, a, b): pass
    def download_shouldDecodeSourceDataOfMIMEType_(self, a, b): return 1


class TestNSURLDownload (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLDownload.canResumeDownloadDecodedWithEncodingMIMEType_)
        self.failUnlessArgIsBOOL(NSURLDownload.setDestination_allowOverwrite_, 1)
        self.failUnlessArgIsBOOL(NSURLDownload.setDeletesFileUponFailure_, 0)
        self.failUnlessResultIsBOOL(NSURLDownload.deletesFileUponFailure)


    def testProtocols(self):
        self.failUnlessArgHasType(TestNSURLDownloadHelper.download_willResumeWithResponse_fromByte_, 2, objc._C_LNG_LNG)
        self.failUnlessArgHasType(TestNSURLDownloadHelper.download_didReceiveDataOfLength_, 1, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSURLDownloadHelper.download_shouldDecodeSourceDataOfMIMEType_)

if __name__ == "__main__":
    main()
