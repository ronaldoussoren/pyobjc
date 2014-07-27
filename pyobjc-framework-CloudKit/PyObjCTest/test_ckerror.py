import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKAsset (TestCase):
        @min_os_level("10.10")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKErrorDomain, unicode)
            self.assertIsInstance(CloudKit.CKPartialErrorsByItemIDKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorAncestorRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorServerRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordChangedErrorClientRecordKey, unicode)
            self.assertIsInstance(CloudKit.CKErrorRetryAfterKey, unicode)

            self.assertEqual(CKErrorInternalError, 1)
            self.assertEqual(CKErrorPartialFailure, 2)
            self.assertEqual(CKErrorNetworkUnavailable, 3)
            self.assertEqual(CKErrorNetworkFailure, 4)
            self.assertEqual(CKErrorBadContainer, 5)
            self.assertEqual(CKErrorServiceUnavailable, 6)
            self.assertEqual(CKErrorRequestRateLimited, 7)
            self.assertEqual(CKErrorMissingEntitlement, 8)
            self.assertEqual(CKErrorNotAuthenticated, 9)
            self.assertEqual(CKErrorPermissionFailure, 10)
            self.assertEqual(CKErrorUnknownItem, 11)
            self.assertEqual(CKErrorInvalidArguments, 12)
            self.assertEqual(CKErrorResultsTruncated, 13)
            self.assertEqual(CKErrorServerRecordChanged, 14)
            self.assertEqual(CKErrorServerRejectedRequest, 15)
            self.assertEqual(CKErrorAssetFileNotFound, 16)
            self.assertEqual(CKErrorAssetFileModified, 17)
            self.assertEqual(CKErrorIncompatibleVersion, 18)
            self.assertEqual(CKErrorConstraintViolation, 19)
            self.assertEqual(CKErrorOperationCancelled, 20)
            self.assertEqual(CKErrorChangeTokenExpired, 21)
            self.assertEqual(CKErrorBatchRequestFailed, 22)
            self.assertEqual(CKErrorZoneBusy, 23)
            self.assertEqual(CKErrorBadDatabase, 24)
            self.assertEqual(CKErrorQuotaExceeded, 25)
            self.assertEqual(CKErrorZoneNotFound, 26)

if __name__ == "__main__":
    main()
