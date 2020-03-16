from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMElement(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_ALLOW_KEYBOARD_INPUT, 1)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttribute_)
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttributeNS_localName_)
        self.assertArgIsBOOL(WebKit.DOMElement.scrollIntoView_, 0)
        self.assertArgIsBOOL(WebKit.DOMElement.scrollIntoViewIfNeeded_, 0)
        self.assertResultIsBOOL(WebKit.DOMElement.hasAttributeNS__)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMElement.contains_)
