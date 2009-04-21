
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLOListElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLOListElement.compact)
        self.failUnlessArgIsBOOL(DOMHTMLOListElement.setCompact_, 0)

if __name__ == "__main__":
    main()
