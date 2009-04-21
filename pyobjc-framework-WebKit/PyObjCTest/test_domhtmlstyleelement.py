
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLStyleElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLStyleElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLStyleElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
