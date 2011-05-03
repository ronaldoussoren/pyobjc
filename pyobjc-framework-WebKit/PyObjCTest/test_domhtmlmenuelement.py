
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLMenuElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLMenuElement.compact)
        self.assertArgIsBOOL(DOMHTMLMenuElement.setCompact_, 0)

if __name__ == "__main__":
    main()
