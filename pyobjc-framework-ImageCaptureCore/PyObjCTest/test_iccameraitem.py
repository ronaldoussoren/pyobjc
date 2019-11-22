from PyObjCTools.TestSupport import *

from ImageCaptureCore import *


class TestICCameraItem(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ICCameraItem.isLocked)
        self.assertResultIsBOOL(ICCameraItem.isInTemporaryStore)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(ICCameraItem.isRaw)
        self.assertResultIsBOOL(ICCameraItem.wasAddedAfterContentCatalogCompleted)

    @min_os_level("10.4")
    def test_constants10_4(self):
        self.assertIsInstance(ICDownloadsDirectoryURL, unicode)
        self.assertIsInstance(ICSaveAsFilename, unicode)
        self.assertIsInstance(ICSavedFilename, unicode)
        self.assertIsInstance(ICSavedAncillaryFiles, unicode)
        self.assertIsInstance(ICOverwrite, unicode)
        self.assertIsInstance(ICDeleteAfterSuccessfulDownload, unicode)
        self.assertIsInstance(ICDownloadSidecarFiles, unicode)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(ICImageSourceThumbnailMaxPixelSize, unicode)
        self.assertIsInstance(ICImageSourceShouldCache, unicode)


if __name__ == "__main__":
    main()
