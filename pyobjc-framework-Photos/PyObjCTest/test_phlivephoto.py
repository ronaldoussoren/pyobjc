from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHLivePhoto(TestCase):
    def test_constants(self):
        self.assertEqual(Photos.PHLivePhotoRequestIDInvalid, 0)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Photos.PHLivePhotoInfoErrorKey, str)
        self.assertIsInstance(Photos.PHLivePhotoInfoIsDegradedKey, str)
        self.assertIsInstance(Photos.PHLivePhotoInfoCancelledKey, str)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            Photos.PHLivePhoto.requestLivePhotoWithResourceFileURLs_placeholderImage_targetSize_contentMode_resultHandler_,
            4,
            b"v@@",
        )
