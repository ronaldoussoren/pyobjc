from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLCredentialStorage (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSURLCredentialStorageChangedNotification, unicode)

if __name__ == "__main__":
    main()
