from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit  # noqa: F401
import objc


class TestDOMXPathNSResolver(TestCase):
    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("DOMXPathNSResolver")
