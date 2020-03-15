import Foundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level, onlyOn64Bit
import objc


class TestNSExtensionRequestHandling(TestCase):
    @min_sdk_level("10.10")
    @onlyOn64Bit
    def testProtocols10_10(self):
        objc.protocolNamed("NSExtensionRequestHandling")
