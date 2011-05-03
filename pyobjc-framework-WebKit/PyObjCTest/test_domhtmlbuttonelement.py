
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLButtonElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLButtonElement.disabled)
        self.assertArgIsBOOL(DOMHTMLButtonElement.setDisabled_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMHTMLButtonElement.willValidate)
        self.assertResultIsBOOL(DOMHTMLButtonElement.autofocus)


if __name__ == "__main__":
    main()
