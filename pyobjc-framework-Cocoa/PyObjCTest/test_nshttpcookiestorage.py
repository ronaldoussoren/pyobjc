from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSHTTPCookieStorage (TestCase):
    def testConstants(self):
        self.assertEqual(NSHTTPCookieAcceptPolicyAlways, 0)
        self.assertEqual(NSHTTPCookieAcceptPolicyNever, 1)
        self.assertEqual(NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain, 2)

        self.assertIsInstance(NSHTTPCookieManagerAcceptPolicyChangedNotification, unicode)
        self.assertIsInstance(NSHTTPCookieManagerCookiesChangedNotification, unicode)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSHTTPCookieStorage.getCookiesForTask_completionHandler_, 1, b'v@')

if __name__ == "__main__":
    main()
