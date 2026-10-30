import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLProtocolHelper(Foundation.NSObject):
    def URLProtocol_didReceiveResponse_cacheStoragePolicy_(self, a, b, c):
        pass


class TestNSURLProtocol(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSURLProtocol.canInitWithRequest_)
        self.assertResultIsBOOL(
            Foundation.NSURLProtocol.requestIsCacheEquivalent_toRequest_
        )
        self.assertResultIsBOOL(Foundation.NSURLProtocol.registerClass_)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(Foundation.NSURLProtocol.canInitWithTask_)

    def test_protocols(self):
        self.assertProtocolExists("NSURLProtocolClient", Foundation)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNSURLProtocolHelper.URLProtocol_didReceiveResponse_cacheStoragePolicy_,
            2,
            objc._C_NSUInteger,
        )
