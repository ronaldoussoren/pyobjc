from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFContentBlockerManager(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.getActiveWindowWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.openWindowWithURL_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.showPreferencesForExtensionWithIdentifier_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.dispatchMessageWithName_toExtensionWithIdentifier_userInfo_completionHandler_,
            3,
            b"v@",
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.getHostApplicationWithCompletionHandler_,
            0,
            b"v@",
        )

    @min_os_level("10.14.4")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariApplication.getAllWindowsWithCompletionHandler_,
            0,
            b"v@",
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(SafariServices.SFExtensionMessageKey, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(SafariServices.SFExtensionProfileKey, str)
