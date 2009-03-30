from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSHTTPCookie (TestCase):
    def testConstants(self):
        self.failUnless( isinstance(NSHTTPCookieName, unicode) )
        self.failUnless( isinstance(NSHTTPCookieValue, unicode) )
        self.failUnless( isinstance(NSHTTPCookieOriginURL, unicode) )
        self.failUnless( isinstance(NSHTTPCookieVersion, unicode) )
        self.failUnless( isinstance(NSHTTPCookieDomain, unicode) )
        self.failUnless( isinstance(NSHTTPCookiePath, unicode) )
        self.failUnless( isinstance(NSHTTPCookieSecure, unicode) )
        self.failUnless( isinstance(NSHTTPCookieExpires, unicode) )
        self.failUnless( isinstance(NSHTTPCookieComment, unicode) )
        self.failUnless( isinstance(NSHTTPCookieCommentURL, unicode) )
        self.failUnless( isinstance(NSHTTPCookieDiscard, unicode) )
        self.failUnless( isinstance(NSHTTPCookieMaximumAge, unicode) )
        self.failUnless( isinstance(NSHTTPCookiePort, unicode) )

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSHTTPCookie.isSessionOnly)
        self.failUnlessResultIsBOOL(NSHTTPCookie.isSecure)

if __name__ == "__main__":
    main()
