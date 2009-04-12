from CFNetwork import *
from PyObjCTools.TestSupport import *
from Foundation import NSString

class TestCFFTPStream (TestCase):

    def testTypes(self):
        self.failUnlessIsCFType(CFHTTPAuthenticationRef)

    def testConstants(self):
        self.failUnlessEqual(kCFStreamErrorHTTPAuthenticationTypeUnsupported, -1000)
        self.failUnlessEqual(kCFStreamErrorHTTPAuthenticationBadUserName, -1001)
        self.failUnlessEqual(kCFStreamErrorHTTPAuthenticationBadPassword, -1002)

        self.failUnlessIsInstance(kCFHTTPAuthenticationUsername, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationPassword, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationAccountDomain, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CFHTTPAuthenticationGetTypeID(), (int, long))

        msg = CFHTTPMessageCreateResponse(None, 401, "Authenticate", kCFHTTPVersion1_0)
        self.failUnlessIsInstance(msg, CFHTTPMessageRef)
        CFHTTPMessageSetHeaderFieldValue(msg, NSString.stringWithString_('WWW-Authenticate'), NSString.stringWithString_('Basic realm="WallyWorld"'))


        self.failUnlessResultIsCFRetained(CFHTTPAuthenticationCreateFromResponse)
        ref = CFHTTPAuthenticationCreateFromResponse(None, msg)
        self.failUnlessIsInstance(ref, CFHTTPAuthenticationRef)

        self.failUnlessResultIsBOOL(CFHTTPAuthenticationIsValid)
        self.failUnlessArgIsOut(CFHTTPAuthenticationIsValid, 1)
        v, err = CFHTTPAuthenticationIsValid(ref, None)
        self.failUnlessIsInstance(v, bool)
        if v:
            self.failUnless(err is None)
        else:
            self.failUnlessIsInstance(err, CFStreamError)

        self.failUnlessResultIsBOOL(CFHTTPAuthenticationAppliesToRequest)
        v = CFHTTPAuthenticationAppliesToRequest(ref, msg)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultIsBOOL(CFHTTPAuthenticationRequiresOrderedRequests)
        v = CFHTTPAuthenticationRequiresOrderedRequests(ref)
        self.failUnlessIsInstance(v, bool)

        url = CFURLCreateWithString(None, "http://www.python.org/", None)
        req = CFHTTPMessageCreateRequest(None, "GET", url, "1.0")

        self.failUnlessResultIsBOOL(CFHTTPMessageApplyCredentials)
        self.failUnlessArgIsOut(CFHTTPMessageApplyCredentials, 4)
        v, err = CFHTTPMessageApplyCredentials(req, ref, "ronald", "secret", None)
        if v is True:
            self.failUnlessEqual(err, None)

        else:
            self.failUnlessIsInstance(err, CFStreamError)

        self.failUnlessResultIsBOOL(CFHTTPMessageApplyCredentialDictionary)
        self.failUnlessArgIsOut(CFHTTPMessageApplyCredentialDictionary, 3)
        v, err = CFHTTPMessageApplyCredentialDictionary(req, ref, {
                kCFHTTPAuthenticationUsername: 'ronald',
                kCFHTTPAuthenticationPassword: 'secret',
            }, None)
        if v is True:
            self.failUnlessEqual(err, None)
        else:
            self.failUnlessIsInstance(err, CFStreamError)

        self.failUnlessResultIsCFRetained(CFHTTPAuthenticationCopyRealm)
        self.failUnlessResultHasType(CFHTTPAuthenticationCopyRealm, '^{__CFString=}')
        v = CFHTTPAuthenticationCopyRealm(ref)
        self.failUnless(v is None or isinstance(v, unicode))

        self.failUnlessResultIsCFRetained(CFHTTPAuthenticationCopyDomains)
        self.failUnlessResultHasType(CFHTTPAuthenticationCopyDomains, '^{__CFArray=}')
        v = CFHTTPAuthenticationCopyDomains(ref)
        self.failUnless(v is None or isinstance(v, CFArrayRef))

        self.failUnlessResultIsCFRetained(CFHTTPAuthenticationCopyMethod)
        self.failUnlessResultHasType(CFHTTPAuthenticationCopyMethod, '^{__CFString=}')
        v = CFHTTPAuthenticationCopyMethod(ref)
        self.failUnless(v is None or isinstance(v, unicode))

        self.failUnlessResultIsBOOL(CFHTTPAuthenticationRequiresUserNameAndPassword)
        v = CFHTTPAuthenticationRequiresUserNameAndPassword(ref)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultIsBOOL(CFHTTPAuthenticationRequiresAccountDomain)
        v = CFHTTPAuthenticationRequiresAccountDomain(ref)
        self.failUnlessIsInstance(v, bool)



    


if __name__ == "__main__":
    main()
