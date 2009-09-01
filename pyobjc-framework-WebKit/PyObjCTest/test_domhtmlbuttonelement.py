
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLButtonElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLButtonElement.disabled)
        self.failUnlessArgIsBOOL(DOMHTMLButtonElement.setDisabled_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(DOMHTMLButtonElement.willValidate)
        self.failUnlessResultIsBOOL(DOMHTMLButtonElement.autofocus)


if __name__ == "__main__":
    main()
