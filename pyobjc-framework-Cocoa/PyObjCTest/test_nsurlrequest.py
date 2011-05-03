from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLRequest (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLRequestUseProtocolCachePolicy, 0)
        self.assertEqual(NSURLRequestReloadIgnoringLocalCacheData, 1)
        self.assertEqual(NSURLRequestReloadIgnoringLocalAndRemoteCacheData, 4)
        self.assertEqual(NSURLRequestReloadIgnoringCacheData, NSURLRequestReloadIgnoringLocalCacheData)
        self.assertEqual(NSURLRequestReturnCacheDataElseLoad, 2)
        self.assertEqual(NSURLRequestReturnCacheDataDontLoad, 3)
        self.assertEqual(NSURLRequestReloadRevalidatingCacheData, 5)

    def testMethods(self):
        self.assertResultIsBOOL(NSURLRequest.HTTPShouldHandleCookies)
        self.assertArgIsBOOL(NSMutableURLRequest.setHTTPShouldHandleCookies_, 0)

if __name__ == "__main__":
    main()
