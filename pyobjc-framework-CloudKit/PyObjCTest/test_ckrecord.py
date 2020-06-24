from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import CloudKit
import objc


class TestCKRecord(TestCase):
    @min_sdk_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("CKRecordKeyValueSetting")

    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKRecord")
        self.assertIsInstance(CloudKit.CKRecord, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertIsInstance(CloudKit.CKRecordTypeUserRecord, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CloudKit.CKRecordParentKey, str)
        self.assertIsInstance(CloudKit.CKRecordShareKey, str)
