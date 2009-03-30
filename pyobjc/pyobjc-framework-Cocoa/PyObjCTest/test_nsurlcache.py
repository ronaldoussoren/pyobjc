from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLCache (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSURLCacheStorageAllowed, 0)
        self.failUnlessEqual(NSURLCacheStorageAllowedInMemoryOnly, 1)
        self.failUnlessEqual(NSURLCacheStorageNotAllowed, 2)

if __name__ == "__main__":
    main()
