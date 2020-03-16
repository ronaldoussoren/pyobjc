from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import WebKit
import objc


class TestWebPluginViewFactory(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.WebPlugInBaseURLKey, str)
        self.assertIsInstance(WebKit.WebPlugInAttributesKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainerKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainingElementKey, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(WebKit.WebPlugInShouldLoadMainResourceKey, str)

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("WebPlugInViewFactory")
