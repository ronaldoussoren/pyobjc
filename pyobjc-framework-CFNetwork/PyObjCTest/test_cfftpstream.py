from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFFTPStream (TestCase):

    def testConstants(self):
        self.assertIsInstance(kCFStreamErrorDomainFTP, (int, long))
        self.assertIsInstance(kCFStreamPropertyFTPUserName, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPPassword, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPUsePassiveMode, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPResourceSize, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPFetchResourceInfo, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPFileTransferOffset, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPAttemptPersistentConnection, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPProxy, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPProxyHost, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPProxyPort, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPProxyUser, unicode)
        self.assertIsInstance(kCFStreamPropertyFTPProxyPassword, unicode)
        self.assertIsInstance(kCFFTPResourceMode, unicode)
        self.assertIsInstance(kCFFTPResourceName, unicode)
        self.assertIsInstance(kCFFTPResourceOwner, unicode)
        self.assertIsInstance(kCFFTPResourceGroup, unicode)
        self.assertIsInstance(kCFFTPResourceLink, unicode)
        self.assertIsInstance(kCFFTPResourceSize, unicode)
        self.assertIsInstance(kCFFTPResourceType, unicode)
        self.assertIsInstance(kCFFTPResourceModDate, unicode)

    def testFunctions(self):
        self.assertResultIsCFRetained(CFReadStreamCreateWithFTPURL)
        url = CFURLCreateWithString(None, "ftp://ftp.python.org/", None)
        self.assertIsInstance(url, CFURLRef)
        ftp = CFReadStreamCreateWithFTPURL(None,  url)
        self.assertIsInstance(ftp, CFReadStreamRef)

        buf = b'-rw-r--r--  1 ronald  staff  1957 Mar 31 07:22 test_cfftpstream.py\r\n'
        self.assertArgHasType(CFFTPCreateParsedResourceListing, 1, b'n^v')
        self.assertArgSizeInArg(CFFTPCreateParsedResourceListing, 1, 2)
        self.assertArgIsOut(CFFTPCreateParsedResourceListing, 3)
        cnt, out = CFFTPCreateParsedResourceListing(None, buf, len(buf), None)
        self.assertIsInstance(cnt, (int, long))
        self.assertIsInstance(out, CFDictionaryRef)
        self.assertEqual(out[kCFFTPResourceGroup], "staff")

        self.assertResultIsCFRetained(CFWriteStreamCreateWithFTPURL)
        url = CFURLCreateWithString(None, "ftp://www.rivm.nl/incoming/test.txt", None)
        self.assertIsInstance(url, CFURLRef)
        ftp = CFWriteStreamCreateWithFTPURL(None,  url)
        self.assertIsInstance(ftp, CFWriteStreamRef)

if __name__ == "__main__":
    main()
