from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKWebsiteDataRecord (TestCase):
    @onlyOn64Bit
    @min_os_level('10.11')
    def testConstants10_10(self):
        self.assertIsInstance(WKWebsiteDataTypeDiskCache, unicode)
        self.assertIsInstance(WKWebsiteDataTypeMemoryCache, unicode)
        self.assertIsInstance(WKWebsiteDataTypeOfflineWebApplicationCache, unicode)
        self.assertIsInstance(WKWebsiteDataTypeCookies, unicode)
        self.assertIsInstance(WKWebsiteDataTypeSessionStorage, unicode)
        self.assertIsInstance(WKWebsiteDataTypeLocalStorage, unicode)
        self.assertIsInstance(WKWebsiteDataTypeWebSQLDatabases, unicode)
        self.assertIsInstance(WKWebsiteDataTypeIndexedDBDatabases, unicode)

    @onlyOn64Bit
    @min_os_level('10.13.4')
    def testConstants10_13_4(self):
        self.assertIsInstance(WKWebsiteDataTypeFetchCache, unicode)
        self.assertIsInstance(WKWebsiteDataTypeServiceWorkerRegistrations, unicode)

if __name__ == "__main__":
    main()
