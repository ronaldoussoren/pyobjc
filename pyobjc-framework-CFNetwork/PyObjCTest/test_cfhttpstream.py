from CFNetwork import *
from PyObjCTools.TestSupport import *
import os

class TestCFHTTPStream (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCFStreamErrorHTTPParseFailure, -1)
        self.failUnlessEqual(kCFStreamErrorHTTPRedirectionLoop, -2)
        self.failUnlessEqual(kCFStreamErrorHTTPBadURL, -3)

        self.failUnlessIsInstance(kCFStreamPropertyHTTPResponseHeader, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPFinalURL, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPFinalRequest, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPProxy, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPProxyHost, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPProxyPort, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPSProxyHost, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPSProxyPort, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPShouldAutoredirect, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPAttemptPersistentConnection, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyHTTPRequestBytesWrittenCount, unicode)

    def testFunctions(self):
       url = CFURLCreateWithString(None, "http://www.python.org/", None)
       self.failUnlessIsInstance(url, CFURLRef)

       req = CFHTTPMessageCreateRequest(None, "GET", url, kCFHTTPVersion1_1)
       self.failUnlessIsInstance(req, CFHTTPMessageRef)

       self.failUnlessResultIsCFRetained(CFReadStreamCreateForHTTPRequest)
       v = CFReadStreamCreateForHTTPRequest(None, req)
       self.failUnlessIsInstance(v, CFReadStreamRef)

       fp = open("/dev/null", "w")
       fd_2 = os.dup(2)
       os.dup2(fp.fileno(), 2)

       try:
           # Avoid deprecation messages from CFNetwork

           self.failUnlessResultIsCFRetained(CFReadStreamCreateForStreamedHTTPRequest)
           v = CFReadStreamCreateForStreamedHTTPRequest(None, req, v)
           self.failUnlessIsInstance(v, CFReadStreamRef)

           self.failUnlessArgIsBOOL(CFHTTPReadStreamSetRedirectsAutomatically, 1)
           CFHTTPReadStreamSetRedirectsAutomatically(v, True)

           CFHTTPReadStreamSetProxy(v, u"localhost", 8080)

       finally:
           os.dup2(fd_2, 2)

if __name__ == "__main__":
    main()
