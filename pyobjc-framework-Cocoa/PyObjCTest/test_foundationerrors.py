from Foundation import *
from PyObjCTools.TestSupport import *

class FoundationErrorsTest (TestCase):
    def testConstants(self):
        self.assertEqual(NSFileNoSuchFileError, 4)
        self.assertEqual(NSFileLockingError, 255)
        self.assertEqual(NSFileReadUnknownError, 256)
        self.assertEqual(NSFileReadNoPermissionError, 257)
        self.assertEqual(NSFileReadInvalidFileNameError, 258)
        self.assertEqual(NSFileReadCorruptFileError, 259)
        self.assertEqual(NSFileReadInapplicableStringEncodingError, 261)
        self.assertEqual(NSFileReadUnsupportedSchemeError, 262)
        self.assertEqual(NSFileReadTooLargeError, 263)
        self.assertEqual(NSFileReadUnknownStringEncodingError, 264)
        self.assertEqual(NSFileWriteUnknownError, 512)
        self.assertEqual(NSFileWriteNoPermissionError, 513)
        self.assertEqual(NSFileWriteInvalidFileNameError, 514)
        self.assertEqual(NSFileWriteInapplicableStringEncodingError, 517)
        self.assertEqual(NSFileWriteUnsupportedSchemeError, 518)
        self.assertEqual(NSFileWriteOutOfSpaceError, 640)
        self.assertEqual(NSKeyValueValidationError, 1024)
        self.assertEqual(NSUserCancelledError, 3072)
        self.assertEqual(NSExecutableNotLoadableError, 3584)
        self.assertEqual(NSExecutableArchitectureMismatchError, 3585)
        self.assertEqual(NSExecutableRuntimeMismatchError, 3586)
        self.assertEqual(NSExecutableLoadError, 3587)
        self.assertEqual(NSExecutableLinkError, 3588)
        self.assertEqual(NSFileErrorMinimum, 0)
        self.assertEqual(NSFileErrorMaximum, 1023)
        self.assertEqual(NSValidationErrorMinimum, 1024)
        self.assertEqual(NSValidationErrorMaximum, 2047)
        self.assertEqual(NSExecutableErrorMinimum, 3584)
        self.assertEqual(NSExecutableErrorMaximum, 3839)
        self.assertEqual(NSFormattingErrorMinimum, 2048)
        self.assertEqual(NSFormattingErrorMaximum, 2559)
        self.assertEqual(NSFormattingError, 2048)
        self.assertEqual(NSCoderInvalidValueError, 4866)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSFileWriteVolumeReadOnlyError, 642)

        self.assertEqual(NSPropertyListReadCorruptError, 3840)
        self.assertEqual(NSPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(NSPropertyListReadStreamError, 3842)
        self.assertEqual(NSPropertyListWriteStreamError, 3851)
        self.assertEqual(NSPropertyListErrorMinimum, 3840)
        self.assertEqual(NSPropertyListErrorMaximum, 4095)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSFileWriteFileExistsError, 516)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSFeatureUnsupportedError, 3328)
        self.assertEqual(NSXPCConnectionInterrupted, 4097)
        self.assertEqual(NSXPCConnectionInvalid, 4099)
        self.assertEqual(NSXPCConnectionReplyInvalid, 4101)
        self.assertEqual(NSXPCConnectionErrorMinimum, 4096)
        self.assertEqual(NSXPCConnectionErrorMaximum, 4224)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertEqual(NSUbiquitousFileUnavailableError, 4353)
        self.assertEqual(NSUbiquitousFileNotUploadedDueToQuotaError, 4354)
        self.assertEqual(NSUbiquitousFileUbiquityServerNotAvailable, 4355)
        self.assertEqual(NSUbiquitousFileErrorMinimum, 4352)
        self.assertEqual(NSUbiquitousFileErrorMaximum, 4607)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSUserActivityHandoffFailedError, 4608)
        self.assertEqual(NSUserActivityConnectionUnavailableError, 4609)
        self.assertEqual(NSUserActivityRemoteApplicationTimedOutError, 4610)
        self.assertEqual(NSUserActivityHandoffUserInfoTooLargeError, 4611)
        self.assertEqual(NSUserActivityErrorMinimum, 4608)
        self.assertEqual(NSUserActivityErrorMaximum, 4863)
        self.assertEqual(NSPropertyListWriteInvalidError, 3852)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(NSFileManagerUnmountUnknownError, 768)
        self.assertEqual(NSFileManagerUnmountBusyError, 769)

        self.assertEqual(NSCoderReadCorruptError, 4864)
        self.assertEqual(NSCoderValueNotFoundError, 4865)
        self.assertEqual(NSCoderErrorMinimum, 4864)
        self.assertEqual(NSCoderErrorMaximum, 4991)

        self.assertEqual(NSBundleErrorMinimum, 4992)
        self.assertEqual(NSBundleErrorMaximum, 5119)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertEqual(NSCloudSharingNetworkFailureError, 5120)
        self.assertEqual(NSCloudSharingQuotaExceededError, 5121)
        self.assertEqual(NSCloudSharingTooManyParticipantsError, 5122)
        self.assertEqual(NSCloudSharingConflictError, 5123)
        self.assertEqual(NSCloudSharingNoPermissionError, 5124)
        self.assertEqual(NSCloudSharingOtherError, 5375)
        self.assertEqual(NSCloudSharingErrorMinimum, 5120)
        self.assertEqual(NSCloudSharingErrorMaximum, 5375)


if __name__ == "__main__":
    main()
