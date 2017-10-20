from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos
    import Quartz

    PHAssetImageProgressHandler = b'vd@o^Z@'

    class TestPHImageManager (TestCase):
        @min_os_level('10.13')
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

            self.assertIsInstance(Photos.PHImageResultIsInCloudKey, unicode)
            self.assertIsInstance(Photos.PHImageResultIsDegradedKey, unicode)
            self.assertIsInstance(Photos.PHImageResultRequestIDKey, unicode)
            self.assertIsInstance(Photos.PHImageCancelledKey, unicode)
            self.assertIsInstance(Photos.PHImageErrorKey, unicode)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(Photos.PHImageRequestOptions.isNetworkAccessAllowed)
            self.assertArgIsBOOL(Photos.PHImageRequestOptions.setNetworkAccessAllowed_, 0)

            self.assertResultIsBOOL(Photos.PHImageRequestOptions.isSynchronous)
            self.assertArgIsBOOL(Photos.PHImageRequestOptions.setSynchronous_, 0)

            self.assertResultIsBlock(Photos.PHImageRequestOptions.progressHandler, PHAssetImageProgressHandler)
            self.assertArgIsBlock(Photos.PHImageRequestOptions.setProgressHandler_, 0, PHAssetImageProgressHandler)

            self.assertArgIsBlock(Photos.PHImageManager.requestImageForAsset_targetSize_contentMode_options_resultHandler_, 4, b'v@@')
            self.assertArgIsBlock(Photos.PHImageManager.requestImageDataForAsset_options_resultHandler_, 2, b'v@@I@')

if __name__ == "__main__":
    main()
