import FileProvider
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFileProviderReplicatedExtensionHelper(FileProvider.NSObject):
    def enumeratorForContainerItemIdentifier_request_error_(self, a, b, c):
        pass

    def itemForIdentifier_request_completionHandler_(self, a, b, c):
        return 1

    def fetchContentsForItemWithIdentifier_version_request_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def createItemBasedOnTemplate_fields_contents_options_request_completionHandler_(
        self, a, b, c, d, e, f
    ):
        pass

    def modifyItem_baseVersion_changedFields_contents_options_request_completionHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def deleteItemWithIdentifier_baseVersion_options_request_completionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def importDidFinishWithCompletionHandler_(self, a):
        pass

    def materializedItemsDidChangeWithCompletionHandler_(self, a):
        pass

    def fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def performActionWithIdentifier_onItemsWithIdentifiers_completionHandler_(
        self, a, b, c
    ):
        pass

    def fetchContentsForItemWithIdentifier_version_usingExistingContentsAtURL_request_completionHandler_(
        self, a, b, c, d, e
    ):
        return 1

    def supportedServiceSourcesForItemIdentifier_completionHandler_(self, a, b):
        return 1


class TestNSFileProviderReplicatedExtension(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderCreateItemMayAlreadyExist, 1 << 0)

        self.assertEqual(FileProvider.NSFileProviderDeleteItemRecursive, 1 << 0)

        self.assertEqual(FileProvider.NSFileProviderModifyItemMayAlreadyExist, 1 << 0)

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

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderEnumerating")
        objc.protocolNamed("NSFileProviderReplicatedExtension")
        objc.protocolNamed("NSFileProviderIncrementalContentFetching")
        objc.protocolNamed("NSFileProviderServicing")
        objc.protocolNamed("NSFileProviderThumbnailing")
        objc.protocolNamed("NSFileProviderCustomAction")

    def test_methods(self):
        self.assertArgHasType(
            TestNSFileProviderReplicatedExtensionHelper.enumeratorForContainerItemIdentifier_request_error_,
            2,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.itemForIdentifier_request_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.fetchContentsForItemWithIdentifier_version_request_completionHandler_,
            3,
            b"v@@@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.createItemBasedOnTemplate_fields_contents_options_request_completionHandler_,  # noqa: B950
            4,
            b"v@@Z@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.modifyItem_baseVersion_changedFields_contents_options_request_completionHandler_,  # noqa: B950
            6,
            b"v@@Z@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.deleteItemWithIdentifier_baseVersion_options_request_completionHandler_,
            4,
            b"v@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.importDidFinishWithCompletionHandler_,
            0,
            b"v",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.materializedItemsDidChangeWithCompletionHandler_,
            0,
            b"v",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            3,
            b"v@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.performActionWithIdentifier_onItemsWithIdentifiers_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.fetchContentsForItemWithIdentifier_version_usingExistingContentsAtURL_request_completionHandler_,  # noqa: B950
            4,
            b"v@@@",
        )
