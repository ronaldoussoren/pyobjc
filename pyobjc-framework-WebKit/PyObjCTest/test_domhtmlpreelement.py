from PyObjCTools.TestSupport import *
from WebKit import *


class TestDOMHTMLPreElement(TestCase):
    @min_os_level("10.6")
    def testMehods10_6(self):
        self.assertResultIsBOOL(DOMHTMLPreElement.wrap)
        self.assertArgIsBOOL(DOMHTMLPreElement.setWrap_, 0)


if __name__ == "__main__":
    main()
