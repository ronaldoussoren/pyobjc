
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLOptGroupElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLOptGroupElement.disabled)
        self.assertArgIsBOOL(DOMHTMLOptGroupElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
