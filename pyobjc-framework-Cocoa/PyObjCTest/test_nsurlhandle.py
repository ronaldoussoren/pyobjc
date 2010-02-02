from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLHandle (TestCase):
    def testMethods(self):
        self.assertIsInstance(NSHTTPPropertyStatusCodeKey, unicode)
        self.assertIsInstance(NSHTTPPropertyStatusReasonKey, unicode)
        self.assertIsInstance(NSHTTPPropertyServerHTTPVersionKey, unicode)
        self.assertIsInstance(NSHTTPPropertyRedirectionHeadersKey, unicode)
        self.assertIsInstance(NSHTTPPropertyErrorPageDataKey, unicode)
        self.assertIsInstance(NSHTTPPropertyHTTPProxy, unicode)
        self.assertIsInstance(NSFTPPropertyUserLoginKey, unicode)
        self.assertIsInstance(NSFTPPropertyUserPasswordKey, unicode)
        self.assertIsInstance(NSFTPPropertyActiveTransferModeKey, unicode)
        self.assertIsInstance(NSFTPPropertyFileOffsetKey, unicode)
        self.assertIsInstance(NSFTPPropertyFTPProxy, unicode)

        self.assertEqual(NSURLHandleNotLoaded, 0)
        self.assertEqual(NSURLHandleLoadSucceeded, 1)
        self.assertEqual(NSURLHandleLoadInProgress, 2)
        self.assertEqual(NSURLHandleLoadFailed, 3)

    def testMethods(self):
        self.assertArgIsBOOL(NSURLHandle.didLoadBytes_loadComplete_, 1)
        self.assertResultIsBOOL(NSURLHandle.canInitWithURL_)
        self.assertArgIsBOOL(NSURLHandle.initWithURL_cached_, 1)
        self.assertResultIsBOOL(NSURLHandle.writeProperty_forKey_)
        self.assertResultIsBOOL(NSURLHandle.writeData_)

if __name__ == "__main__":
    main()
