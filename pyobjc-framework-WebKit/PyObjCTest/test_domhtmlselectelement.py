
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLSelectElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLSelectElement.setDisabled_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.multiple)
        self.failUnlessArgIsBOOL(DOMHTMLSelectElement.setMultiple_, 0)

if __name__ == "__main__":
    main()
