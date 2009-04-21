
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLLinkElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLLinkElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLLinkElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
