from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHTTPCookie(TestCase):
    def testConstants(self):
        self.assertIsInstance(NSHTTPCookieName, unicode)
        self.assertIsInstance(NSHTTPCookieValue, unicode)
        self.assertIsInstance(NSHTTPCookieOriginURL, unicode)
        self.assertIsInstance(NSHTTPCookieVersion, unicode)
        self.assertIsInstance(NSHTTPCookieDomain, unicode)
        self.assertIsInstance(NSHTTPCookiePath, unicode)
        self.assertIsInstance(NSHTTPCookieSecure, unicode)
        self.assertIsInstance(NSHTTPCookieExpires, unicode)
        self.assertIsInstance(NSHTTPCookieComment, unicode)
        self.assertIsInstance(NSHTTPCookieCommentURL, unicode)
        self.assertIsInstance(NSHTTPCookieDiscard, unicode)
        self.assertIsInstance(NSHTTPCookieMaximumAge, unicode)
        self.assertIsInstance(NSHTTPCookiePort, unicode)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(NSHTTPCookieSameSitePolicy, unicode)
        self.assertIsInstance(NSHTTPCookieSameSiteLax, unicode)
        self.assertIsInstance(NSHTTPCookieSameSiteStrict, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSHTTPCookie.isSessionOnly)
        self.assertResultIsBOOL(NSHTTPCookie.isSecure)
        self.assertResultIsBOOL(NSHTTPCookie.isHTTPOnly)


if __name__ == "__main__":
    main()
