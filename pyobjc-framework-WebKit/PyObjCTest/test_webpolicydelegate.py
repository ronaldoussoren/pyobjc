from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit


class TestWebPolicyDelegate(TestCase):
    def test_enums(self):
        self.assertIsEnumType(WebKit.WebNavigationType)
        self.assertEqual(WebKit.WebNavigationTypeLinkClicked, 0)
        self.assertEqual(WebKit.WebNavigationTypeFormSubmitted, 1)
        self.assertEqual(WebKit.WebNavigationTypeBackForward, 2)
        self.assertEqual(WebKit.WebNavigationTypeReload, 3)
        self.assertEqual(WebKit.WebNavigationTypeFormResubmitted, 4)
        self.assertEqual(WebKit.WebNavigationTypeOther, 5)

    def test_constants(self):
        self.assertIsInstance(WebKit.WebActionNavigationTypeKey, str)
        self.assertIsInstance(WebKit.WebActionElementKey, str)
        self.assertIsInstance(WebKit.WebActionButtonKey, str)
        self.assertIsInstance(WebKit.WebActionModifierFlagsKey, str)
        self.assertIsInstance(WebKit.WebActionOriginalURLKey, str)

    def test_protocols(self):
        self.assertProtocolExists(
            "WebPolicyDecisionListener", WebKit, "WebPolicyDecisionListenerProtocol"
        )

    @min_sdk_level("10.11")
    def test_protocols10_11(self):
        self.assertProtocolExists("WebPolicyDelegate", WebKit)
