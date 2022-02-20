from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos
import Quartz

PHAssetImageProgressHandler = b"vd@o^Z@"
PHAssetVideoProgressHandler = b"vd@o^Z@"


class TestPHImageManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Photos.PHImageRequestOptionsDeliveryMode)
        self.assertIsEnumType(Photos.PHImageRequestOptionsResizeMode)
        self.assertIsEnumType(Photos.PHImageRequestOptionsVersion)
        self.assertIsEnumType(Photos.PHVideoRequestOptionsDeliveryMode)
        self.assertIsEnumType(Photos.PHVideoRequestOptionsVersion)
        self.assertIsEnumType(Photos.UIImageOrientation)

    @min_os_level("10.13")
    def testConstants(self):
        self.assertEqual(Photos.PHImageRequestOptionsVersionCurrent, 0)
        self.assertEqual(Photos.PHImageRequestOptionsVersionUnadjusted, 1)
        self.assertEqual(Photos.PHImageRequestOptionsVersionOriginal, 2)

        self.assertEqual(Photos.PHImageRequestOptionsDeliveryModeOpportunistic, 0)
        self.assertEqual(Photos.PHImageRequestOptionsDeliveryModeHighQualityFormat, 1)
        self.assertEqual(Photos.PHImageRequestOptionsDeliveryModeFastFormat, 2)

        self.assertEqual(Photos.PHImageRequestOptionsResizeModeNone, 0)
        self.assertEqual(Photos.PHImageRequestOptionsResizeModeFast, 1)
        self.assertEqual(Photos.PHImageRequestOptionsResizeModeExact, 2)

        self.assertEqual(Photos.PHInvalidImageRequestID, 0)

        self.assertIsInstance(Photos.PHImageManagerMaximumSize, Quartz.CGSize)

        self.assertIsInstance(Photos.PHImageResultIsInCloudKey, str)
        self.assertIsInstance(Photos.PHImageResultIsDegradedKey, str)
        self.assertIsInstance(Photos.PHImageResultRequestIDKey, str)
        self.assertIsInstance(Photos.PHImageCancelledKey, str)
        self.assertIsInstance(Photos.PHImageErrorKey, str)

        self.assertEqual(Photos.PHVideoRequestOptionsDeliveryModeAutomatic, 0)
        self.assertEqual(Photos.PHVideoRequestOptionsDeliveryModeHighQualityFormat, 1)
        self.assertEqual(Photos.PHVideoRequestOptionsDeliveryModeMediumQualityFormat, 2)
        self.assertEqual(Photos.PHVideoRequestOptionsDeliveryModeFastFormat, 3)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Photos.PHImageRequestOptions.isNetworkAccessAllowed)
        self.assertArgIsBOOL(Photos.PHImageRequestOptions.setNetworkAccessAllowed_, 0)

        self.assertResultIsBOOL(Photos.PHImageRequestOptions.isSynchronous)
        self.assertArgIsBOOL(Photos.PHImageRequestOptions.setSynchronous_, 0)

        self.assertResultIsBlock(
            Photos.PHImageRequestOptions.progressHandler, PHAssetImageProgressHandler
        )
        self.assertArgIsBlock(
            Photos.PHImageRequestOptions.setProgressHandler_,
            0,
            PHAssetImageProgressHandler,
        )

        self.assertArgIsBlock(
            Photos.PHImageManager.requestImageForAsset_targetSize_contentMode_options_resultHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            Photos.PHImageManager.requestImageDataForAsset_options_resultHandler_,
            2,
            b"v@@I@",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(Photos.PHLivePhotoRequestOptions.isNetworkAccessAllowed)
        self.assertArgIsBOOL(
            Photos.PHLivePhotoRequestOptions.setNetworkAccessAllowed_, 0
        )

        self.assertResultIsBlock(
            Photos.PHLivePhotoRequestOptions.progressHandler,
            PHAssetImageProgressHandler,
        )
        self.assertArgIsBlock(
            Photos.PHLivePhotoRequestOptions.setProgressHandler_,
            0,
            PHAssetImageProgressHandler,
        )

        self.assertResultIsBOOL(Photos.PHVideoRequestOptions.isNetworkAccessAllowed)
        self.assertArgIsBOOL(Photos.PHVideoRequestOptions.setNetworkAccessAllowed_, 0)

        self.assertResultIsBlock(
            Photos.PHVideoRequestOptions.progressHandler, PHAssetVideoProgressHandler
        )
        self.assertArgIsBlock(
            Photos.PHVideoRequestOptions.setProgressHandler_,
            0,
            PHAssetVideoProgressHandler,
        )

        self.assertArgIsBlock(
            Photos.PHImageManager.requestImageDataAndOrientationForAsset_options_resultHandler_,
            2,
            b"v@@I@",
        )
        self.assertArgIsBlock(
            Photos.PHImageManager.requestLivePhotoForAsset_targetSize_contentMode_options_resultHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            Photos.PHImageManager.requestPlayerItemForVideo_options_resultHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Photos.PHImageManager.requestExportSessionForVideo_options_exportPreset_resultHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            Photos.PHImageManager.requestAVAssetForVideo_options_resultHandler_,
            2,
            b"v@@@",
        )
