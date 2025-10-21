from PyObjCTools.TestSupport import TestCase, min_sdk_level
import BackgroundAssets


class TestBAManagedDownloaderExtensionHelper(BackgroundAssets.NSObject):
    def shouldDownloadAssetPack_(self, a):
        return 1


class TestBAManagedDownloaderExtension(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("BAManagedDownloaderExtension")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestBAManagedDownloaderExtensionHelper.shouldDownloadAssetPack_
        )
