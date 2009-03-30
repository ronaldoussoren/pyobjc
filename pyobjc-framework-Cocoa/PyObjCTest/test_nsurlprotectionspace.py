from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLProtectionSpace (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSURLProtectionSpaceHTTPProxy, unicode)
        self.failUnlessIsInstance(NSURLProtectionSpaceHTTPSProxy, unicode)
        self.failUnlessIsInstance(NSURLProtectionSpaceFTPProxy, unicode)
        self.failUnlessIsInstance(NSURLProtectionSpaceSOCKSProxy, unicode)
        self.failUnlessIsInstance(NSURLAuthenticationMethodDefault, unicode)
        self.failUnlessIsInstance(NSURLAuthenticationMethodHTTPBasic, unicode)
        self.failUnlessIsInstance(NSURLAuthenticationMethodHTTPDigest, unicode)
        self.failUnlessIsInstance(NSURLAuthenticationMethodHTMLForm, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLProtectionSpace.receivesCredentialSecurely)
        self.failUnlessResultIsBOOL(NSURLProtectionSpace.isProxy)

if __name__ == "__main__":
    main()
