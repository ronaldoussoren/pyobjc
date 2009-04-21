
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLInputElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.defaultChecked)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setDefaultChecked_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.checked)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setChecked_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setDisabled_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.readOnly)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setReadOnly_, 0)

if __name__ == "__main__":
    main()
