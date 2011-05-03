from CFNetwork import *
from PyObjCTools.TestSupport import *
import os

class TestCFHTTPStream (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCFStreamPropertyHTTPFinalRequest, unicode)

    def testConstants(self):
        self.assertEqual(kCFStreamErrorHTTPParseFailure, -1)
        self.assertEqual(kCFStreamErrorHTTPRedirectionLoop, -2)
        self.assertEqual(kCFStreamErrorHTTPBadURL, -3)

        self.assertIsInstance(kCFStreamPropertyHTTPResponseHeader, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPFinalURL, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPProxy, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPProxyHost, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPProxyPort, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPSProxyHost, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPSProxyPort, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPShouldAutoredirect, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPAttemptPersistentConnection, unicode)
        self.assertIsInstance(kCFStreamPropertyHTTPRequestBytesWrittenCount, unicode)

    def testFunctions(self):
       url = CFURLCreateWithString(None, "http://www.python.org/", None)
       self.assertIsInstance(url, CFURLRef)

       req = CFHTTPMessageCreateRequest(None, "GET", url, kCFHTTPVersion1_1)
       self.assertIsInstance(req, CFHTTPMessageRef)

       self.assertResultIsCFRetained(CFReadStreamCreateForHTTPRequest)
       v = CFReadStreamCreateForHTTPRequest(None, req)
       self.assertIsInstance(v, CFReadStreamRef)

       fp = open("/dev/null", "w")
       fd_2 = os.dup(2)
       os.dup2(fp.fileno(), 2)

       try:
           # Avoid deprecation messages from CFNetwork

           self.assertResultIsCFRetained(CFReadStreamCreateForStreamedHTTPRequest)
           v = CFReadStreamCreateForStreamedHTTPRequest(None, req, v)
           self.assertIsInstance(v, CFReadStreamRef)

           self.assertArgIsBOOL(CFHTTPReadStreamSetRedirectsAutomatically, 1)
           CFHTTPReadStreamSetRedirectsAutomatically(v, True)

           CFHTTPReadStreamSetProxy(v, u"localhost", 8080)

       finally:
           os.dup2(fd_2, 2)

if __name__ == "__main__":
    main()
