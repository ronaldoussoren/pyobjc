
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebFrameView (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(WebFrameView.setAllowsScrolling_, 0)
        self.failUnlessResultIsBOOL(WebFrameView.allowsScrolling)
        self.failUnlessResultIsBOOL(WebFrameView.canPrintHeadersAndFooters)
        self.failUnlessResultIsBOOL(WebFrameView.documentViewShouldHandlePrint)

if __name__ == "__main__":
    main()
