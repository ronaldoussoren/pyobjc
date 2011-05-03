from CFNetwork import *
from PyObjCTools.TestSupport import *
import sys

if sys.version_info[0] != 2:
    def buffer(value):
        return value.encode('latin1')

class TestCFHTTPMessage (TestCase):

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCFHTTPAuthenticationSchemeNTLM, unicode)
        self.assertIsInstance(kCFHTTPAuthenticationSchemeNegotiate, unicode)

    def testConstants(self):
        self.assertIsInstance(kCFHTTPVersion1_0, unicode)
        self.assertIsInstance(kCFHTTPVersion1_1, unicode)
        self.assertIsInstance(kCFHTTPAuthenticationSchemeBasic, unicode)
        self.assertIsInstance(kCFHTTPAuthenticationSchemeDigest, unicode)

    def testTypes(self):
        self.assertIsCFType(CFHTTPMessageRef)

    def testFunctions(self):
        self.assertIsInstance(CFHTTPMessageGetTypeID(), (int, long))

        url = CFURLCreateWithString(None, "http://www.python.org/", None)
        self.assertIsInstance(url, CFURLRef)

        self.assertResultIsCFRetained(CFHTTPMessageCreateRequest)
        req = CFHTTPMessageCreateRequest(None, "GET", url, kCFHTTPVersion1_1)
        self.assertIsInstance(req, CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFHTTPMessageCreateResponse)
        resp = CFHTTPMessageCreateResponse(None, 200, "Okidoki", kCFHTTPVersion1_1)
        self.assertIsInstance(req, CFHTTPMessageRef)
        
        self.assertResultIsCFRetained(CFHTTPMessageCreateEmpty)
        self.assertArgIsBOOL(CFHTTPMessageCreateEmpty, 1)
        m = CFHTTPMessageCreateEmpty(None, True)
        self.assertIsInstance(m, CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFHTTPMessageCreateCopy)
        m = CFHTTPMessageCreateCopy(None, req)
        self.assertIsInstance(m, CFHTTPMessageRef)

        self.assertResultIsBOOL(CFHTTPMessageIsRequest)
        self.assertTrue(CFHTTPMessageIsRequest(req) is True)
        self.assertTrue(CFHTTPMessageIsRequest(resp) is False)

        self.assertResultIsCFRetained(CFHTTPMessageCopyVersion)
        v = CFHTTPMessageCopyVersion(req)
        self.assertIsInstance(v, unicode)

        CFHTTPMessageSetBody(req, buffer("hello world"))

        self.assertResultIsCFRetained(CFHTTPMessageCopyBody)
        b = CFHTTPMessageCopyBody(req)
        if sys.version_info[0] == 2:
            self.assertIsInstance(b, (CFDataRef, buffer))
        else:
            self.assertIsInstance(b, (CFDataRef, memoryview, bytes))

        self.assertResultIsCFRetained(CFHTTPMessageCopyAllHeaderFields)
        v = CFHTTPMessageCopyAllHeaderFields(req)
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertResultIsCFRetained(CFHTTPMessageCopyHeaderFieldValue)
        v = CFHTTPMessageCopyHeaderFieldValue(req, u"X-Python")
        self.assertTrue(v is None)

        CFHTTPMessageSetHeaderFieldValue(req, u"X-Python", u"Rocks")
        v = CFHTTPMessageCopyHeaderFieldValue(req, u"X-Python")
        self.assertEqual(v, u"Rocks")

        self.assertResultIsBOOL(CFHTTPMessageAppendBytes)
        self.assertArgHasType(CFHTTPMessageAppendBytes, 1, b'n^v')
        self.assertArgSizeInArg(CFHTTPMessageAppendBytes, 1, 2)

        v = CFHTTPMessageAppendBytes(req, b"hello world", 11)
        self.assertTrue(v is True)


        self.assertResultIsBOOL(CFHTTPMessageIsHeaderComplete)
        v = CFHTTPMessageIsHeaderComplete(req)
        self.assertTrue(v is False)

        self.assertResultIsCFRetained(CFHTTPMessageCopySerializedMessage)
        v = CFHTTPMessageCopySerializedMessage(resp)
        self.assertIsInstance(v, CFDataRef)

        self.assertResultIsCFRetained(CFHTTPMessageCopyRequestURL)
        v = CFHTTPMessageCopyRequestURL(req)
        self.assertIsInstance(v, CFURLRef)

        self.assertResultIsCFRetained(CFHTTPMessageCopyRequestMethod)
        v = CFHTTPMessageCopyRequestMethod(req)
        self.assertIsInstance(v, unicode)

        self.assertResultIsBOOL(CFHTTPMessageAddAuthentication)
        self.assertArgIsBOOL(CFHTTPMessageAddAuthentication, 5)
        v = CFHTTPMessageAddAuthentication(req, resp, u"ronald", u"secret", kCFHTTPAuthenticationSchemeBasic, False)
        self.assertIsInstance(v, bool)

        v = CFHTTPMessageGetResponseStatusCode(resp)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CFHTTPMessageCopyResponseStatusLine)
        v = CFHTTPMessageCopyResponseStatusLine(resp)
        self.assertIsInstance(v, unicode)


if __name__ == "__main__":
    main()






