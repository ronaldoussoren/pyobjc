from PyObjCTools.TestSupport import *

import FileProvider

class TestNSFileProviderError (TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderErrorNotAuthenticated, -1000)
        self.assertEqual(FileProvider.NSFileProviderErrorFilenameCollision, -1001)
        self.assertEqual(FileProvider.NSFileProviderErrorSyncAnchorExpired, -1002)
        self.assertEqual(FileProvider.NSFileProviderErrorPageExpired, FileProvider.NSFileProviderErrorSyncAnchorExpired)
        self.assertEqual(FileProvider.NSFileProviderErrorInsufficientQuota, -1003)
        self.assertEqual(FileProvider.NSFileProviderErrorServerUnreachable, -1004)
        self.assertEqual(FileProvider.NSFileProviderErrorNoSuchItem, -1005)
        self.assertEqual(FileProvider.NSFileProviderErrorVersionOutOfDate, -1006)
        self.assertEqual(FileProvider.NSFileProviderErrorDirectoryNotEmpty, -1007)

    @min_os_level('10.15')
    def test_constants10_15(self):
        self.assertIsInstance(FileProvider.NSFileProviderErrorItemKey, unicode)



