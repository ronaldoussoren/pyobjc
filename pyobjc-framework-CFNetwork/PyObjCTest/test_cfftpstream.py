import CFNetwork
from PyObjCTools.TestSupport import TestCase


class TestCFFTPStream(TestCase):
    def testConstants(self):
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainFTP, int)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPUserName, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPPassword, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPUsePassiveMode, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPResourceSize, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPFetchResourceInfo, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPFileTransferOffset, str)
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertyFTPAttemptPersistentConnection, str
        )
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPProxy, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPProxyHost, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPProxyPort, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPProxyUser, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyFTPProxyPassword, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceMode, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceName, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceOwner, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceGroup, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceLink, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceSize, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceType, str)
        self.assertIsInstance(CFNetwork.kCFFTPResourceModDate, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(CFNetwork.CFReadStreamCreateWithFTPURL)
        url = CFNetwork.CFURLCreateWithString(None, "ftp://ftp.python.org/", None)
        self.assertIsInstance(url, CFNetwork.CFURLRef)
        ftp = CFNetwork.CFReadStreamCreateWithFTPURL(None, url)
        self.assertIsInstance(ftp, CFNetwork.CFReadStreamRef)

        buf = b"-rw-r--r--  1 ronald  staff  1957 Mar 31 07:22 test_cfftpstream.py\r\n"
        self.assertArgHasType(CFNetwork.CFFTPCreateParsedResourceListing, 1, b"n^v")
        self.assertArgSizeInArg(CFNetwork.CFFTPCreateParsedResourceListing, 1, 2)
        self.assertArgIsOut(CFNetwork.CFFTPCreateParsedResourceListing, 3)
        cnt, out = CFNetwork.CFFTPCreateParsedResourceListing(None, buf, len(buf), None)
        self.assertIsInstance(cnt, int)
        self.assertIsInstance(out, CFNetwork.CFDictionaryRef)
        self.assertEqual(out[CFNetwork.kCFFTPResourceGroup], "staff")

        self.assertResultIsCFRetained(CFNetwork.CFWriteStreamCreateWithFTPURL)
        url = CFNetwork.CFURLCreateWithString(
            None, "ftp://www.rivm.nl/incoming/test.txt", None
        )
        self.assertIsInstance(url, CFNetwork.CFURLRef)
        ftp = CFNetwork.CFWriteStreamCreateWithFTPURL(None, url)
        self.assertIsInstance(ftp, CFNetwork.CFWriteStreamRef)
