from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets
import objc


class TestBADownloaderHelper(BackgroundAssets.NSObject):
    def download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_(
        self, a, b, c, d
    ):
        pass

    def download_didReceiveChallenge_completionHandler_(self, a, b, c):
        pass


class TestBADownloadManager(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BADownloadManagerDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            1,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            3,
            objc._C_LNG_LNG,
        )

        self.assertArgIsBlock(
            TestBADownloaderHelper.download_didReceiveChallenge_completionHandler_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )

    def test_methods(self):
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.fetchCurrentDownloadsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsOut(
            BackgroundAssets.BADownloadManager.scheduleDownload_error_, 1
        )
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.performWithExclusiveControl_, 0, b"vZ@"
        )
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.performWithExclusiveControlBeforeDate_performHandler_,
            1,
            b"vZ@",
        )

        self.assertResultIsBOOL(
            BackgroundAssets.BADownloadManager.startForegroundDownload_error_
        )
        self.assertArgIsOut(
            BackgroundAssets.BADownloadManager.startForegroundDownload_error_, 1
        )

        self.assertResultIsBOOL(
            BackgroundAssets.BADownloadManager.cancelDownload_error_
        )
        self.assertArgIsOut(BackgroundAssets.BADownloadManager.cancelDownload_error_, 1)

    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertArgIsOut(
            BackgroundAssets.BADownloadManager.fetchCurrentDownloads_, 0
        )
