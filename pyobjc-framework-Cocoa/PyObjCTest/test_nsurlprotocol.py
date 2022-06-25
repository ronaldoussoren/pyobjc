import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLProtocolHelper(Foundation.NSObject):
    def URLProtocol_didReceiveResponse_cacheStoragePolicy_(self, a, b, c):
        pass


class TestNSURLProtocol(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSURLProtocol.canInitWithRequest_)
        self.assertResultIsBOOL(
            Foundation.NSURLProtocol.requestIsCacheEquivalent_toRequest_
        )
        self.assertResultIsBOOL(Foundation.NSURLProtocol.registerClass_)

        self.assertArgHasType(
            TestNSURLProtocolHelper.URLProtocol_didReceiveResponse_cacheStoragePolicy_,
            2,
            objc._C_NSUInteger,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Foundation.NSURLProtocol.canInitWithTask_)

    def testProtocols(self):
        self.assertProtocolExists("NSURLProtocolClient")
