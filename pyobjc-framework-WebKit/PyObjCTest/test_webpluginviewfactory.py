from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebPluginViewFactory(TestCase):
    def test_constants(self):
        self.assertIsInstance(WebKit.WebPlugInBaseURLKey, str)
        self.assertIsInstance(WebKit.WebPlugInAttributesKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainerKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainingElementKey, str)
        self.assertIsInstance(WebKit.WebPlugInShouldLoadMainResourceKey, str)

    def test_protocols(self):
        self.assertProtocolExists("WebPlugInViewFactory", WebKit)
