import os

import CFNetwork
from PyObjCTools.TestSupport import TestCase, min_os_level, os_level_key, os_release


class TestCFHTTPStream(TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPFinalRequest, str)

    def testConstants(self):
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainHTTP, int)

        self.assertEqual(CFNetwork.kCFStreamErrorHTTPParseFailure, -1)
        self.assertEqual(CFNetwork.kCFStreamErrorHTTPRedirectionLoop, -2)
        self.assertEqual(CFNetwork.kCFStreamErrorHTTPBadURL, -3)

        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPResponseHeader, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPFinalURL, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPProxy, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPProxyHost, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPProxyPort, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPSProxyHost, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPSProxyPort, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyHTTPShouldAutoredirect, str)
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertyHTTPAttemptPersistentConnection, str
        )
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertyHTTPRequestBytesWrittenCount, str
        )

    def testFunctions(self):
        url = CFNetwork.CFURLCreateWithString(None, "http://www.python.org/", None)
        self.assertIsInstance(url, CFNetwork.CFURLRef)

        req = CFNetwork.CFHTTPMessageCreateRequest(
            None, "GET", url, CFNetwork.kCFHTTPVersion1_1
        )
        self.assertIsInstance(req, CFNetwork.CFHTTPMessageRef)

        self.assertResultIsCFRetained(CFNetwork.CFReadStreamCreateForHTTPRequest)
        v = CFNetwork.CFReadStreamCreateForHTTPRequest(None, req)
        self.assertIsInstance(v, CFNetwork.CFReadStreamRef)

        with open("/dev/null", "w") as fp:
            fd_2 = os.dup(2)
            os.dup2(fp.fileno(), 2)

        try:
            # Avoid deprecation messages from CFNetwork

            self.assertResultIsCFRetained(
                CFNetwork.CFReadStreamCreateForStreamedHTTPRequest
            )
            v = CFNetwork.CFReadStreamCreateForStreamedHTTPRequest(None, req, v)
            self.assertIsInstance(v, CFNetwork.CFReadStreamRef)

            if os_level_key(os_release()) < os_level_key("10.15"):
                self.assertArgIsBOOL(
                    CFNetwork.CFHTTPReadStreamSetRedirectsAutomatically, 1
                )
                CFNetwork.CFHTTPReadStreamSetRedirectsAutomatically(v, True)

            if os_level_key(os_release()) < os_level_key("10.9"):
                CFNetwork.CFHTTPReadStreamSetProxy(v, "localhost", 8080)

        finally:
            os.dup2(fd_2, 2)
