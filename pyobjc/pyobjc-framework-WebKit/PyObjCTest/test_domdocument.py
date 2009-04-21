
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMDocument (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(DOMDocument.getMatchedCSSRules_pseudoElement_authorOnly_, 2)
        self.failUnlessArgIsBOOL(DOMDocument.importNode__, 1)

        self.failUnlessArgIsBOOL(DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createNodeIterator____, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createTreeWalker____, 3)


if __name__ == "__main__":
    main()
