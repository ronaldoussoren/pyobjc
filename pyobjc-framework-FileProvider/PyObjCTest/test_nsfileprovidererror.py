from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderError(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderErrorNotAuthenticated, -1000)
        self.assertEqual(FileProvider.NSFileProviderErrorFilenameCollision, -1001)
        self.assertEqual(FileProvider.NSFileProviderErrorSyncAnchorExpired, -1002)
        self.assertEqual(
            FileProvider.NSFileProviderErrorPageExpired,
            FileProvider.NSFileProviderErrorSyncAnchorExpired,
        )
        self.assertEqual(FileProvider.NSFileProviderErrorInsufficientQuota, -1003)
        self.assertEqual(FileProvider.NSFileProviderErrorServerUnreachable, -1004)
        self.assertEqual(FileProvider.NSFileProviderErrorNoSuchItem, -1005)
        self.assertEqual(FileProvider.NSFileProviderErrorVersionOutOfDate, -1006)
