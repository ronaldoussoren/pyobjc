from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderExtension(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderItemFieldContents, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderItemFieldFilename, 1 << 1)
        self.assertEqual(
            FileProvider.NSFileProviderItemFieldParentItemIdentifier, 1 << 2
        )
        self.assertEqual(FileProvider.NSFileProviderItemFieldLastUsedDate, 1 << 3)
        self.assertEqual(FileProvider.NSFileProviderItemFieldTagData, 1 << 4)
        self.assertEqual(FileProvider.NSFileProviderItemFieldFavoriteRank, 1 << 5)
        self.assertEqual(FileProvider.NSFileProviderItemFieldCreationDate, 1 << 6)
        self.assertEqual(
            FileProvider.NSFileProviderItemFieldContentModificationDate, 1 << 7
        )
        self.assertEqual(FileProvider.NSFileProviderItemFieldFlags, 1 << 8)
        self.assertEqual(FileProvider.NSFileProviderItemFieldTrashed, 1 << 9)
        self.assertEqual(
            FileProvider.NSFileProviderItemFieldExtendedAttributes, 1 << 10
        )
