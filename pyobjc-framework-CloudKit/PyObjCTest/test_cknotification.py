from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKNotification(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKNotificationType)
        self.assertIsEnumType(CloudKit.CKQueryNotificationReason)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKNotification")
        self.assertIsInstance(CloudKit.CKNotification, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKQueryNotification")
        self.assertIsInstance(CloudKit.CKQueryNotification, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKRecordZoneNotification")
        self.assertIsInstance(CloudKit.CKRecordZoneNotification, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(CloudKit.CKNotificationTypeQuery, 1)
        self.assertEqual(CloudKit.CKNotificationTypeRecordZone, 2)
        self.assertEqual(CloudKit.CKNotificationTypeReadNotification, 3)
        self.assertEqual(CloudKit.CKNotificationTypeDatabase, 4)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordCreated, 1)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordUpdated, 2)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordDeleted, 3)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(CloudKit.CKNotification.isPruned)
        # self.assertArgIsBOOL(CloudKit.CKNotification.setPruned_, 0)

        self.assertResultIsBOOL(CloudKit.CKQueryNotification.isPublicDatabase)
