
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMElement.hasAttribute_)
        self.assertResultIsBOOL(DOMElement.hasAttributeNS_localName_)
        self.assertArgIsBOOL(DOMElement.scrollIntoView_, 0)
        self.assertArgIsBOOL(DOMElement.scrollIntoViewIfNeeded_, 0)
        self.assertResultIsBOOL(DOMElement.hasAttributeNS__)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(DOMElement.contains_)


if __name__ == "__main__":
    main()
