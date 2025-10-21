from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebsiteDataRecord(TestCase):
    @min_os_level("10.11")
    def testConstants10_10(self):
        self.assertIsInstance(WebKit.WKWebsiteDataTypeDiskCache, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeMemoryCache, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeOfflineWebApplicationCache, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeCookies, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeSessionStorage, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeLocalStorage, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeWebSQLDatabases, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeIndexedDBDatabases, str)

    @min_os_level("10.13.4")
    def testConstants10_13_4(self):
        self.assertIsInstance(WebKit.WKWebsiteDataTypeFetchCache, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeServiceWorkerRegistrations, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertIsInstance(WebKit.WKWebsiteDataTypeFileSystem, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(WebKit.WKWebsiteDataTypeSearchFieldRecentSearches, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeMediaKeys, str)
        self.assertIsInstance(WebKit.WKWebsiteDataTypeHashSalt, str)

    @min_os_level("26.0")
    def testConstants26_0(self):
        self.assertIsInstance(WebKit.WKWebsiteDataTypeScreenTime, str)
