
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLImageElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLImageElement.isMap)
        self.assertArgIsBOOL(DOMHTMLImageElement.setIsMap_, 0)

        self.assertResultIsBOOL(DOMHTMLImageElement.complete)

if __name__ == "__main__":
    main()
