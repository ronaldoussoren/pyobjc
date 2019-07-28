from PyObjCTools.TestSupport import *

import FileProvider

class TestNSFileProviderExtension (TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderItemFieldContents, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderItemFieldFilename, 1 << 1)
        self.assertEqual(FileProvider.NSFileProviderItemFieldParentItemIdentifier, 1 << 2)
        self.assertEqual(FileProvider.NSFileProviderItemFieldLastUsedDate, 1 << 3)
        self.assertEqual(FileProvider.NSFileProviderItemFieldTagData, 1 << 4)
        self.assertEqual(FileProvider.NSFileProviderItemFieldFavoriteRank, 1 << 5)
        self.assertEqual(FileProvider.NSFileProviderItemFieldCreationDate, 1 << 6)
        self.assertEqual(FileProvider.NSFileProviderItemFieldContentModificationDate, 1 << 7)
        self.assertEqual(FileProvider.NSFileProviderItemFieldFlags, 1 << 8)
        self.assertEqual(FileProvider.NSFileProviderItemFieldTrashed, 1 << 9)
        self.assertEqual(FileProvider.NSFileProviderItemFieldExtendedAttributes, 1 << 10)

        self.assertEqual(FileProvider.NSFileProviderCreateItemOptionsItemMayAlreadyExist, 1 << 0)

        self.assertEqual(FileProvider.NSFileProviderDeleteItemOptionsRecursive, 1 << 0)


    @min_os_level('10.15')
    def test_methods10_15(self):
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.fetchContentsForItemWithIdentifier_version_completionHandler_, 2, b'v@@@')
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.fetchContentsForItemWithIdentifier_version_usingExistingContentsAtURL_existingVersion_completionHandler_, 4, b'v@@@')
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.itemChanged_baseVersion_changedFields_contents_completionHandler_, 4, b'v@@')
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.createItemBasedOnTemplate_fields_contents_options_completionHandler_, 4, b'v@@')
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.deleteItemWithIdentifier_baseVersion_options_completionHandler_, 3, b'v@')
        self.assertArgIsBlock(FileProvier.NSFileProviderExtension.importDidFinishWithCompletionHandler_, 0, b'v')
