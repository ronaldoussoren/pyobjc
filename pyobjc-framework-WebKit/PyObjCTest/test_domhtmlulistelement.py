
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLUListElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLUListElement.compact)
        self.failUnlessArgIsBOOL(DOMHTMLUListElement.setCompact_, 0)


if __name__ == "__main__":
    main()
