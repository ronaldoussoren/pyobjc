import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKError (TestCase):
        @min_os_level("10.10")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKErrorDomain, unicode)
            self.assertIsInstance(CloudKit.CKPartialErrorsByItemIDKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorAncestorRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorServerRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorClientRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKErrorRetryAfterKey, unicode)

            self.assertEqual(CloudKit.CKErrorInternalError, 1)
            self.assertEqual(CloudKit.CKErrorPartialFailure, 2)
            self.assertEqual(CloudKit.CKErrorNetworkUnavailable, 3)
            self.assertEqual(CloudKit.CKErrorNetworkFailure, 4)
            self.assertEqual(CloudKit.CKErrorBadContainer, 5)
            self.assertEqual(CloudKit.CKErrorServiceUnavailable, 6)
            self.assertEqual(CloudKit.CKErrorRequestRateLimited, 7)
            self.assertEqual(CloudKit.CKErrorMissingEntitlement, 8)
            self.assertEqual(CloudKit.CKErrorNotAuthenticated, 9)
            self.assertEqual(CloudKit.CKErrorPermissionFailure, 10)
            self.assertEqual(CloudKit.CKErrorUnknownItem, 11)
            self.assertEqual(CloudKit.CKErrorInvalidArguments, 12)
            self.assertEqual(CloudKit.CKErrorResultsTruncated, 13)
            self.assertEqual(CloudKit.CKErrorServerRecordChanged, 14)
            self.assertEqual(CloudKit.CKErrorServerRejectedRequest, 15)
            self.assertEqual(CloudKit.CKErrorAssetFileNotFound, 16)
            self.assertEqual(CloudKit.CKErrorAssetFileModified, 17)
            self.assertEqual(CloudKit.CKErrorIncompatibleVersion, 18)
            self.assertEqual(CloudKit.CKErrorConstraintViolation, 19)
            self.assertEqual(CloudKit.CKErrorOperationCancelled, 20)
            self.assertEqual(CloudKit.CKErrorChangeTokenExpired, 21)
            self.assertEqual(CloudKit.CKErrorBatchRequestFailed, 22)
            self.assertEqual(CloudKit.CKErrorZoneBusy, 23)
            self.assertEqual(CloudKit.CKErrorBadDatabase, 24)
            self.assertEqual(CloudKit.CKErrorQuotaExceeded, 25)
            self.assertEqual(CloudKit.CKErrorZoneNotFound, 26)
            self.assertEqual(CloudKit.CKErrorLimitExceeded, 27)
            self.assertEqual(CloudKit.CKErrorUserDeletedZone, 28)
            self.assertEqual(CloudKit.CKErrorTooManyParticipants, 29)
            self.assertEqual(CloudKit.CKErrorAlreadyShared, 30)
            self.assertEqual(CloudKit.CKErrorReferenceViolation, 31)
            self.assertEqual(CloudKit.CKErrorManagedAccountRestricted, 32)
            self.assertEqual(CloudKit.CKErrorParticipantMayNeedVerification, 33)
            self.assertEqual(CloudKit.CKErrorServerResponseLost, 34)
            self.assertEqual(CloudKit.CKErrorAssetNotAvailable, 35)

if __name__ == "__main__":
    main()
