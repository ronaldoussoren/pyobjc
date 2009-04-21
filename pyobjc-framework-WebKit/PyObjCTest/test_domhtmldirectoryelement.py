
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLDirectoryElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLDirectoryElement.compact)
        self.failUnlessArgIsBOOL(DOMHTMLDirectoryElement.setCompact_, 0)


if __name__ == "__main__":
    main()
