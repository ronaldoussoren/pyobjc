from PyObjCTools.TestSupport import TestCase
import BackgroundAssets
import objc


class TestBADownloaderExtensionHelper(BackgroundAssets.NSObject):
    def receivedAuthenticationChallenge_download_completionHandler_(self, a, b, c):
        pass


class TestBADownloaderExtension(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BADownloaderExtension")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestBADownloaderExtensionHelper.receivedAuthenticationChallenge_download_completionHandler_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )
