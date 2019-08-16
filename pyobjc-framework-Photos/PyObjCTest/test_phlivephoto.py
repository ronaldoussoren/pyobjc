from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHLivePhoto(TestCase):
        def test_constants(self):
            self.assertEqual(Photos.PHLivePhotoRequestIDInvalid, 0)

        @min_os_level("10.15")
        def test_constants10_15(self):
            self.assertIsInstance(Photos.PHLivePhotoInfoErrorKey, unicode)
            self.assertIsInstance(Photos.PHLivePhotoInfoIsDegradedKey, unicode)
            self.assertIsInstance(Photos.PHLivePhotoInfoCancelledKey, unicode)

        @min_os_level("10.15")
        def test_methods10_15(self):
            self.assertArgIsBlock(
                Photos.PHLivePhoto.requestLivePhotoWithResourceFileURLs_placeholderImage_targetSize_contentMode_resultHandler_,
                4,
                b"v@@",
            )


if __name__ == "__main__":
    main()
