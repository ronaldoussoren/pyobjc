from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSKitError(TestCase):
    def test_constants(self):
        self.assertIsInstance(FSKit.FSKitErrorDomain, str)

        self.assertIsEnumType(FSKit.FSErrorCode)

        self.assertEqual(FSKit.FSErrorModuleLoadFailed, 4500)
        self.assertEqual(FSKit.FSErrorResourceUnrecognized, 4501)
        self.assertEqual(FSKit.FSErrorResourceDamaged, 4502)
        self.assertEqual(FSKit.FSErrorResourceUnusable, 4503)
        self.assertEqual(FSKit.FSErrorStatusOperationInProgress, 4504)
        self.assertEqual(FSKit.FSErrorStatusOperationPaused, 4505)
        self.assertEqual(FSKit.FSErrorInvalidDirectoryCookie, 4506)

        self.assertIsEnumType(FSKit.FSDataCacheErrorCode)
        self.assertEqual(FSKit.FSErrorInvalidCacheModeCoherency, 4510)
        self.assertEqual(FSKit.FSErrorInvalidCacheTransition, 4511)
        self.assertEqual(FSKit.FSErrorCacheFlushFailed, 4512)
        self.assertEqual(FSKit.FSErrorCacheInvalidationFailed, 4513)
        self.assertEqual(FSKit.FSErrorCacheOperationConflict, 4514)
