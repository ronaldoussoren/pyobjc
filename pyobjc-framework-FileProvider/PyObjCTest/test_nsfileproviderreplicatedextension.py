import FileProvider
import Foundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFileProviderReplicatedExtensionHelper(FileProvider.NSObject):
    def setInteractionSuppressed_forIdentifier_(self, a, b):
        pass

    def isInteractionSuppressedForIdentifier_(self, a):
        return 1

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

    def pendingItemsDidChangeWithCompletionHandler_(self, a):
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

    def fetchPartialContentsForItemWithIdentifier_version_request_minimalRange_aligningTo_options_completionHandler_(  # noqa: B950
        self, a, b, c, d, e, f, g
    ):
        return 1


class TestNSFileProviderReplicatedExtension(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(FileProvider.NSFileProviderCreateItemOptions)
        self.assertIsEnumType(FileProvider.NSFileProviderDeleteItemOptions)
        self.assertIsEnumType(FileProvider.NSFileProviderFetchContentsOptions)
        self.assertIsEnumType(FileProvider.NSFileProviderItemFields)
        self.assertIsEnumType(FileProvider.NSFileProviderMaterializationFlags)
        self.assertIsEnumType(FileProvider.NSFileProviderModifyItemOptions)

    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderCreateItemMayAlreadyExist, 1 << 0)
        self.assertEqual(
            FileProvider.NSFileProviderCreateItemDeletionConflicted, 1 << 1
        )

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
        self.assertEqual(FileProvider.NSFileProviderItemTypeAndCreator, 1 << 10)

        self.assertEqual(
            FileProvider.NSFileProviderMaterializationFlagsKnownSparseRanges, 1 << 0
        )
        self.assertEqual(
            FileProvider.NSFileProviderFetchContentsOptionsStrictVersioning, 1 << 0
        )

    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("NSFileProviderEnumerating")
        self.assertProtocolExists("NSFileProviderReplicatedExtension")
        self.assertProtocolExists("NSFileProviderIncrementalContentFetching")
        self.assertProtocolExists("NSFileProviderServicing")
        self.assertProtocolExists("NSFileProviderThumbnailing")
        self.assertProtocolExists("NSFileProviderCustomAction")

    @min_sdk_level("11.3")
    def test_protocols11_3(self):
        self.assertProtocolExists("NSFileProviderDomainState")

    @min_sdk_level("12.0")
    def test_protocols12_0(self):
        self.assertProtocolExists("NSFileProviderUserInteractionSuppressing")

    @min_sdk_level("12.3")
    def test_protocols12_3(self):
        self.assertProtocolExists("NSFileProviderPartialContentFetching")

    def test_methods(self):
        self.assertArgIsBOOL(
            TestNSFileProviderReplicatedExtensionHelper.setInteractionSuppressed_forIdentifier_,
            0,
        )
        self.assertResultIsBOOL(
            TestNSFileProviderReplicatedExtensionHelper.isInteractionSuppressedForIdentifier_
        )

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
            TestNSFileProviderReplicatedExtensionHelper.pendingItemsDidChangeWithCompletionHandler_,
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

        self.assertArgHasType(
            TestNSFileProviderReplicatedExtensionHelper.fetchPartialContentsForItemWithIdentifier_version_request_minimalRange_aligningTo_options_completionHandler_,  # noqa: B950
            3,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSFileProviderReplicatedExtensionHelper.fetchPartialContentsForItemWithIdentifier_version_request_minimalRange_aligningTo_options_completionHandler_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSFileProviderReplicatedExtensionHelper.fetchPartialContentsForItemWithIdentifier_version_request_minimalRange_aligningTo_options_completionHandler_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestNSFileProviderReplicatedExtensionHelper.fetchPartialContentsForItemWithIdentifier_version_request_minimalRange_aligningTo_options_completionHandler_,  # noqa: B950
            6,
            b"v@@" + Foundation.NSRange.__typestr__ + b"Q@",
        )
