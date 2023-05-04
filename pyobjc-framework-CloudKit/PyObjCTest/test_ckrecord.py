from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import CloudKit
import objc


class TestCKRecord(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        # Documentation claims this protocol is available on 10.11,
        # but value isn't present in the latest 10.11 SDK.
        self.assertProtocolExists("CKRecordKeyValueSetting")

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
