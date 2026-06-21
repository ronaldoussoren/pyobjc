from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKContentWorldConfiguration(TestCase):
    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.openClosedShadowRootsEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setOpenClosedShadowRootsEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.autofillScriptingEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setAutofillScriptingEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.elementUserInfoEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setElementUserInfoEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.legacyBuiltinOverridesEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setLegacyBuiltinOverridesEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.nodeSerializationEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setNodeSerializationEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.jsHandleCreationEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setJSHandleCreationEnabled_, 0
        )
        self.assertResultIsBOOL(WebKit.WKContentWorldConfiguration.isInspectable)
        self.assertArgIsBOOL(WebKit.WKContentWorldConfiguration.setInspectable_, 0)
