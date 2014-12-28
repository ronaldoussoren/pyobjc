
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLTextAreaElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.disabled)
        self.assertArgIsBOOL(DOMHTMLTextAreaElement.setDisabled_, 0)
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.readOnly)
        self.assertArgIsBOOL(DOMHTMLTextAreaElement.setReadOnly_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.autofocus)
        self.assertArgIsBOOL(DOMHTMLTextAreaElement.setAutofocus_, 0)
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.willValidate)

if __name__ == "__main__":
    main()
