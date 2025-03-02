from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionController(TestCase):
    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionController.loadExtensionContext_error_
        )
        self.assertArgIsOut(
            WebKit.WKWebExtensionController.loadExtensionContext_error_, 1
        )

        self.assertResultIsBOOL(
            WebKit.WKWebExtensionController.unloadExtensionContext_error_
        )
        self.assertArgIsOut(
            WebKit.WKWebExtensionController.unloadExtensionContext_error_, 1
        )

        self.assertArgIsBlock(
            WebKit.WKWebExtensionController.fetchDataRecordsOfTypes_completionHander_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            WebKit.WKWebExtensionController.fetchDataRecordOfTypes_forExtensionContext_completionHander_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            WebKit.WKWebExtensionController.removeDataOfTypes_fromDataRecords_completionHandler_,
            2,
            b"v",
        )

        self.assertArgIsBOOL(
            WebKit.WKWebExtensionController.didCloseTab_windowIsClosing_, 1
        )
