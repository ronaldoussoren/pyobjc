from PyObjCTools.TestSupport import TestCase

import FileProvider


class TestNSFileProviderModifyItemOptions(TestCase):
    def test_constants(self):
        self.assertIsEnumType(FileProvider.NSFileProviderModifyItemOptions)
        self.assertEqual(FileProvider.NSFileProviderModifyItemMayAlreadyExist, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderModifyItemFailOnConflict, 1 << 1)
        self.assertEqual(
            FileProvider.NSFileProviderModifyItemIsImmediateUploadRequestByPresentingApplication,
            1 << 2,
        )
