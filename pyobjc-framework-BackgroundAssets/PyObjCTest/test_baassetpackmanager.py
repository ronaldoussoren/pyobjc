from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAAssetPackManager(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            BackgroundAssets.BAAssetPackManager.getAllAssetPacksWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            BackgroundAssets.BAAssetPackManager.getAssetPackWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            BackgroundAssets.BAAssetPackManager.getStatusOfAssetPackWithIdentifier_completionHandler_,
            1,
            b"vQ@",
        )
        self.assertArgIsBlock(
            BackgroundAssets.BAAssetPackManager.ensureLocalAvailabilityOfAssetPack_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            BackgroundAssets.BAAssetPackManager.checkForUpdatesWithCompletionHandler_,
            0,
            b"v@@@",
        )
        self.assertArgIsOut(
            BackgroundAssets.BAAssetPackManager.contentsAtPath_searchingInAssetPackWithIdentifier_options_error_,
            3,
        )
        self.assertArgIsOut(
            BackgroundAssets.BAAssetPackManager.fileDescriptorForPath_searchingInAssetPackWithIdentifier_error_,
            2,
        )
        self.assertArgIsOut(BackgroundAssets.BAAssetPackManager.URLForPath_error_, 1)
