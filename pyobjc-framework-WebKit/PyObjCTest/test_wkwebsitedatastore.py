from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebsiteDataStore(TestCase):
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(WebKit.WKWebsiteDataStore.isPersistent)

        self.assertArgIsBlock(
            WebKit.WKWebsiteDataStore.fetchDataRecordsOfTypes_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            WebKit.WKWebsiteDataStore.removeDataOfTypes_forDataRecords_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            WebKit.WKWebsiteDataStore.removeDataOfTypes_modifiedSince_completionHandler_,
            2,
            b"v",
        )
