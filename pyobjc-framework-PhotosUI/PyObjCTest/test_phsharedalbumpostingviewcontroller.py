from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPHSharedAlbumPostingViewController(TestCase):
    @min_os_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("PHContentEditingController", PhotosUI)
