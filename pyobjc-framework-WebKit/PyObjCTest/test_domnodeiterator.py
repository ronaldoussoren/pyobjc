from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMNodeIterator(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMNodeIterator.expandEntityReferences)

        self.assertResultIsBOOL(WebKit.DOMNodeIterator.pointerBeforeReferenceNode)
