from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLRequest (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSURLRequestUseProtocolCachePolicy, 0)
        self.failUnlessEqual(NSURLRequestReloadIgnoringLocalCacheData, 1)
        self.failUnlessEqual(NSURLRequestReloadIgnoringLocalAndRemoteCacheData, 4)
        self.failUnlessEqual(NSURLRequestReloadIgnoringCacheData, NSURLRequestReloadIgnoringLocalCacheData)
        self.failUnlessEqual(NSURLRequestReturnCacheDataElseLoad, 2)
        self.failUnlessEqual(NSURLRequestReturnCacheDataDontLoad, 3)
        self.failUnlessEqual(NSURLRequestReloadRevalidatingCacheData, 5)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLRequest.HTTPShouldHandleCookies)
        self.failUnlessArgIsBOOL(NSMutableURLRequest.setHTTPShouldHandleCookies_, 0)

if __name__ == "__main__":
    main()
