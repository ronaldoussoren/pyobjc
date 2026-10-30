from PyObjCTools.TestSupport import TestCase, min_sdk_level
import PhotosUI


class TestPHSharedAlbumCustomizationViewController(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "PHSharedAlbumCustomizationViewControllerDelegate", PhotosUI
        )
