
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLTextAreaElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.disabled)
        self.assertArgIsBOOL(DOMHTMLTextAreaElement.setDisabled_, 0)
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.readOnly)
        self.assertArgIsBOOL(DOMHTMLTextAreaElement.setReadOnly_, 0)

if __name__ == "__main__":
    main()
