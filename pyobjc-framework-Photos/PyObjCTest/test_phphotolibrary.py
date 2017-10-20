from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHPhotoLibrary (TestCase):
        def testConstants(self):
            self.assertEqual(Photos.PHAuthorizationStatusNotDetermined, 0)
            self.assertEqual(Photos.PHAuthorizationStatusRestricted, 1)
            self.assertEqual(Photos.PHAuthorizationStatusDenied, 2)
            self.assertEqual(Photos.PHAuthorizationStatusAuthorized, 3)

        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('PHPhotoLibraryChangeObserver')

        @min_os_level('10.13')
        def testMethods(self):
            self.assertArgIsBlock(Photos.PHPhotoLibrary.requestAuthorization_, 0, b'v' + objc._C_NSInteger)
            self.assertArgIsBlock(Photos.PHPhotoLibrary.performChanges_completionHandler_, 1, b'vZ@')
            self.assertArgIsOut(Photos.PHPhotoLibrary.performChangesAndWait_error_, 1)
            self.assertResultIsBOOL(Photos.PHPhotoLibrary.performChangesAndWait_error_)

if __name__ == "__main__":
    main()
