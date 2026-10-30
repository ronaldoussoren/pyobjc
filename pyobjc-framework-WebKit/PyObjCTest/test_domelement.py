from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMElement(TestCase):
    def test_constants(self):
        self.assertEqual(WebKit.DOM_ALLOW_KEYBOARD_INPUT, 1)

    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttribute_)
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttributeNS_localName_)
        self.assertArgIsBOOL(WebKit.DOMElement.scrollIntoView_, 0)
        self.assertArgIsBOOL(WebKit.DOMElement.scrollIntoViewIfNeeded_, 0)
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttributeNS__)

        self.assertResultIsBOOL(WebKit.DOMElement.contains_)
