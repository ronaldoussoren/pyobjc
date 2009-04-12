from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFHTTPMessage (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCFHTTPVersion1_0, unicode)
        self.failUnlessIsInstance(kCFHTTPVersion1_1, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationSchemeBasic, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationSchemeDigest, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationSchemeNTLM, unicode)
        self.failUnlessIsInstance(kCFHTTPAuthenticationSchemeNegotiate, unicode)

    def testTypes(self):
        self.failUnlessIsCFType(CFHTTPMessageRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CFHTTPMessageGetTypeID(), (int, long))

        url = CFURLCreateWithString(None, "http://www.python.org/", None)
        self.failUnlessIsInstance(url, CFURLRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCreateRequest)
        req = CFHTTPMessageCreateRequest(None, "GET", url, kCFHTTPVersion1_1)
        self.failUnlessIsInstance(req, CFHTTPMessageRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCreateResponse)
        resp = CFHTTPMessageCreateResponse(None, 200, "Okidoki", kCFHTTPVersion1_1)
        self.failUnlessIsInstance(req, CFHTTPMessageRef)
        
        self.failUnlessResultIsCFRetained(CFHTTPMessageCreateEmpty)
        self.failUnlessArgIsBOOL(CFHTTPMessageCreateEmpty, 1)
        m = CFHTTPMessageCreateEmpty(None, True)
        self.failUnlessIsInstance(m, CFHTTPMessageRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCreateCopy)
        m = CFHTTPMessageCreateCopy(None, req)
        self.failUnlessIsInstance(m, CFHTTPMessageRef)

        self.failUnlessResultIsBOOL(CFHTTPMessageIsRequest)
        self.failUnless(CFHTTPMessageIsRequest(req) is True)
        self.failUnless(CFHTTPMessageIsRequest(resp) is False)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyVersion)
        v = CFHTTPMessageCopyVersion(req)
        self.failUnlessIsInstance(v, unicode)

        CFHTTPMessageSetBody(req, buffer("hello world"))

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyBody)
        b = CFHTTPMessageCopyBody(req)
        self.failUnlessIsInstance(b, (CFDataRef, buffer))

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyAllHeaderFields)
        v = CFHTTPMessageCopyAllHeaderFields(req)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyHeaderFieldValue)
        v = CFHTTPMessageCopyHeaderFieldValue(req, u"X-Python")
        self.failUnless(v is None)

        CFHTTPMessageSetHeaderFieldValue(req, u"X-Python", u"Rocks")
        v = CFHTTPMessageCopyHeaderFieldValue(req, u"X-Python")
        self.failUnlessEqual(v, u"Rocks")

        self.failUnlessResultIsBOOL(CFHTTPMessageAppendBytes)
        self.failUnlessArgHasType(CFHTTPMessageAppendBytes, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFHTTPMessageAppendBytes, 1, 2)

        v = CFHTTPMessageAppendBytes(req, "hello world", 11)
        self.failUnless(v is True)


        self.failUnlessResultIsBOOL(CFHTTPMessageIsHeaderComplete)
        v = CFHTTPMessageIsHeaderComplete(req)
        self.failUnless(v is False)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopySerializedMessage)
        v = CFHTTPMessageCopySerializedMessage(resp)
        self.failUnlessIsInstance(v, CFDataRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyRequestURL)
        v = CFHTTPMessageCopyRequestURL(req)
        self.failUnlessIsInstance(v, CFURLRef)

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyRequestMethod)
        v = CFHTTPMessageCopyRequestMethod(req)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsBOOL(CFHTTPMessageAddAuthentication)
        self.failUnlessArgIsBOOL(CFHTTPMessageAddAuthentication, 5)
        v = CFHTTPMessageAddAuthentication(req, resp, u"ronald", u"secret", kCFHTTPAuthenticationSchemeNTLM, False)
        self.failUnlessIsInstance(v, bool)

        v = CFHTTPMessageGetResponseStatusCode(resp)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(CFHTTPMessageCopyResponseStatusLine)
        v = CFHTTPMessageCopyResponseStatusLine(resp)
        self.failUnlessIsInstance(v, unicode)


if __name__ == "__main__":
    main()






