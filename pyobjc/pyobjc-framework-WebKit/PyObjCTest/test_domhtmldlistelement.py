
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLDListElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLDListElement.compact)
        self.assertArgIsBOOL(DOMHTMLDListElement.setCompact_, 0)

if __name__ == "__main__":
    main()
