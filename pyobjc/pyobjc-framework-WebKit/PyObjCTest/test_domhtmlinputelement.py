
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLInputElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLInputElement.defaultChecked)
        self.assertArgIsBOOL(DOMHTMLInputElement.setDefaultChecked_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.checked)
        self.assertArgIsBOOL(DOMHTMLInputElement.setChecked_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.disabled)
        self.assertArgIsBOOL(DOMHTMLInputElement.setDisabled_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.readOnly)
        self.assertArgIsBOOL(DOMHTMLInputElement.setReadOnly_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMHTMLInputElement.autofocus)
        self.assertArgIsBOOL(DOMHTMLInputElement.setAutofocus_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.multiple)
        self.assertArgIsBOOL(DOMHTMLInputElement.setMultiple_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.indeterminate)
        self.assertArgIsBOOL(DOMHTMLInputElement.setIndeterminate_, 0)
        self.assertResultIsBOOL(DOMHTMLInputElement.willValidate)

if __name__ == "__main__":
    main()
