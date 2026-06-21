from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLTableCellElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTableCellElement.noWrap)
        self.assertArgIsBOOL(WebKit.DOMHTMLTableCellElement.setNoWrap_, 0)
