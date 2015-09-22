from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str


class TestWKWebsiteDataStore (TestCase):
    @onlyOn64Bit
    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(WKWebsiteDataStore.isPersistent)

        self.assertResultIsBOOL(WKWebsiteDataStore.fetchDataRecordsOfTypes_completionHandler_, 1, b'v@')
        self.assertResultIsBOOL(WKWebsiteDataStore.removeDataOfTypes_forDataRecords_completionHandler_, 2, b'v')
        self.assertResultIsBOOL(WKWebsiteDataStore.removeDataOfTypes_modifiedSince_completionHandler_, 2, b'v')

if __name__ == "__main__":
    main()
