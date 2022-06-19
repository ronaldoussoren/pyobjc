import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class FoundationErrorsTest(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSFileNoSuchFileError, 4)
        self.assertEqual(Foundation.NSFileLockingError, 255)
        self.assertEqual(Foundation.NSFileReadUnknownError, 256)
        self.assertEqual(Foundation.NSFileReadNoPermissionError, 257)
        self.assertEqual(Foundation.NSFileReadInvalidFileNameError, 258)
        self.assertEqual(Foundation.NSFileReadCorruptFileError, 259)
        self.assertEqual(Foundation.NSFileReadInapplicableStringEncodingError, 261)
        self.assertEqual(Foundation.NSFileReadUnsupportedSchemeError, 262)
        self.assertEqual(Foundation.NSFileReadTooLargeError, 263)
        self.assertEqual(Foundation.NSFileReadUnknownStringEncodingError, 264)
        self.assertEqual(Foundation.NSFileWriteUnknownError, 512)
        self.assertEqual(Foundation.NSFileWriteNoPermissionError, 513)
        self.assertEqual(Foundation.NSFileWriteInvalidFileNameError, 514)
        self.assertEqual(Foundation.NSFileWriteInapplicableStringEncodingError, 517)
        self.assertEqual(Foundation.NSFileWriteUnsupportedSchemeError, 518)
        self.assertEqual(Foundation.NSFileWriteOutOfSpaceError, 640)
        self.assertEqual(Foundation.NSKeyValueValidationError, 1024)
        self.assertEqual(Foundation.NSUserCancelledError, 3072)
        self.assertEqual(Foundation.NSExecutableNotLoadableError, 3584)
        self.assertEqual(Foundation.NSExecutableArchitectureMismatchError, 3585)
        self.assertEqual(Foundation.NSExecutableRuntimeMismatchError, 3586)
        self.assertEqual(Foundation.NSExecutableLoadError, 3587)
        self.assertEqual(Foundation.NSExecutableLinkError, 3588)
        self.assertEqual(Foundation.NSFileErrorMinimum, 0)
        self.assertEqual(Foundation.NSFileErrorMaximum, 1023)
        self.assertEqual(Foundation.NSValidationErrorMinimum, 1024)
        self.assertEqual(Foundation.NSValidationErrorMaximum, 2047)
        self.assertEqual(Foundation.NSExecutableErrorMinimum, 3584)
        self.assertEqual(Foundation.NSExecutableErrorMaximum, 3839)
        self.assertEqual(Foundation.NSFormattingErrorMinimum, 2048)
        self.assertEqual(Foundation.NSFormattingErrorMaximum, 2559)
        self.assertEqual(Foundation.NSFormattingError, 2048)
        self.assertEqual(Foundation.NSCoderInvalidValueError, 4866)

        self.assertEqual(Foundation.NSBundleOnDemandResourceOutOfSpaceError, 4992)
        self.assertEqual(
            Foundation.NSBundleOnDemandResourceExceededMaximumSizeError, 4993
        )
        self.assertEqual(Foundation.NSBundleOnDemandResourceInvalidTagError, 4994)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSFileWriteVolumeReadOnlyError, 642)

        self.assertEqual(Foundation.NSPropertyListReadCorruptError, 3840)
        self.assertEqual(Foundation.NSPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(Foundation.NSPropertyListReadStreamError, 3842)
        self.assertEqual(Foundation.NSPropertyListWriteStreamError, 3851)
        self.assertEqual(Foundation.NSPropertyListErrorMinimum, 3840)
        self.assertEqual(Foundation.NSPropertyListErrorMaximum, 4095)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSFileWriteFileExistsError, 516)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSFeatureUnsupportedError, 3328)
        self.assertEqual(Foundation.NSXPCConnectionInterrupted, 4097)
        self.assertEqual(Foundation.NSXPCConnectionInvalid, 4099)
        self.assertEqual(Foundation.NSXPCConnectionReplyInvalid, 4101)
        self.assertEqual(Foundation.NSXPCConnectionCodeSigningRequirementFailure, 4102)
        self.assertEqual(Foundation.NSXPCConnectionErrorMinimum, 4096)
        self.assertEqual(Foundation.NSXPCConnectionErrorMaximum, 4224)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(Foundation.NSUbiquitousFileUnavailableError, 4353)
        self.assertEqual(Foundation.NSUbiquitousFileNotUploadedDueToQuotaError, 4354)
        self.assertEqual(Foundation.NSUbiquitousFileUbiquityServerNotAvailable, 4355)
        self.assertEqual(Foundation.NSUbiquitousFileErrorMinimum, 4352)
        self.assertEqual(Foundation.NSUbiquitousFileErrorMaximum, 4607)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSUserActivityHandoffFailedError, 4608)
        self.assertEqual(Foundation.NSUserActivityConnectionUnavailableError, 4609)
        self.assertEqual(Foundation.NSUserActivityRemoteApplicationTimedOutError, 4610)
        self.assertEqual(Foundation.NSUserActivityHandoffUserInfoTooLargeError, 4611)
        self.assertEqual(Foundation.NSUserActivityErrorMinimum, 4608)
        self.assertEqual(Foundation.NSUserActivityErrorMaximum, 4863)
        self.assertEqual(Foundation.NSPropertyListWriteInvalidError, 3852)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(Foundation.NSFileManagerUnmountUnknownError, 768)
        self.assertEqual(Foundation.NSFileManagerUnmountBusyError, 769)

        self.assertEqual(Foundation.NSCoderReadCorruptError, 4864)
        self.assertEqual(Foundation.NSCoderValueNotFoundError, 4865)
        self.assertEqual(Foundation.NSCoderErrorMinimum, 4864)
        self.assertEqual(Foundation.NSCoderErrorMaximum, 4991)

        self.assertEqual(Foundation.NSBundleErrorMinimum, 4992)
        self.assertEqual(Foundation.NSBundleErrorMaximum, 5119)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(Foundation.NSCloudSharingNetworkFailureError, 5120)
        self.assertEqual(Foundation.NSCloudSharingQuotaExceededError, 5121)
        self.assertEqual(Foundation.NSCloudSharingTooManyParticipantsError, 5122)
        self.assertEqual(Foundation.NSCloudSharingConflictError, 5123)
        self.assertEqual(Foundation.NSCloudSharingNoPermissionError, 5124)
        self.assertEqual(Foundation.NSCloudSharingOtherError, 5375)
        self.assertEqual(Foundation.NSCloudSharingErrorMinimum, 5120)
        self.assertEqual(Foundation.NSCloudSharingErrorMaximum, 5375)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertEqual(Foundation.NSCompressionFailedError, 5376)
        self.assertEqual(Foundation.NSDecompressionFailedError, 5377)
        self.assertEqual(Foundation.NSCompressionErrorMinimum, 5376)
        self.assertEqual(Foundation.NSCompressionErrorMaximum, 5503)
