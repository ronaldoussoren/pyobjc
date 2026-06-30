from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import Photos


class TestPHPhotoLibrary(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Photos.PHAuthorizationStatus)
        self.assertEqual(Photos.PHAuthorizationStatusNotDetermined, 0)
        self.assertEqual(Photos.PHAuthorizationStatusRestricted, 1)
        self.assertEqual(Photos.PHAuthorizationStatusDenied, 2)
        self.assertEqual(Photos.PHAuthorizationStatusAuthorized, 3)

        self.assertIsEnumType(Photos.PHAccessLevel)
        self.assertEqual(Photos.PHAccessLevelAddOnly, 1)
        self.assertEqual(Photos.PHAccessLevelReadWrite, 2)

    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("PHPhotoLibraryChangeObserver", Photos)

    @min_sdk_level("10.15")
    def test_protocols10_15(self):
        self.assertProtocolExists("PHPhotoLibraryAvailabilityObserver", Photos)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.requestAuthorization_, 0, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.performChanges_completionHandler_, 1, b"vZ@"
        )
        self.assertArgIsOut(Photos.PHPhotoLibrary.performChangesAndWait_error_, 1)
        self.assertResultIsBOOL(Photos.PHPhotoLibrary.performChangesAndWait_error_)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.requestAuthorizationForAccessLevel_handler_,
            1,
            b"v" + objc._C_NSInteger,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(
            Photos.PHPhotoLibrary.fetchPersistentChangesSinceToken_error_,
            1,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(Photos.PHPhotoLibrary.isUploadJobExtensionEnabled)

        self.assertResultIsBOOL(
            Photos.PHPhotoLibrary.isUploadJobExtensionEnabled_error_
        )
        self.assertArgIsBOOL(
            Photos.PHPhotoLibrary.isUploadJobExtensionEnabled_error_, 0
        )
        self.assertArgIsOut(Photos.PHPhotoLibrary.isUploadJobExtensionEnabled_error_, 1)
