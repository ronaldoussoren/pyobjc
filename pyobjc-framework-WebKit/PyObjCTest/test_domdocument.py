from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMDocument(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            WebKit.DOMDocument.getMatchedCSSRules_pseudoElement_authorOnly_, 2
        )
        self.assertArgIsBOOL(WebKit.DOMDocument.importNode__, 1)

        self.assertArgIsBOOL(
            WebKit.DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_,
            3,
        )
        self.assertArgIsBOOL(
            WebKit.DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_,
            3,
        )
        self.assertArgIsBOOL(WebKit.DOMDocument.createNodeIterator____, 3)
        self.assertArgIsBOOL(WebKit.DOMDocument.createTreeWalker____, 3)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMDocument.xmlStandalone)
        self.assertArgIsBOOL(WebKit.DOMDocument.setXmlStandalone_, 0)

        self.assertArgIsBOOL(WebKit.DOMDocument.importNode_deep_, 1)
        self.assertArgIsBOOL(
            WebKit.DOMDocument.createNodeIterator_whatToShow_filter_expandEntityReferences_,
            3,
        )
        self.assertArgIsBOOL(
            WebKit.DOMDocument.createTreeWalker_whatToShow_filter_expandEntityReferences_,
            3,
        )

        self.assertResultIsBOOL(WebKit.DOMDocument.execCommand_userInterface_value_)
        self.assertArgIsBOOL(WebKit.DOMDocument.execCommand_userInterface_value_, 1)
        self.assertResultIsBOOL(WebKit.DOMDocument.execCommand_userInterface_)
        self.assertArgIsBOOL(WebKit.DOMDocument.execCommand_userInterface_, 1)
        self.assertResultIsBOOL(WebKit.DOMDocument.execCommand_)
        self.assertResultIsBOOL(WebKit.DOMDocument.queryCommandEnabled_)
        self.assertResultIsBOOL(WebKit.DOMDocument.queryCommandIndeterm_)
        self.assertResultIsBOOL(WebKit.DOMDocument.queryCommandState_)
        self.assertResultIsBOOL(WebKit.DOMDocument.queryCommandSupported_)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.DOMDocument.hasFocus)
