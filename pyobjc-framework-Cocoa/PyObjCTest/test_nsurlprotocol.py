from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLProtocolHelper (NSObject):
    def URLProtocol_didReceiveResponse_cacheStoragePolicy_(self, a, b, c): pass

class TestNSURLProtocol (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSURLProtocol.canInitWithRequest_)
        self.assertResultIsBOOL(NSURLProtocol.requestIsCacheEquivalent_toRequest_)
        self.assertResultIsBOOL(NSURLProtocol.registerClass_)

        self.assertArgHasType(TestNSURLProtocolHelper.URLProtocol_didReceiveResponse_cacheStoragePolicy_, 2, objc._C_NSUInteger)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSURLProtocol.canInitWithTask_)

    def testProtocols(self):
        objc.protocolNamed('NSURLProtocolClient')

if __name__ == "__main__":
    main()
