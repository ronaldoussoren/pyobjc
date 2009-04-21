
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLFrameElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLFrameElement.noResize)
        self.failUnlessArgIsBOOL(DOMHTMLFrameElement.setNoResize_, 0)

if __name__ == "__main__":
    main()
