from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMTreeWalker(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMTreeWalker.expandEntityReferences)
