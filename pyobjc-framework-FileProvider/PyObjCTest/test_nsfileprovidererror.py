import FileProvider
from PyObjCTools.TestSupport import TestCase


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
        self.assertEqual(FileProvider.NSFileProviderErrorDeletionRejected, -1006)
        self.assertEqual(FileProvider.NSFileProviderErrorDirectoryNotEmpty, -1007)
        self.assertEqual(FileProvider.NSFileProviderErrorProviderNotFound, -2001)
        self.assertEqual(FileProvider.NSFileProviderErrorProviderTranslocated, -2002)
        self.assertEqual(
            FileProvider.NSFileProviderErrorOlderExtensionVersionRunning, -2003
        )
        self.assertEqual(
            FileProvider.NSFileProviderErrorNewerExtensionVersionFound, -2004
        )
        self.assertEqual(FileProvider.NSFileProviderErrorCannotSynchronize, -2005)
