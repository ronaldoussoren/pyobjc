import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestICCameraItem(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(ImageCaptureCore.ICCameraItemMetadataOption, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICCameraItemThumbnailOption, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICDownloadOption, str)

    def test_constants(self):
        self.assertIsInstance(ImageCaptureCore.ICDownloadsDirectoryURL, str)
        self.assertIsInstance(ImageCaptureCore.ICSaveAsFilename, str)
        self.assertIsInstance(ImageCaptureCore.ICSavedFilename, str)
        self.assertIsInstance(ImageCaptureCore.ICSavedAncillaryFiles, str)
        self.assertIsInstance(ImageCaptureCore.ICOverwrite, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteAfterSuccessfulDownload, str)
        self.assertIsInstance(ImageCaptureCore.ICDownloadSidecarFiles, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(ImageCaptureCore.ICImageSourceThumbnailMaxPixelSize, str)
        self.assertIsInstance(ImageCaptureCore.ICImageSourceShouldCache, str)

    def test_methods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraItem.isLocked)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraItem.isInTemporaryStore)

        self.assertResultIsBOOL(ImageCaptureCore.ICCameraItem.isRaw)
        self.assertResultIsBOOL(
            ImageCaptureCore.ICCameraItem.wasAddedAfterContentCatalogCompleted
        )
