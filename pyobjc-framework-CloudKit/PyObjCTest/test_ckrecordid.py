from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKRecordID(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKRecordID")
        self.assertIsInstance(CloudKit.CKRecordID, objc.objc_class)
