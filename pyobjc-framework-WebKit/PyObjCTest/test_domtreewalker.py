from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMTreeWalker(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMTreeWalker.expandEntityReferences)
