from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKRecordZone(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKRecordZone")
        self.assertIsInstance(CloudKit.CKRecordZone, objc.objc_class)

    @min_os_level("10.8")
    def testConstants(self):
        self.assertEqual(CloudKit.CKRecordZoneCapabilityFetchChanges, 1 << 0)
        self.assertEqual(CloudKit.CKRecordZoneCapabilityAtomic, 1 << 1)
        self.assertEqual(CloudKit.CKRecordZoneCapabilitySharing, 1 << 2)
        self.assertIsInstance(CloudKit.CKRecordZoneDefaultName, str)
