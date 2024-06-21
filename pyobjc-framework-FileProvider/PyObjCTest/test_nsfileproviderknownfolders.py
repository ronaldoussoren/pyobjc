import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderKnownFoldersHelper(FileProvider.NSObject):
    def getKnownFolderLocations_completionHandler_(self, a, b):
        pass


class TestNSFileProviderKnownFolders(TestCase):
    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            FileProvider.NSFileProviderKnownFolderLocations.shouldCreateBinaryCompatibilitySymlink
        )
        self.assertArgIsBOOL(
            FileProvider.NSFileProviderKnownFolderLocations.setShouldCreateBinaryCompatibilitySymlink_,
            0,
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.claimKnownFolders_localizedReason_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.releaseKnownFolders_localizedReason_completionHandler_,
            2,
            b"v@",
        )

    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderKnownFolderSupporting")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestNSFileProviderKnownFoldersHelper.getKnownFolderLocations_completionHandler_,
            1,
            b"v@@",
        )
