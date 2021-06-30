from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKFetchRecordZonesOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKFetchRecordZonesOperation")
        self.assertIsInstance(CloudKit.CKFetchRecordZonesOperation, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZonesOperation.setFetchRecordZonesCompletionBlock_,
            0,
            b"v@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock, b"v@@"
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZonesOperation.setPerRecordZoneCompletionBlock_,
            0,
            b"v@@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZonesOperation.perRecordZoneCompletionBlock, b"v@@@"
        )
