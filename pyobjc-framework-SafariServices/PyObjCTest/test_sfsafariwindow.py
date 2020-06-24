from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariWindow(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariWindow.getActiveTabWithCompletionHandler_, 0, b"v@"
        )

        self.assertArgIsBOOL(
            SafariServices.SFSafariWindow.openTabWithURL_makeActiveIfPossible_completionHandler_,
            1,
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariWindow.openTabWithURL_makeActiveIfPossible_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            SafariServices.SFSafariWindow.getToolbarItemWithCompletionHandler_, 0, b"v@"
        )

    @min_os_level("10.14.4")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariWindow.getAllTabsWithCompletionHandler_, 0, b"v@"
        )
