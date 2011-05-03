
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLStyleElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLStyleElement.disabled)
        self.assertArgIsBOOL(DOMHTMLStyleElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
