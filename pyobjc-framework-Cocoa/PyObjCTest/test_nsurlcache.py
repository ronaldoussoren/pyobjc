from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLCache (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLCacheStorageAllowed, 0)
        self.assertEqual(NSURLCacheStorageAllowedInMemoryOnly, 1)
        self.assertEqual(NSURLCacheStorageNotAllowed, 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSURLCache.getCachedResponseForDataTask_completionHandler_, 1, b'v@')

if __name__ == "__main__":
    main()
