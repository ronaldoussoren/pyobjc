from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPHPhotoLibrary_PhotosUISupport(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            PhotosUI.PHPhotoLibrary.presentLimitedLibraryPickerFromViewController_completionHandler_,
            1,
            b"v@",
        )
