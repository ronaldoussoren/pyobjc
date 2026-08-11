from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKContentWorldConfiguration(TestCase):
    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.allowAccessingClosedShadowRoots
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setAllowAccessingClosedShadowRoots_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.isAutofillScriptingEnabled
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
            WebKit.WKContentWorldConfiguration.isLegacyBuiltinOverridesEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setLegacyBuiltinOverridesEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.isNodeSnapshotCreationEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setNodeSerializationEnabled_, 0
        )
        self.assertResultIsBOOL(
            WebKit.WKContentWorldConfiguration.isJSHandleCreationEnabled
        )
        self.assertArgIsBOOL(
            WebKit.WKContentWorldConfiguration.setJSHandleCreationEnabled_, 0
        )
        self.assertResultIsBOOL(WebKit.WKContentWorldConfiguration.isInspectable)
        self.assertArgIsBOOL(WebKit.WKContentWorldConfiguration.setInspectable_, 0)
