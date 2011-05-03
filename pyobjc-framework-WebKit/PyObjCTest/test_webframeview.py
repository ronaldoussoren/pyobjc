
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebFrameView (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(WebFrameView.setAllowsScrolling_, 0)
        self.assertResultIsBOOL(WebFrameView.allowsScrolling)
        self.assertResultIsBOOL(WebFrameView.canPrintHeadersAndFooters)
        self.assertResultIsBOOL(WebFrameView.documentViewShouldHandlePrint)

if __name__ == "__main__":
    main()
