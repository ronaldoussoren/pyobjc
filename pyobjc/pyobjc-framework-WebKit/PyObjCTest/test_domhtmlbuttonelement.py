
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLButtonElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLButtonElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLButtonElement.setDisabled_, 0)

if __name__ == "__main__":
    main()
