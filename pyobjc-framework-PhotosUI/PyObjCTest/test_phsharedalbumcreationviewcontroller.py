from PyObjCTools.TestSupport import TestCase, min_sdk_level
import PhotosUI


class TestPHSharedAlbumCreationViewController(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PhotosUI.PHSharedAlbumCreationSharingPolicy)
        self.assertEqual(PhotosUI.PHSharedAlbumCreationSharingPolicyPrivate, 0)
        self.assertEqual(PhotosUI.PHSharedAlbumCreationSharingPolicyPublic, 1)

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "PHSharedAlbumCreationViewControllerDelegate", PhotosUI
        )
