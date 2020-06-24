from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKModifyRecordZonesOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKModifyRecordZonesOperation")
        self.assertIsInstance(CloudKit.CKModifyRecordZonesOperation, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBlock(
            CloudKit.CKModifyRecordZonesOperation.modifyRecordZonesCompletionBlock,
            b"v@@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKModifyRecordZonesOperation.setModifyRecordZonesCompletionBlock_,
            0,
            b"v@@@",
        )
