
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMTraversal (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createNodeIterator____, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createTreeWalker____, 3)


if __name__ == "__main__":
    main()
