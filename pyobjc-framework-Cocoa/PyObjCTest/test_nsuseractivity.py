import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestNSUserActivity(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Foundation.NSUserActivityTypeBrowsingWeb, str)

    @min_os_level("10.10")
    @expectedFailure  # XXX
    def testConstants10_10_failon1015beta(self):
        self.assertIsInstance(Foundation.NSUserActivityDocumentURLKey, str)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Foundation.NSUserActivity.needsSave)
        self.assertArgIsBOOL(Foundation.NSUserActivity.setNeedsSave_, 0)

        self.assertResultIsBOOL(Foundation.NSUserActivity.supportsContinuationStreams)
        self.assertArgIsBOOL(
            Foundation.NSUserActivity.setSupportsContinuationStreams_, 0
        )

        self.assertArgIsBlock(
            Foundation.NSUserActivity.getContinuationStreamsWithCompletionHandler_,
            0,
            b"v@@@",
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(Foundation.NSUserActivity.isEligibleForHandoff)
        self.assertArgIsBOOL(Foundation.NSUserActivity.setEligibleForHandoff_, 0)

        self.assertResultIsBOOL(Foundation.NSUserActivity.isEligibleForSearch)
        self.assertArgIsBOOL(Foundation.NSUserActivity.setEligibleForSearch_, 0)

        self.assertResultIsBOOL(Foundation.NSUserActivity.isEligibleForPublicIndexing)
        self.assertArgIsBOOL(Foundation.NSUserActivity.setEligibleForPublicIndexing_, 0)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            Foundation.NSUserActivity.deleteSavedUserActivitiesWithPersistentIdentifiers_completionHandler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            Foundation.NSUserActivity.deleteAllSavedUserActivitiesWithCompletionHandler_,
            0,
            b"v",
        )

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("NSUserActivityDelegate")
