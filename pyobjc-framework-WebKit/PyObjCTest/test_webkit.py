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
        self.assertProtocolExists("DOMEventListener", WebKit)
        self.assertProtocolExists("DOMEventTarget", WebKit)
        self.assertProtocolExists("DOMNodeFilter", WebKit, "DOMNodeFilterProtocol")
        self.assertProtocolExists("DOMXPathNSResolver", WebKit)
        self.assertProtocolExists("WebDocumentRepresentation", WebKit)
        self.assertProtocolExists("WebDocumentSearching", WebKit)
        self.assertProtocolExists("WebDocumentText", WebKit)
        self.assertProtocolExists("WebDocumentView", WebKit)
        self.assertProtocolExists(
            "WebOpenPanelResultListener", WebKit, "WebOpenPanelResultListenerProtocol"
        )
        self.assertProtocolExists("WebPlugInViewFactory", WebKit)
        self.assertProtocolExists(
            "WebPolicyDecisionListener", WebKit, "WebPolicyDecisionListenerProtocol"
        )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(WebKit)
