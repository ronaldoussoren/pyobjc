from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKErrorCode)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(WebKit.WKErrorDomain, str)

        self.assertEqual(WebKit.WKErrorUnknown, 1)
        self.assertEqual(WebKit.WKErrorWebContentProcessTerminated, 2)
        self.assertEqual(WebKit.WKErrorWebViewInvalidated, 3)
        self.assertEqual(WebKit.WKErrorJavaScriptExceptionOccurred, 4)
        self.assertEqual(WebKit.WKErrorJavaScriptResultTypeIsUnsupported, 5)
        self.assertEqual(WebKit.WKErrorContentRuleListStoreCompileFailed, 6)
        self.assertEqual(WebKit.WKErrorContentRuleListStoreLookUpFailed, 7)
        self.assertEqual(WebKit.WKErrorContentRuleListStoreRemoveFailed, 8)
        self.assertEqual(WebKit.WKErrorContentRuleListStoreVersionMismatch, 9)
        self.assertEqual(WebKit.WKErrorAttributedStringContentFailedToLoad, 10)
        self.assertEqual(WebKit.WKErrorAttributedStringContentLoadTimedOut, 11)
        self.assertEqual(WebKit.WKErrorJavaScriptInvalidFrameTarget, 12)
        self.assertEqual(WebKit.WKErrorNavigationAppBoundDomain, 13)
        self.assertEqual(WebKit.WKErrorJavaScriptAppBoundDomain, 14)
        self.assertEqual(WebKit.WKErrorDuplicateCredential, 15)
        self.assertEqual(WebKit.WKErrorMalformedCredential, 16)
        self.assertEqual(WebKit.WKErrorCredentialNotFound, 17)
