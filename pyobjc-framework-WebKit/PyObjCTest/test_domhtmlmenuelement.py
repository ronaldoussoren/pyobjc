
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLMenuElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLMenuElement.compact)
        self.failUnlessArgIsBOOL(DOMHTMLMenuElement.setCompact_, 0)

if __name__ == "__main__":
    main()
