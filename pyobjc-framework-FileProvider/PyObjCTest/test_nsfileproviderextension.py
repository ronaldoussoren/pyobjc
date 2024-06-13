import FileProvider
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSFileProviderExtensionHelper(FileProvider.NSObject):
    def shouldConnectExternalDomainWithCompletionHandler_(self, a):
        pass


class TestNSFileProviderExtension(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderItemContents, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderItemFilename, 1 << 1)
        self.assertEqual(FileProvider.NSFileProviderItemParentItemIdentifier, 1 << 2)
        self.assertEqual(FileProvider.NSFileProviderItemLastUsedDate, 1 << 3)
        self.assertEqual(FileProvider.NSFileProviderItemTagData, 1 << 4)
        self.assertEqual(FileProvider.NSFileProviderItemFavoriteRank, 1 << 5)
        self.assertEqual(FileProvider.NSFileProviderItemCreationDate, 1 << 6)
        self.assertEqual(FileProvider.NSFileProviderItemContentModificationDate, 1 << 7)
        self.assertEqual(FileProvider.NSFileProviderItemFileSystemFlags, 1 << 8)
        self.assertEqual(FileProvider.NSFileProviderItemExtendedAttributes, 1 << 9)

    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderExternalVolumeHandling")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestNSFileProviderExtensionHelper.shouldConnectExternalDomainWithCompletionHandler_,
            0,
            b"v@",
        )

    def test_methods(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.itemForIdentifier_error_, 1
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.providePlaceholderAtURL_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.startProvidingItemAtURL_completionHandler_,
            1,
            b"v@",
        )
