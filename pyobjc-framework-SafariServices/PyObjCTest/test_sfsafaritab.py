from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariTab(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariTab.getActivePageWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariTab.getPagesWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariTab.activateWithCompletionHandler_, 0, b"v"
        )

    @min_os_level("10.14.4")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariTab.getContainingWindowWithCompletionHandler_,
            0,
            b"v",
        )
