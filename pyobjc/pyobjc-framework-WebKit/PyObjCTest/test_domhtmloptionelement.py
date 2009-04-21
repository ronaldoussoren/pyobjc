
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLOptionElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLOptionElement.defaultSelected)
        self.failUnlessArgIsBOOL(DOMHTMLOptionElement.setDefaultSelected_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLOptionElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLOptionElement.setDisabled_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLOptionElement.selected)
        self.failUnlessArgIsBOOL(DOMHTMLOptionElement.setSelected_, 0)

if __name__ == "__main__":
    main()
