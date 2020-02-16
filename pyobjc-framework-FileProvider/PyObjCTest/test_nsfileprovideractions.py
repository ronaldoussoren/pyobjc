from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderActions(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.performActionWithIdentifier_onItemsWithIdentifiers_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.importDocumentAtURL_toParentItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.createDirectoryWithName_inParentItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.renameItemWithIdentifier_toName_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.reparentItemWithIdentifier_toParentItemWithIdentifier_newName_completionHandler_,
            3,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.trashItemWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.untrashItemWithIdentifier_toParentItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.deleteItemWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setLastUsedDate_forItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setTagData_forItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setFavoriteRank_forItemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.performActionWithIdentifier_onItemsWithIdentifiers_completionHandler_,
            2,
            b"v@",
        )
