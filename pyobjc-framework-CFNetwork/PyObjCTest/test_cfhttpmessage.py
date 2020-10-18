import CFNetwork
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestCFHTTPMessage(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeNegotiate2, str)
        self.assertIsInstance(
            CFNetwork.kCFHTTPAuthenticationSchemeXMobileMeAuthToken, str
        )

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeNTLM, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeNegotiate, str)

    @expectedFailure
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CFNetwork.kCFHTTPVersion2_0, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeKerberos, str)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(CFNetwork.kCFHTTPVersion3_0, str)

    def testConstants(self):
        self.assertIsInstance(CFNetwork.kCFHTTPVersion1_0, str)
        self.assertIsInstance(CFNetwork.kCFHTTPVersion1_1, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeBasic, str)
        self.assertIsInstance(CFNetwork.kCFHTTPAuthenticationSchemeDigest, str)

    def testTypes(self):
        self.assertIsCFType(CFNetwork.CFHTTPMessageRef)

    def testFunctions(self):
        self.assertIsInstance(CFNetwork.CFHTTPMessageGetTypeID(), int)

        url = CFNetwork.CFURLCreateWithString(None, "http://www.python.org/", None)
        self.assertIsInstance(url, CFNetwork.CFURLRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCreateRequest)
        req = CFNetwork.CFHTTPMessageCreateRequest(
            None, "GET", url, CFNetwork.kCFHTTPVersion1_1
        )
        self.assertIsInstance(req, CFNetwork.CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCreateResponse)
        resp = CFNetwork.CFHTTPMessageCreateResponse(
            None, 200, "Okidoki", CFNetwork.kCFHTTPVersion1_1
        )
        self.assertIsInstance(req, CFNetwork.CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCreateEmpty)
        self.assertArgIsBOOL(CFNetwork.CFHTTPMessageCreateEmpty, 1)
        m = CFNetwork.CFHTTPMessageCreateEmpty(None, True)
        self.assertIsInstance(m, CFNetwork.CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCreateCopy)
        m = CFNetwork.CFHTTPMessageCreateCopy(None, req)
        self.assertIsInstance(m, CFNetwork.CFHTTPMessageRef)

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageIsRequest)
        self.assertTrue(CFNetwork.CFHTTPMessageIsRequest(req) is True)
        self.assertTrue(CFNetwork.CFHTTPMessageIsRequest(resp) is False)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyVersion)
        v = CFNetwork.CFHTTPMessageCopyVersion(req)
        self.assertIsInstance(v, str)

        CFNetwork.CFHTTPMessageSetBody(req, b"hello world")

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyBody)
        b = CFNetwork.CFHTTPMessageCopyBody(req)
        self.assertIsInstance(b, (CFNetwork.NSData, memoryview, bytes))

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyAllHeaderFields)
        v = CFNetwork.CFHTTPMessageCopyAllHeaderFields(req)
        self.assertIsInstance(v, CFNetwork.CFDictionaryRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyHeaderFieldValue)
        v = CFNetwork.CFHTTPMessageCopyHeaderFieldValue(req, "X-Python")
        self.assertTrue(v is None)

        CFNetwork.CFHTTPMessageSetHeaderFieldValue(req, "X-Python", "Rocks")
        v = CFNetwork.CFHTTPMessageCopyHeaderFieldValue(req, "X-Python")
        self.assertEqual(v, "Rocks")

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageAppendBytes)
        self.assertArgHasType(CFNetwork.CFHTTPMessageAppendBytes, 1, b"n^v")
        self.assertArgSizeInArg(CFNetwork.CFHTTPMessageAppendBytes, 1, 2)

        v = CFNetwork.CFHTTPMessageAppendBytes(req, b"hello world", 11)
        self.assertTrue(v is True)

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageIsHeaderComplete)
        v = CFNetwork.CFHTTPMessageIsHeaderComplete(req)
        self.assertTrue(v is False or v is True)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopySerializedMessage)
        v = CFNetwork.CFHTTPMessageCopySerializedMessage(resp)
        self.assertIsInstance(v, CFNetwork.CFDataRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyRequestURL)
        v = CFNetwork.CFHTTPMessageCopyRequestURL(req)
        self.assertIsInstance(v, CFNetwork.CFURLRef)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyRequestMethod)
        v = CFNetwork.CFHTTPMessageCopyRequestMethod(req)
        self.assertIsInstance(v, str)

        self.assertResultIsBOOL(CFNetwork.CFHTTPMessageAddAuthentication)
        self.assertArgIsBOOL(CFNetwork.CFHTTPMessageAddAuthentication, 5)
        v = CFNetwork.CFHTTPMessageAddAuthentication(
            req,
            resp,
            "ronald",
            "secret",
            CFNetwork.kCFHTTPAuthenticationSchemeBasic,
            False,
        )
        self.assertIsInstance(v, bool)

        v = CFNetwork.CFHTTPMessageGetResponseStatusCode(resp)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CFNetwork.CFHTTPMessageCopyResponseStatusLine)
        v = CFNetwork.CFHTTPMessageCopyResponseStatusLine(resp)
        self.assertIsInstance(v, str)
