from PyObjCTools.TestSupport import TestCase
import Photos


class TestPHError(TestCase):
    def test_constants(self):
        self.assertEqual(Photos.PHPhotosErrorInternalError, -1)

        self.assertEqual(Photos.PHPhotosErrorUserCancelled, 3072)
        self.assertEqual(Photos.PHPhotosErrorLibraryVolumeOffline, 3114)
        self.assertEqual(Photos.PHPhotosErrorRelinquishingLibraryBundleToWriter, 3142)
        self.assertEqual(Photos.PHPhotosErrorSwitchingSystemPhotoLibrary, 3143)
        self.assertEqual(Photos.PHPhotosErrorNetworkAccessRequired, 3164)
        self.assertEqual(Photos.PHPhotosErrorNetworkError, 3169)
        self.assertEqual(Photos.PHPhotosErrorIdentifierNotFound, 3201)
        self.assertEqual(Photos.PHPhotosErrorMultipleIdentifiersFound, 3202)

        self.assertEqual(Photos.PHPhotosErrorChangeNotSupported, 3300)
        self.assertEqual(Photos.PHPhotosErrorOperationInterrupted, 3301)
        self.assertEqual(Photos.PHPhotosErrorInvalidResource, 3302)
        self.assertEqual(Photos.PHPhotosErrorMissingResource, 3303)
        self.assertEqual(Photos.PHPhotosErrorNotEnoughSpace, 3305)
        self.assertEqual(Photos.PHPhotosErrorRequestNotSupportedForAsset, 3306)

        self.assertEqual(Photos.PHPhotosErrorAccessRestricted, 3310)
        self.assertEqual(Photos.PHPhotosErrorAccessUserDenied, 3311)

        self.assertEqual(Photos.PHPhotosErrorLibraryInFileProviderSyncRoot, 5423)

        self.assertEqual(Photos.PHPhotosErrorPersistentChangeTokenExpired, 3105)
        self.assertEqual(Photos.PHPhotosErrorPersistentChangeDetailsUnavailable, 3210)

        self.assertEqual(Photos.PHPhotosErrorInvalid, -1)
