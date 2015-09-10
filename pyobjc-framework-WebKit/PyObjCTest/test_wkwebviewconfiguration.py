from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKWebViewConfiguration (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKWebViewConfiguration.suppressesIncrementalRendering)
        self.assertArgIsBOOL(WKWebViewConfiguration.setSuppressesIncrementalRendering_, 0)


if __name__ == "__main__":
    main()
