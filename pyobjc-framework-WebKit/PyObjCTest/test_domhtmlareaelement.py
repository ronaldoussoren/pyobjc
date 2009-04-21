from WebKit import *
from PyObjCTools.TestSupport import *


class TestDOMHTMLAreaElement (TestCase):
    def testMehods(self):
        self.failUnlessResultIsBOOL(DOMHTMLAreaElement.noHref)
        self.failUnlessArgIsBOOL(DOMHTMLAreaElement.setNoHref_, 0)

if __name__ == "__main__":
    main()
