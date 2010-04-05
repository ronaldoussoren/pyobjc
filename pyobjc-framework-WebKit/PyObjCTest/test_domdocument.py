
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMDocument (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(DOMDocument.getMatchedCSSRules_pseudoElement_authorOnly_, 2)
        self.assertArgIsBOOL(DOMDocument.importNode__, 1)

        self.assertArgIsBOOL(DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_, 3)
        self.assertArgIsBOOL(DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_, 3)
        self.assertArgIsBOOL(DOMDocument.createNodeIterator____, 3)
        self.assertArgIsBOOL(DOMDocument.createTreeWalker____, 3)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMDocument.xmlStandalone)
        self.assertArgIsBOOL(DOMDocument.setXmlStandalone_, 0)

        self.assertArgIsBOOL(DOMDocument.importNode_deep_, 1)
        self.assertArgIsBOOL(DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_, 3)
        self.assertArgIsBOOL(DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_, 3)

        self.assertResultIsBOOL(DOMDocument.execCommand_userInterface_value_)
        self.assertArgIsBOOL(DOMDocument.execCommand_userInterface_value_, 1)
        self.assertResultIsBOOL(DOMDocument.execCommand_userInterface_)
        self.assertArgIsBOOL(DOMDocument.execCommand_userInterface_, 1)
        self.assertResultIsBOOL(DOMDocument.execCommand_)
        self.assertResultIsBOOL(DOMDocument.queryCommandEnabled_)
        self.assertResultIsBOOL(DOMDocument.queryCommandIndeterm_)
        self.assertResultIsBOOL(DOMDocument.queryCommandState_)
        self.assertResultIsBOOL(DOMDocument.queryCommandSupported_)


if __name__ == "__main__":
    main()
