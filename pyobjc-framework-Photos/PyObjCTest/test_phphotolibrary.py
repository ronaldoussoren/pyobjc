from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import Photos


class TestPHPhotoLibrary(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Photos.PHAccessLevel)
        self.assertIsEnumType(Photos.PHAuthorizationStatus)

    def testConstants(self):
        self.assertEqual(Photos.PHAuthorizationStatusNotDetermined, 0)
        self.assertEqual(Photos.PHAuthorizationStatusRestricted, 1)
        self.assertEqual(Photos.PHAuthorizationStatusDenied, 2)
        self.assertEqual(Photos.PHAuthorizationStatusAuthorized, 3)

        self.assertEqual(Photos.PHAccessLevelAddOnly, 1)
        self.assertEqual(Photos.PHAccessLevelReadWrite, 2)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("PHPhotoLibraryChangeObserver")

    @min_sdk_level("10.15")
    def testProtocols10_15(self):
        objc.protocolNamed("PHPhotoLibraryAvailabilityObserver")

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.requestAuthorization_, 0, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.performChanges_completionHandler_, 1, b"vZ@"
        )
        self.assertArgIsOut(Photos.PHPhotoLibrary.performChangesAndWait_error_, 1)
        self.assertResultIsBOOL(Photos.PHPhotoLibrary.performChangesAndWait_error_)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            Photos.PHPhotoLibrary.requestAuthorizationForAccessLevel_handler_,
            1,
            b"v" + objc._C_NSInteger,
        )
