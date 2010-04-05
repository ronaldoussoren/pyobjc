
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLLinkElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLLinkElement.disabled)
        self.assertArgIsBOOL(DOMHTMLLinkElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
