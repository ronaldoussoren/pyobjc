from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFFTPStream (TestCase):

    def testConstants(self):
        self.failUnlessIsInstance(kCFStreamErrorDomainFTP, (int, long))
        self.failUnlessIsInstance(kCFStreamPropertyFTPUserName, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPPassword, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPUsePassiveMode, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPResourceSize, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPFetchResourceInfo, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPFileTransferOffset, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPAttemptPersistentConnection, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPProxy, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPProxyHost, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPProxyPort, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPProxyUser, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyFTPProxyPassword, unicode)
        self.failUnlessIsInstance(kCFFTPResourceMode, unicode)
        self.failUnlessIsInstance(kCFFTPResourceName, unicode)
        self.failUnlessIsInstance(kCFFTPResourceOwner, unicode)
        self.failUnlessIsInstance(kCFFTPResourceGroup, unicode)
        self.failUnlessIsInstance(kCFFTPResourceLink, unicode)
        self.failUnlessIsInstance(kCFFTPResourceSize, unicode)
        self.failUnlessIsInstance(kCFFTPResourceType, unicode)
        self.failUnlessIsInstance(kCFFTPResourceModDate, unicode)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CFReadStreamCreateWithFTPURL)
        url = CFURLCreateWithString(None, "ftp://ftp.python.org/", None)
        self.failUnlessIsInstance(url, CFURLRef)
        ftp = CFReadStreamCreateWithFTPURL(None,  url)
        self.failUnlessIsInstance(ftp, CFReadStreamRef)

        buf = '-rw-r--r--  1 ronald  staff  1957 Mar 31 07:22 test_cfftpstream.py\r\n'
        self.failUnlessArgHasType(CFFTPCreateParsedResourceListing, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFFTPCreateParsedResourceListing, 1, 2)
        self.failUnlessArgIsOut(CFFTPCreateParsedResourceListing, 3)
        cnt, out = CFFTPCreateParsedResourceListing(None, buf, len(buf), None)
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnlessIsInstance(out, CFDictionaryRef)
        self.failUnlessEqual(out[kCFFTPResourceGroup], "staff")

        self.failUnlessResultIsCFRetained(CFWriteStreamCreateWithFTPURL)
        url = CFURLCreateWithString(None, "ftp://www.rivm.nl/incoming/test.txt", None)
        self.failUnlessIsInstance(url, CFURLRef)
        ftp = CFWriteStreamCreateWithFTPURL(None,  url)
        self.failUnlessIsInstance(ftp, CFWriteStreamRef)

if __name__ == "__main__":
    main()
