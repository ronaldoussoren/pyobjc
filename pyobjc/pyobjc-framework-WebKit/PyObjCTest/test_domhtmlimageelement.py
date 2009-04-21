
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLImageElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLImageElement.isMap)
        self.failUnlessArgIsBOOL(DOMHTMLImageElement.setIsMap_, 0)

if __name__ == "__main__":
    main()
