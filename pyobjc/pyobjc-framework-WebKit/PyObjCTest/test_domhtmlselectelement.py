
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLSelectElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLSelectElement.setDisabled_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.multiple)
        self.failUnlessArgIsBOOL(DOMHTMLSelectElement.setMultiple_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.willValidate)
        self.failUnlessResultIsBOOL(DOMHTMLSelectElement.autofocus)
        self.failUnlessArgIsBOOL(DOMHTMLSelectElement.setAutofocus_, 0)

if __name__ == "__main__":
    main()
