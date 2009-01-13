from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSHTTPCookieStorage (TestCase):
    def testConstants(self):
        self.assertEquals(NSHTTPCookieAcceptPolicyAlways, 0)
        self.assertEquals(NSHTTPCookieAcceptPolicyNever, 1)
        self.assertEquals(NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain, 2)

        self.failUnless(isinstance(NSHTTPCookieManagerAcceptPolicyChangedNotification, unicode))
        self.failUnless(isinstance(NSHTTPCookieManagerCookiesChangedNotification, unicode))


if __name__ == "__main__":
    main()
