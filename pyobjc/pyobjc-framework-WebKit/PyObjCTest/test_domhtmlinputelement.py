
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

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.autofocus)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setAutofocus_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.multiple)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setMultiple_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.indeterminate)
        self.failUnlessArgIsBOOL(DOMHTMLInputElement.setIndeterminate_, 0)
        self.failUnlessResultIsBOOL(DOMHTMLInputElement.willValidate)

if __name__ == "__main__":
    main()
