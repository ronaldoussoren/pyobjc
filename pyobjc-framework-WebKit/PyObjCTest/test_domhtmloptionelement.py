
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLOptionElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLOptionElement.defaultSelected)
        self.assertArgIsBOOL(DOMHTMLOptionElement.setDefaultSelected_, 0)
        self.assertResultIsBOOL(DOMHTMLOptionElement.disabled)
        self.assertArgIsBOOL(DOMHTMLOptionElement.setDisabled_, 0)
        self.assertResultIsBOOL(DOMHTMLOptionElement.selected)
        self.assertArgIsBOOL(DOMHTMLOptionElement.setSelected_, 0)

if __name__ == "__main__":
    main()
