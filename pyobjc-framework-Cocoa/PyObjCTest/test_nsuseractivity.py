import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSUserActivity(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AppKit.NSUserActivityDocumentURLKey, str)
        self.assertIsInstance(AppKit.NSUserActivityTypeBrowsingWeb, str)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSUserActivity.needsSave)
        self.assertArgIsBOOL(AppKit.NSUserActivity.setNeedsSave_, 0)

        self.assertResultIsBOOL(AppKit.NSUserActivity.supportsContinuationStreams)
        self.assertArgIsBOOL(AppKit.NSUserActivity.setSupportsContinuationStreams_, 0)

        self.assertArgIsBlock(
            AppKit.NSUserActivity.getContinuationStreamsWithCompletionHandler_,
            0,
            b"v@@@",
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSUserActivity.isEligibleForHandoff)
        self.assertArgIsBOOL(AppKit.NSUserActivity.setEligibleForHandoff_, 0)

        self.assertResultIsBOOL(AppKit.NSUserActivity.isEligibleForSearch)
        self.assertArgIsBOOL(AppKit.NSUserActivity.setEligibleForSearch_, 0)

        self.assertResultIsBOOL(AppKit.NSUserActivity.isEligibleForPublicIndexing)
        self.assertArgIsBOOL(AppKit.NSUserActivity.setEligibleForPublicIndexing_, 0)

    @min_os_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("NSUserActivityDelegate")
