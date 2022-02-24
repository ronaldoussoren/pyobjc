import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLCache(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSURLCacheStoragePolicy)

    def testConstants(self):
        self.assertEqual(Foundation.NSURLCacheStorageAllowed, 0)
        self.assertEqual(Foundation.NSURLCacheStorageAllowedInMemoryOnly, 1)
        self.assertEqual(Foundation.NSURLCacheStorageNotAllowed, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSURLCache.getCachedResponseForDataTask_completionHandler_,
            1,
            b"v@",
        )
