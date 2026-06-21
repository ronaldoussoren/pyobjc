from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMAttr(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMAttr.specified)
