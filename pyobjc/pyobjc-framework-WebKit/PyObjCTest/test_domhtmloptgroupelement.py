
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLOptGroupElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLOptGroupElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLOptGroupElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
