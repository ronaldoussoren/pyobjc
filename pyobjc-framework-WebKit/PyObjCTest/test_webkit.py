"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
import WebKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestWebKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(WebKit, "WebResource")
        self.assertIsInstance(WebKit.WebResource, objc.objc_class)

        self.assertHasAttr(WebKit, "DOMHTMLObjectElement")
        self.assertIsInstance(WebKit.DOMHTMLObjectElement, objc.objc_class)

    def testValues(self):
        self.assertHasAttr(WebKit, "DOM_CSS_PERCENTAGE")
        self.assertIsInstance(WebKit.DOM_CSS_PERCENTAGE, int)
        self.assertEqual(WebKit.DOM_CSS_PERCENTAGE, 2)

        self.assertHasAttr(WebKit, "DOM_CSS_VALUE_LIST")
        self.assertIsInstance(WebKit.DOM_CSS_VALUE_LIST, int)
        self.assertEqual(WebKit.DOM_CSS_VALUE_LIST, 2)

        self.assertHasAttr(WebKit, "WebViewInsertActionDropped")
        self.assertIsInstance(WebKit.WebViewInsertActionDropped, int)

    def testVariables(self):
        self.assertHasAttr(WebKit, "DOMRangeException")
        self.assertIsInstance(WebKit.DOMRangeException, str)

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("DOMEventListener")
        objc.protocolNamed("DOMEventTarget")
        objc.protocolNamed("DOMNodeFilter")
        objc.protocolNamed("DOMXPathNSResolver")
        objc.protocolNamed("WebDocumentRepresentation")
        objc.protocolNamed("WebDocumentSearching")
        objc.protocolNamed("WebDocumentText")
        objc.protocolNamed("WebDocumentView")
        objc.protocolNamed("WebOpenPanelResultListener")
        objc.protocolNamed("WebPlugInViewFactory")
        objc.protocolNamed("WebPolicyDecisionListener")
