from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLDownloadHelper (NSObject):
    def download_willResumeWithResponse_fromByte_(self, a, b, c): pass
    def download_didReceiveDataOfLength_(self, a, b): pass
    def download_shouldDecodeSourceDataOfMIMEType_(self, a, b): return 1
    def download_canAuthenticateAgainstProtectionSpace_(self, a, b): return 1
    def downloadShouldUseCredentialStorage_(self, a): return 1
    def download_willResumeWithResponse_fromByte_(self, a, b ,c): pass


class TestNSURLDownload (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSURLDownload.canResumeDownloadDecodedWithEncodingMIMEType_)
        self.assertArgIsBOOL(NSURLDownload.setDestination_allowOverwrite_, 1)
        self.assertArgIsBOOL(NSURLDownload.setDeletesFileUponFailure_, 0)
        self.assertResultIsBOOL(NSURLDownload.deletesFileUponFailure)


    def testProtocols(self):
        self.assertArgHasType(TestNSURLDownloadHelper.download_willResumeWithResponse_fromByte_, 2, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLDownloadHelper.download_didReceiveDataOfLength_, 1, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSURLDownloadHelper.download_shouldDecodeSourceDataOfMIMEType_)
        self.assertResultIsBOOL(TestNSURLDownloadHelper.download_canAuthenticateAgainstProtectionSpace_)
        self.assertResultIsBOOL(TestNSURLDownloadHelper.downloadShouldUseCredentialStorage_)
        self.assertArgHasType(TestNSURLDownloadHelper.download_willResumeWithResponse_fromByte_,
                2, objc._C_LNG_LNG)

if __name__ == "__main__":
    main()
