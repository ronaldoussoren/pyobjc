
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

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(DOMDocument.xmlStandalone)
        self.failUnlessArgIsBOOL(DOMDocument.setXmlStandalone_, 0)

        self.failUnlessArgIsBOOL(DOMDocument.importNode_deep_, 1)
        self.failUnlessArgIsBOOL(DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_, 3)
        self.failUnlessArgIsBOOL(DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_, 3)

        self.failUnlessResultIsBOOL(DOMDocument.execCommand_userInterface_value_)
        self.failUnlessArgIsBOOL(DOMDocument.execCommand_userInterface_value_, 1)
        self.failUnlessResultIsBOOL(DOMDocument.execCommand_userInterface_)
        self.failUnlessArgIsBOOL(DOMDocument.execCommand_userInterface_, 1)
        self.failUnlessResultIsBOOL(DOMDocument.execCommand_)
        self.failUnlessResultIsBOOL(DOMDocument.queryCommandEnabled_)
        self.failUnlessResultIsBOOL(DOMDocument.queryCommandIndeterm_)
        self.failUnlessResultIsBOOL(DOMDocument.queryCommandState_)
        self.failUnlessResultIsBOOL(DOMDocument.queryCommandSupported_)


if __name__ == "__main__":
    main()
