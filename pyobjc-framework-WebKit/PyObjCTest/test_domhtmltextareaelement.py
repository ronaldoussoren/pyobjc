
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLTextAreaElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLTextAreaElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLTextAreaElement.setDisabled_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLTextAreaElement.readOnly)
        self.failUnlessArgIsBOOL(DOMHTMLTextAreaElement.setReadOnly_, 0)

if __name__ == "__main__":
    main()
