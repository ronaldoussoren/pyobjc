import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLProtectionSpace(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSURLProtectionSpaceHTTPProxy, str)
        self.assertIsInstance(Foundation.NSURLProtectionSpaceHTTPSProxy, str)
        self.assertIsInstance(Foundation.NSURLProtectionSpaceFTPProxy, str)
        self.assertIsInstance(Foundation.NSURLProtectionSpaceSOCKSProxy, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodDefault, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodHTTPBasic, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodHTTPDigest, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodHTMLForm, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Foundation.NSURLProtectionSpaceHTTP, str)
        self.assertIsInstance(Foundation.NSURLProtectionSpaceHTTPS, str)
        self.assertIsInstance(Foundation.NSURLProtectionSpaceFTP, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodNTLM, str)
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodNegotiate, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(
            Foundation.NSURLAuthenticationMethodClientCertificate, str
        )
        self.assertIsInstance(Foundation.NSURLAuthenticationMethodServerTrust, str)

    def testMethods(self):
        self.assertResultIsBOOL(
            Foundation.NSURLProtectionSpace.receivesCredentialSecurely
        )
        self.assertResultIsBOOL(Foundation.NSURLProtectionSpace.isProxy)
