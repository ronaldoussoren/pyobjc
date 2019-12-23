from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHError(TestCase):
        def test_constants(self):
            self.assertEqual(Photos.PHPhotosErrorInvalid, -1)
            self.assertEqual(Photos.PHPhotosErrorUserCancelled, 3072)
            self.assertEqual(Photos.PHPhotosErrorLibraryVolumeOffline, 3114)
            self.assertEqual(
                Photos.PHPhotosErrorRelinquishingLibraryBundleToWriter, 3142
            )
            self.assertEqual(Photos.PHPhotosErrorSwitchingSystemPhotoLibrary, 3143)


if __name__ == "__main__":
    main()
