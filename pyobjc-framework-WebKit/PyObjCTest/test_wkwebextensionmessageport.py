from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionMessagePort(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionMessagePortError)
        self.assertEqual(WebKit.WKWebExtensionMessagePortErrorUnknown, 1)
        self.assertEqual(WebKit.WKWebExtensionMessagePortErrorNotConnected, 2)
        self.assertEqual(WebKit.WKWebExtensionMessagePortErrorMessageInvalid, 3)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionMessagePortErrorDomain, str)

    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBlock(WebKit.WKWebExtensionMessagePort.messageHandler, b"v@@")
        self.assertArgIsBlock(
            WebKit.WKWebExtensionMessagePort.setMessageHandler_, 0, b"v@@"
        )

        self.assertResultIsBOOL(WebKit.WKWebExtensionMessagePort.isDisconnected)

        self.assertArgIsBlock(
            WebKit.WKWebExtensionMessagePort.sendMessage_completionHandler_, 1, b"v@"
        )
