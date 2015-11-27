from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKFrameInfo (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKFrameInfo.isMainFrame)

if __name__ == "__main__":
    main()
