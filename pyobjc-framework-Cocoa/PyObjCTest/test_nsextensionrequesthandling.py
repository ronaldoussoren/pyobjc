import Foundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSExtensionRequestHandling(TestCase):
    @min_sdk_level("10.10")
    def testProtocols10_10(self):
        self.assertProtocolExists("NSExtensionRequestHandling")
