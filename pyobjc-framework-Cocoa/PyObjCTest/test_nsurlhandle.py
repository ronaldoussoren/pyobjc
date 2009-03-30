from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLHandle (TestCase):
    def testMethods(self):
        self.failUnlessIsInstance(NSHTTPPropertyStatusCodeKey, unicode)
        self.failUnlessIsInstance(NSHTTPPropertyStatusReasonKey, unicode)
        self.failUnlessIsInstance(NSHTTPPropertyServerHTTPVersionKey, unicode)
        self.failUnlessIsInstance(NSHTTPPropertyRedirectionHeadersKey, unicode)
        self.failUnlessIsInstance(NSHTTPPropertyErrorPageDataKey, unicode)
        self.failUnlessIsInstance(NSHTTPPropertyHTTPProxy, unicode)
        self.failUnlessIsInstance(NSFTPPropertyUserLoginKey, unicode)
        self.failUnlessIsInstance(NSFTPPropertyUserPasswordKey, unicode)
        self.failUnlessIsInstance(NSFTPPropertyActiveTransferModeKey, unicode)
        self.failUnlessIsInstance(NSFTPPropertyFileOffsetKey, unicode)
        self.failUnlessIsInstance(NSFTPPropertyFTPProxy, unicode)

        self.failUnlessEqual(NSURLHandleNotLoaded, 0)
        self.failUnlessEqual(NSURLHandleLoadSucceeded, 1)
        self.failUnlessEqual(NSURLHandleLoadInProgress, 2)
        self.failUnlessEqual(NSURLHandleLoadFailed, 3)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSURLHandle.didLoadBytes_loadComplete_, 1)
        self.failUnlessResultIsBOOL(NSURLHandle.canInitWithURL_)
        self.failUnlessArgIsBOOL(NSURLHandle.initWithURL_cached_, 1)
        self.failUnlessResultIsBOOL(NSURLHandle.writeProperty_forKey_)
        self.failUnlessResultIsBOOL(NSURLHandle.writeData_)

if __name__ == "__main__":
    main()
