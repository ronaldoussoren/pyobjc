from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKModifyRecordsOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKModifyRecordsOperation")
        self.assertIsInstance(CloudKit.CKModifyRecordsOperation, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(CloudKit.CKRecordSaveIfServerRecordUnchanged, 0)
        self.assertEqual(CloudKit.CKRecordSaveChangedKeys, 1)
        self.assertEqual(CloudKit.CKRecordSaveAllKeys, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(CloudKit.CKModifyRecordsOperation.atomic)
        self.assertArgIsBOOL(CloudKit.CKModifyRecordsOperation.setAtomic_, 0)

        self.assertResultIsBlock(
            CloudKit.CKModifyRecordsOperation.perRecordProgressBlock, b"v@d"
        )
        self.assertArgIsBlock(
            CloudKit.CKModifyRecordsOperation.setPerRecordProgressBlock_, 0, b"v@d"
        )
        self.assertResultIsBlock(
            CloudKit.CKModifyRecordsOperation.perRecordCompletionBlock, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKModifyRecordsOperation.setPerRecordCompletionBlock_, 0, b"v@"
        )
        self.assertResultIsBlock(
            CloudKit.CKModifyRecordsOperation.modifyRecordsCompletionBlock, b"v@@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKModifyRecordsOperation.setModifyRecordsCompletionBlock_,
            0,
            b"v@@@",
        )
