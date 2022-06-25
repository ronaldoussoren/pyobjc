from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit
import objc


class TestWKDownloadDelegateHelper(WebKit.NSObject):
    def download_decideDestinationUsingResponse_suggestedFilename_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def download_willPerformHTTPRedirection_newRequest_decisionHandler_(
        self, a, b, c, d
    ):
        pass

    def download_didReceiveAuthenticationChallenge_completionHandler_(self, a, b, c):
        pass


class TestWKDownloadDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKDownloadRedirectPolicy)

    def test_constants(self):
        self.assertEqual(WebKit.WKDownloadRedirectPolicyCancel, 0)
        self.assertEqual(WebKit.WKDownloadRedirectPolicyAllow, 1)

    @min_sdk_level("11.3")
    def test_protocols(self):
        self.assertProtocolExists("WKDownloadDelegate")

    @min_sdk_level("11.3")
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
