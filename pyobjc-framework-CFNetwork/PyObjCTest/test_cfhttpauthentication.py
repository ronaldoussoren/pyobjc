import CFNetwork
from Foundation import NSString
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCFFTPStream(TestCase):
    def testTypes(self):
        self.assertIsCFType(CFNetwork.CFHTTPAuthenticationRef)

    def testConstants(self):
        self.assertEqual(
            CFNetwork.kCFStreamErrorHTTPAuthenticationTypeUnsupported, -1000
        )
        self.assertEqual(CFNetwork.kCFStreamErrorHTTPAuthenticationBadUserName, -1001)
        self.assertEqual(CFNetwork.kCFStreamErrorHTTPAuthenticationBadPassword, -1002)

        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationUsername, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationPassword, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationAccountDomain, str)

    @min_os_level("10.5")
    # These functions should work on 10.4 as well, but caue a crash in
    # CFNetwork on that platform
    def testFunctions(self):
        self.assertIsInstance(CFNetwork.CFHTTPAuthenticationGetTypeID(), int)

        msg = CFNetwork.CFHTTPMessageCreateResponse(
            None, 401, "Authenticate", CFNetwork.kCFHTTPVersion1_0
        )
        self.assertIsInstance(msg, CFNetwork.CFHTTPMessageRef)
        CFNetwork.CFHTTPMessageSetHeaderFieldValue(
            msg,
            NSString.stringWithString_("WWW-Authenticate"),
            NSString.stringWithString_('Basic realm="WallyWorld"'),
        )

        self.assertResultIsCFRetained(CFNetwork.CFHTTPAuthenticationCreateFromResponse)
        ref = CFNetwork.CFHTTPAuthenticationCreateFromResponse(None, msg)
        self.assertIsInstance(ref, CFNetwork.CFHTTPAuthenticationRef)

        self.assertResultIsBOOL(CFNetwork.CFHTTPAuthenticationIsValid)
        self.assertArgIsOut(CFNetwork.CFHTTPAuthenticationIsValid, 1)
        v, err = CFNetwork.CFHTTPAuthenticationIsValid(ref, None)
        self.assertIsInstance(v, bool)
        if v:
            self.assertTrue(err is None)
        else:
            self.assertIsInstance(err, CFNetwork.CFStreamError)

        self.assertResultIsBOOL(CFNetwork.CFHTTPAuthenticationAppliesToRequest)
        v = CFNetwork.CFHTTPAuthenticationAppliesToRequest(ref, msg)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(CFNetwork.CFHTTPAuthenticationRequiresOrderedRequests)
        v = CFNetwork.CFHTTPAuthenticationRequiresOrderedRequests(ref)
        self.assertIsInstance(v, bool)

        url = CFNetwork.CFURLCreateWithString(None, "http://www.python.org/", None)
        req = CFNetwork.CFHTTPMessageCreateRequest(None, "GET", url, "1.0")

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageApplyCredentials)
        self.assertArgIsOut(CFNetwork.CFHTTPMessageApplyCredentials, 4)
        v, err = CFNetwork.CFHTTPMessageApplyCredentials(
            req, ref, "ronald", "secret", None
        )
        if v is True:
            self.assertEqual(err, None)

        else:
            self.assertIsInstance(err, CFNetwork.CFStreamError)

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageApplyCredentialDictionary)
        self.assertArgIsOut(CFNetwork.CFHTTPMessageApplyCredentialDictionary, 3)
        v, err = CFNetwork.CFHTTPMessageApplyCredentialDictionary(
            req,
            ref,
            {
                CFNetwork.kCFHTTPAuthenticationUsername: "ronald",
                CFNetwork.kCFHTTPAuthenticationPassword: "secret",
            },
            None,
        )
        if v is True:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFNetwork.CFStreamError)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPAuthenticationCopyRealm)
        self.assertResultHasType(
            CFNetwork.CFHTTPAuthenticationCopyRealm, b"^{__CFString=}"
        )
        v = CFNetwork.CFHTTPAuthenticationCopyRealm(ref)
        self.assertTrue(v is None or isinstance(v, str))

        self.assertResultIsCFRetained(CFNetwork.CFHTTPAuthenticationCopyDomains)
        self.assertResultHasType(
            CFNetwork.CFHTTPAuthenticationCopyDomains, b"^{__CFArray=}"
        )
        v = CFNetwork.CFHTTPAuthenticationCopyDomains(ref)
        self.assertTrue(v is None or isinstance(v, CFNetwork.CFArrayRef))

        self.assertResultIsCFRetained(CFNetwork.CFHTTPAuthenticationCopyMethod)
        self.assertResultHasType(
            CFNetwork.CFHTTPAuthenticationCopyMethod, b"^{__CFString=}"
        )
        v = CFNetwork.CFHTTPAuthenticationCopyMethod(ref)
        self.assertTrue(v is None or isinstance(v, str))

        self.assertResultIsBOOL(
            CFNetwork.CFHTTPAuthenticationRequiresUserNameAndPassword
        )
        v = CFNetwork.CFHTTPAuthenticationRequiresUserNameAndPassword(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(CFNetwork.CFHTTPAuthenticationRequiresAccountDomain)
        v = CFNetwork.CFHTTPAuthenticationRequiresAccountDomain(ref)
        self.assertIsInstance(v, bool)
