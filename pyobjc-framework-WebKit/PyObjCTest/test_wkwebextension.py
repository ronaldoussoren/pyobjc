from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionDataRecord(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionDataRecordError)
        self.assertEqual(WebKit.WKWebExtensionDataRecordErrorUnknown, 1)
        self.assertEqual(WebKit.WKWebExtensionDataRecordErrorLocalStorageFailed, 2)
        self.assertEqual(WebKit.WKWebExtensionDataRecordErrorSessionStorageFailed, 3)
        self.assertEqual(
            WebKit.WKWebExtensionDataRecordErrorSynchronizedStorageFailed, 4
        )

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionDataRecordErrorDomain, str)
