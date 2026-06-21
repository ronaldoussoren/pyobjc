from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import WebKit


class TestWebPluginViewFactory(TestCase):
    def test_constants(self):
        self.assertIsInstance(WebKit.WebPlugInBaseURLKey, str)
        self.assertIsInstance(WebKit.WebPlugInAttributesKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainerKey, str)
        self.assertIsInstance(WebKit.WebPlugInContainingElementKey, str)

    @min_os_level("10.6")
    def test_constants10_6(self):
        self.assertIsInstance(WebKit.WebPlugInShouldLoadMainResourceKey, str)

    @min_sdk_level("10.6")
    def test_protocols(self):
        self.assertProtocolExists("WebPlugInViewFactory", WebKit)
