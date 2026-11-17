from PyObjCTools.TestSupport import TestCase
import PhotosUI


class TestPHPhotoUIError(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PhotosUI.PHPhotosUIError)
        self.assertEqual(PhotosUI.PHPhotosUIAssetCollectionNotFoundError, 1)
        self.assertEqual(PhotosUI.PHPhotosUIAssetCollectionNotWritableError, 2)
        self.assertEqual(PhotosUI.PHPhotosUIAssetCollectionCreationFailedError, 3)
        self.assertEqual(PhotosUI.PHPhotosUISharedAlbumMigrationInProgressError, 100)
        self.assertEqual(PhotosUI.PHPhotosUIICloudPhotosNotEnabledError, 101)
