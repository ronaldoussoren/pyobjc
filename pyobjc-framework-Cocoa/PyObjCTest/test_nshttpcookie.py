import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSHTTPCookie(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSHTTPCookiePropertyKey, str)
        self.assertIsTypedEnum(Foundation.NSHTTPCookieStringPolicy, str)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSHTTPCookieName, str)
        self.assertIsInstance(Foundation.NSHTTPCookieValue, str)
        self.assertIsInstance(Foundation.NSHTTPCookieOriginURL, str)
        self.assertIsInstance(Foundation.NSHTTPCookieVersion, str)
        self.assertIsInstance(Foundation.NSHTTPCookieDomain, str)
        self.assertIsInstance(Foundation.NSHTTPCookiePath, str)
        self.assertIsInstance(Foundation.NSHTTPCookieSecure, str)
        self.assertIsInstance(Foundation.NSHTTPCookieExpires, str)
        self.assertIsInstance(Foundation.NSHTTPCookieComment, str)
        self.assertIsInstance(Foundation.NSHTTPCookieCommentURL, str)
        self.assertIsInstance(Foundation.NSHTTPCookieDiscard, str)
        self.assertIsInstance(Foundation.NSHTTPCookieMaximumAge, str)
        self.assertIsInstance(Foundation.NSHTTPCookiePort, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Foundation.NSHTTPCookieSameSitePolicy, str)
        self.assertIsInstance(Foundation.NSHTTPCookieSameSiteLax, str)
        self.assertIsInstance(Foundation.NSHTTPCookieSameSiteStrict, str)

    @min_os_level("15.2")
    def testConstants15_2(self):
        self.assertIsInstance(Foundation.NSHTTPCookieSetByJavaScript, str)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSHTTPCookie.isSessionOnly)
        self.assertResultIsBOOL(Foundation.NSHTTPCookie.isSecure)
        self.assertResultIsBOOL(Foundation.NSHTTPCookie.isHTTPOnly)
