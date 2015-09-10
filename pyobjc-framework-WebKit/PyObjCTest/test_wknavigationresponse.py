from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKNavigationResponse (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKNavigationResponse.isForMainFrame)
        self.assertResultIsBOOL(WKNavigationResponse.canShowMIMEType)

if __name__ == "__main__":
    main()
