from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPhotosTypes (TestCase):
        @min_os_level('10.11')
        def testConstants(self):

            self.assertEqual(Photos.PHAssetMediaTypeUnknown, 0)
            self.assertEqual(Photos.PHAssetMediaTypeImage, 1)
            self.assertEqual(Photos.PHAssetMediaTypeVideo, 2)
            self.assertEqual(Photos.PHAssetMediaTypeAudio, 3)

            self.assertEqual(Photos.PHAssetMediaSubtypeNone, 0)

            self.assertEqual(Photos.PHAssetMediaSubtypePhotoPanorama, (1 << 0))
            self.assertEqual(Photos.PHAssetMediaSubtypePhotoHDR, (1 << 1))
            self.assertEqual(Photos.PHAssetMediaSubtypePhotoScreenshot, (1 << 2))

            self.assertEqual(Photos.PHAssetMediaSubtypeVideoStreamed, (1 << 16))
            self.assertEqual(Photos.PHAssetMediaSubtypeVideoHighFrameRate, (1 << 17))
            self.assertEqual(Photos.PHAssetMediaSubtypeVideoTimelapse, (1 << 18))


if __name__ == "__main__":
    main()
