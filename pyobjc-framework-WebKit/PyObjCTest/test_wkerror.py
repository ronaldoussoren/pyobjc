from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKError (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(WKErrorDomain, unicode)

        self.assertEqual(WKErrorUnknown, 1)
        self.assertEqual(WKErrorWebContentProcessTerminated, 2)
        self.assertEqual(WKErrorWebViewInvalidated, 3)
        self.assertEqual(WKErrorJavaScriptExceptionOccurred, 4)
        self.assertEqual(WKErrorJavaScriptResultTypeIsUnsupported, 5)
        self.assertEqual(WKErrorContentRuleListStoreCompileFailed, 6)
        self.assertEqual(WKErrorContentRuleListStoreLookUpFailed, 7)
        self.assertEqual(WKErrorContentRuleListStoreRemoveFailed, 8)
        self.assertEqual(WKErrorContentRuleListStoreVersionMismatch, 9)


if __name__ == "__main__":
    main()
