import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderActions(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.importDocumentAtURL_toParentItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.createDirectoryWithName_inParentItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.renameItemWithIdentifier_toName_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.reparentItemWithIdentifier_toParentItemWithIdentifier_newName_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.trashItemWithIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.untrashItemWithIdentifier_toParentItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.deleteItemWithIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setLastUsedDate_forItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setTagData_forItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.setFavoriteRank_forItemIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
