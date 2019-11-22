from PyObjCTools.TestSupport import *

from ImageCaptureCore import *


class TestICCameraFile(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ICCameraFile.highFramerate)
        self.assertResultIsBOOL(ICCameraFile.timeLapse)
        self.assertResultIsBOOL(ICCameraFile.firstPicked)
        self.assertResultIsBOOL(ICCameraFile.burstFavorite)
        self.assertResultIsBOOL(ICCameraFile.burstPicked)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            ICCameraFile.requestThumbnailDataWithOptions_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            ICCameraFile.requestMetadataDictionaryWithOptions_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            ICCameraFile.requestDownloadWithOptions_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            ICCameraFile.requestReadDataAtOffset_length_completion_, 2, b"v@@"
        )


if __name__ == "__main__":
    main()
