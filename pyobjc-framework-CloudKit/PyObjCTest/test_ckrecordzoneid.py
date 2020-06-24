from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKRecordZoneID(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKRecordZoneID")
        self.assertIsInstance(CloudKit.CKRecordZoneID, objc.objc_class)
