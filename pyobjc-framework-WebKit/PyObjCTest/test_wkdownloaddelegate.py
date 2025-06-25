from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit
import objc


class TestWKDownloadDelegateHelper(WebKit.NSObject):
    def download_decideDestinationUsingResponse_suggestedFilename_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def download_willPerformHTTPRedirection_newRequest_decisionHandler_(self, a, b, c, d):
        pass

    def download_didReceiveAuthenticationChallenge_completionHandler_(self, a, b, c):
        pass

    def download_decidePlaceholderPolicy_(self, a, b):
        pass

    def download_didReceivePlaceholderURL_completionHandler_(self, a, b, c):
        pass


class TestWKDownloadDelegate(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKDownloadRedirectPolicy)
        self.assertEqual(WebKit.WKDownloadRedirectPolicyCancel, 0)
        self.assertEqual(WebKit.WKDownloadRedirectPolicyAllow, 1)

        self.assertIsEnumType(WebKit.WKDownloadPlaceholderPolicy)
        self.assertEqual(WebKit.WKDownloadPlaceholderPolicyDisable, 0)
        self.assertEqual(WebKit.WKDownloadPlaceholderPolicyEnable, 1)

    @min_sdk_level("11.3")
    def test_protocols(self):
        self.assertProtocolExists("WKDownloadDelegate")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestWKDownloadDelegateHelper.download_decideDestinationUsingResponse_suggestedFilename_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKDownloadDelegateHelper.download_willPerformHTTPRedirection_newRequest_decisionHandler_,
            3,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestWKDownloadDelegateHelper.download_didReceiveAuthenticationChallenge_completionHandler_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )

        self.assertArgIsBlock(
            TestWKDownloadDelegateHelper.download_decidePlaceholderPolicy_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )

        self.assertArgIsBlock(
            TestWKDownloadDelegateHelper.download_didReceivePlaceholderURL_completionHandler_,
            2,
            b"v",
        )
