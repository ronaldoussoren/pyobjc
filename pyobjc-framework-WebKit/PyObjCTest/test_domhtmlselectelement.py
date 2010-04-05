
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLSelectElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLSelectElement.disabled)
        self.assertArgIsBOOL(DOMHTMLSelectElement.setDisabled_, 0)
        self.assertResultIsBOOL(DOMHTMLSelectElement.multiple)
        self.assertArgIsBOOL(DOMHTMLSelectElement.setMultiple_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMHTMLSelectElement.willValidate)
        self.assertResultIsBOOL(DOMHTMLSelectElement.autofocus)
        self.assertArgIsBOOL(DOMHTMLSelectElement.setAutofocus_, 0)

if __name__ == "__main__":
    main()
