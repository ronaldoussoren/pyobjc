import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestICCameraFile(TestCase):
    @min_os_level("10.10")
    def test_methods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraFile.highFramerate)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraFile.timeLapse)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraFile.firstPicked)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraFile.burstFavorite)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraFile.burstPicked)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraFile.requestThumbnailDataWithOptions_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraFile.requestMetadataDictionaryWithOptions_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraFile.requestDownloadWithOptions_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraFile.requestReadDataAtOffset_length_completion_,
            2,
            b"v@@",
        )
