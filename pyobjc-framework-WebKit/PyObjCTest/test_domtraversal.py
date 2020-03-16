from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMTraversal(TestCase):
    def testMethods(self):
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
