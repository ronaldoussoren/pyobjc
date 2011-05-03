from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLCache (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLCacheStorageAllowed, 0)
        self.assertEqual(NSURLCacheStorageAllowedInMemoryOnly, 1)
        self.assertEqual(NSURLCacheStorageNotAllowed, 2)

if __name__ == "__main__":
    main()
