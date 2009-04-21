
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLDListElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLDListElement.compact)
        self.failUnlessArgIsBOOL(DOMHTMLDListElement.setCompact_, 0)

if __name__ == "__main__":
    main()
