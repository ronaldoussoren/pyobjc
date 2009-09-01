from WebKit import *
from PyObjCTools.TestSupport import *


class TestDOMHTMLPreElement (TestCase):

    @min_os_level('10.6')
    def testMehods10_6(self):
        self.failUnlessResultIsBOOL(DOMHTMLPreElement.wrap)
        self.failUnlessArgIsBOOL(DOMHTMLPreElement.setWrap_, 0)

if __name__ == "__main__":
    main()
