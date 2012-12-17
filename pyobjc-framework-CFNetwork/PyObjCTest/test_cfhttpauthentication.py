from CFNetwork import *
from PyObjCTools.TestSupport import *
from Foundation import NSString

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestCFFTPStream (TestCase):

    def testTypes(self):
        self.assertIsCFType(CFHTTPAuthenticationRef)

    def testConstants(self):
        self.assertEqual(kCFStreamErrorHTTPAuthenticationTypeUnsupported, -1000)
        self.assertEqual(kCFStreamErrorHTTPAuthenticationBadUserName, -1001)
        self.assertEqual(kCFStreamErrorHTTPAuthenticationBadPassword, -1002)

        self.assertIsInstance(kCFHTTPAuthenticationUsername, unicode)
        self.assertIsInstance(kCFHTTPAuthenticationPassword, unicode)
        self.assertIsInstance(kCFHTTPAuthenticationAccountDomain, unicode)

    @min_os_level('10.5')
    #These functions should work on 10.4 as well, but caue a crash in CFNetwork on that platform
    def testFunctions(self):
        self.assertIsInstance(CFHTTPAuthenticationGetTypeID(), (int, long))

        msg = CFHTTPMessageCreateResponse(None, 401, "Authenticate", kCFHTTPVersion1_0)
        self.assertIsInstance(msg, CFHTTPMessageRef)
        CFHTTPMessageSetHeaderFieldValue(msg, NSString.stringWithString_('WWW-Authenticate'), NSString.stringWithString_('Basic realm="WallyWorld"'))

        self.assertResultIsCFRetained(CFHTTPAuthenticationCreateFromResponse)
        ref = CFHTTPAuthenticationCreateFromResponse(None, msg)
        self.assertIsInstance(ref, CFHTTPAuthenticationRef)

        self.assertResultIsBOOL(CFHTTPAuthenticationIsValid)
        self.assertArgIsOut(CFHTTPAuthenticationIsValid, 1)
        v, err = CFHTTPAuthenticationIsValid(ref, None)
        self.assertIsInstance(v, bool)
        if v:
            self.assertTrue(err is None)
        else:
            self.assertIsInstance(err, CFStreamError)

        self.assertResultIsBOOL(CFHTTPAuthenticationAppliesToRequest)
        v = CFHTTPAuthenticationAppliesToRequest(ref, msg)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(CFHTTPAuthenticationRequiresOrderedRequests)
        v = CFHTTPAuthenticationRequiresOrderedRequests(ref)
        self.assertIsInstance(v, bool)

        url = CFURLCreateWithString(None, "http://www.python.org/", None)
        req = CFHTTPMessageCreateRequest(None, "GET", url, "1.0")

        self.assertResultIsBOOL(CFHTTPMessageApplyCredentials)
        self.assertArgIsOut(CFHTTPMessageApplyCredentials, 4)
        v, err = CFHTTPMessageApplyCredentials(req, ref, "ronald", "secret", None)
        if v is True:
            self.assertEqual(err, None)

        else:
            self.assertIsInstance(err, CFStreamError)

        self.assertResultIsBOOL(CFHTTPMessageApplyCredentialDictionary)
        self.assertArgIsOut(CFHTTPMessageApplyCredentialDictionary, 3)
        v, err = CFHTTPMessageApplyCredentialDictionary(req, ref, {
                kCFHTTPAuthenticationUsername: 'ronald',
                kCFHTTPAuthenticationPassword: 'secret',
            }, None)
        if v is True:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFStreamError)

        self.assertResultIsCFRetained(CFHTTPAuthenticationCopyRealm)
        self.assertResultHasType(CFHTTPAuthenticationCopyRealm, b'@')
        v = CFHTTPAuthenticationCopyRealm(ref)
        self.assertTrue(v is None or isinstance(v, unicode))

        self.assertResultIsCFRetained(CFHTTPAuthenticationCopyDomains)
        self.assertResultHasType(CFHTTPAuthenticationCopyDomains, b'^{__CFArray=}')
        v = CFHTTPAuthenticationCopyDomains(ref)
        self.assertTrue(v is None or isinstance(v, CFArrayRef))

        self.assertResultIsCFRetained(CFHTTPAuthenticationCopyMethod)
        self.assertResultHasType(CFHTTPAuthenticationCopyMethod, b'@')
        v = CFHTTPAuthenticationCopyMethod(ref)
        self.assertTrue(v is None or isinstance(v, unicode))

        self.assertResultIsBOOL(CFHTTPAuthenticationRequiresUserNameAndPassword)
        v = CFHTTPAuthenticationRequiresUserNameAndPassword(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(CFHTTPAuthenticationRequiresAccountDomain)
        v = CFHTTPAuthenticationRequiresAccountDomain(ref)
        self.assertIsInstance(v, bool)






if __name__ == "__main__":
    main()
