from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSHTTPCookieStorage (TestCase):
    def testConstants(self):
        self.assertEqual(NSHTTPCookieAcceptPolicyAlways, 0)
        self.assertEqual(NSHTTPCookieAcceptPolicyNever, 1)
        self.assertEqual(NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain, 2)

        self.assertIsInstance(NSHTTPCookieManagerAcceptPolicyChangedNotification, unicode)
        self.assertIsInstance(NSHTTPCookieManagerCookiesChangedNotification, unicode)

if __name__ == "__main__":
    main()
