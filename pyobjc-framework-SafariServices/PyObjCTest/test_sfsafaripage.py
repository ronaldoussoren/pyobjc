from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariPage(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariPage.getPagePropertiesWithCompletionHandler_,
            0,
            b"v@",
        )

    @min_os_level("10.14.4")
    def test_methods10_14(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariPage.getContainingTabWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariPage.getScreenshotOfVisibleAreaWithCompletionHandler_,
            0,
            b"v@",
        )
