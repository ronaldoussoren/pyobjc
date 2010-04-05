
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLDirectoryElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLDirectoryElement.compact)
        self.assertArgIsBOOL(DOMHTMLDirectoryElement.setCompact_, 0)


if __name__ == "__main__":
    main()
