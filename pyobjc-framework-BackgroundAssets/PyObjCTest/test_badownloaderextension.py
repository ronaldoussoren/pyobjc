from PyObjCTools.TestSupport import TestCase
import BackgroundAssets
import objc


class TestBADownloaderExtensionHelper(BackgroundAssets.NSObject):
    def backgroundDownload_didReceiveChallenge_completionHandler_(self, a, b, c):
        pass


class TestBADownloaderExtension(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BAContentRequest)
        self.assertEqual(BackgroundAssets.BAContentRequestInstall, 1)
        self.assertEqual(BackgroundAssets.BAContentRequestUpdate, 2)
        self.assertEqual(BackgroundAssets.BAContentRequestPeriodic, 3)

    def test_protocols(self):
        self.assertProtocolExists("BADownloaderExtension")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestBADownloaderExtensionHelper.backgroundDownload_didReceiveChallenge_completionHandler_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )
