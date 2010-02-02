from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLProtectionSpace (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSURLProtectionSpaceHTTPProxy, unicode)
        self.assertIsInstance(NSURLProtectionSpaceHTTPSProxy, unicode)
        self.assertIsInstance(NSURLProtectionSpaceFTPProxy, unicode)
        self.assertIsInstance(NSURLProtectionSpaceSOCKSProxy, unicode)
        self.assertIsInstance(NSURLAuthenticationMethodDefault, unicode)
        self.assertIsInstance(NSURLAuthenticationMethodHTTPBasic, unicode)
        self.assertIsInstance(NSURLAuthenticationMethodHTTPDigest, unicode)
        self.assertIsInstance(NSURLAuthenticationMethodHTMLForm, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSURLAuthenticationMethodClientCertificate, unicode)
        self.assertIsInstance(NSURLAuthenticationMethodServerTrust, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSURLProtectionSpace.receivesCredentialSecurely)
        self.assertResultIsBOOL(NSURLProtectionSpace.isProxy)

if __name__ == "__main__":
    main()
