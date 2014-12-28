from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str


class TestWKFrameInfo (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKFrameInfo.isMainFrame)

if __name__ == "__main__":
    main()
