from PyObjCTools.TestSupport import TestCase, min_sdk_level
import BackgroundAssets  # noqa: F401


class TestBAManagedAssetPackDownloadDelegate(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("BAManagedAssetPackDownloadDelegate")
