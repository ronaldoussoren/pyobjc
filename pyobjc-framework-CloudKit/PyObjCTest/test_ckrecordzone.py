from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKRecordZone(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CloudKit.CKRecordZoneCapabilities)
        self.assertEqual(CloudKit.CKRecordZoneCapabilityFetchChanges, 1 << 0)
        self.assertEqual(CloudKit.CKRecordZoneCapabilityAtomic, 1 << 1)
        self.assertEqual(CloudKit.CKRecordZoneCapabilitySharing, 1 << 2)
        self.assertEqual(CloudKit.CKRecordZoneCapabilityZoneWideSharing, 1 << 3)

        self.assertIsEnumType(CloudKit.CKRecordZoneEncryptionScope)
        self.assertEqual(CloudKit.CKRecordZoneEncryptionScopePerRecord, 0)
        self.assertEqual(CloudKit.CKRecordZoneEncryptionScopePerZone, 1)

    def test_constants(self):
        self.assertIsInstance(CloudKit.CKRecordZoneDefaultName, str)

    @min_os_level("10.10")
    def test_classes(self):
        self.assertHasAttr(CloudKit, "CKRecordZone")
        self.assertIsInstance(CloudKit.CKRecordZone, objc.objc_class)
