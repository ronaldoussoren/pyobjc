"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import WebKit


class TestWebKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(WebKit, "WebResource")
        self.assertIsInstance(WebKit.WebResource, objc.objc_class)

        self.assertHasAttr(WebKit, "DOMHTMLObjectElement")
        self.assertIsInstance(WebKit.DOMHTMLObjectElement, objc.objc_class)

    def testValues(self):
        self.assertHasAttr(WebKit, "DOM_CSS_PERCENTAGE")
        self.assertIsInstance(WebKit.DOM_CSS_PERCENTAGE, (int, long))
        self.assertEqual(WebKit.DOM_CSS_PERCENTAGE, 2)

        self.assertHasAttr(WebKit, "DOM_CSS_VALUE_LIST")
        self.assertIsInstance(WebKit.DOM_CSS_VALUE_LIST, (int, long))
        self.assertEqual(WebKit.DOM_CSS_VALUE_LIST, 2)

        self.assertHasAttr(WebKit, "WebViewInsertActionDropped")
        self.assertIsInstance(WebKit.WebViewInsertActionDropped, (int, long))

    def testVariables(self):
        self.assertHasAttr(WebKit, "DOMRangeException")
        self.assertIsInstance(WebKit.DOMRangeException, unicode)

    @onlyOn32Bit
    def testFunctions(self):
        self.assertHasAttr(WebKit, "WebConvertNSImageToCGImageRef")
        self.assertIsInstance(WebKit.WebConvertNSImageToCGImageRef, objc.function)

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


if __name__ == "__main__":
    main()
