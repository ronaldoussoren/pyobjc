from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKNotification(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CloudKit.CKNotificationType)
        self.assertEqual(CloudKit.CKNotificationTypeQuery, 1)
        self.assertEqual(CloudKit.CKNotificationTypeRecordZone, 2)
        self.assertEqual(CloudKit.CKNotificationTypeReadNotification, 3)
        self.assertEqual(CloudKit.CKNotificationTypeDatabase, 4)

        self.assertIsEnumType(CloudKit.CKQueryNotificationReason)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordCreated, 1)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordUpdated, 2)
        self.assertEqual(CloudKit.CKQueryNotificationReasonRecordDeleted, 3)

    @min_os_level("10.10")
    def test_methods(self):
        self.assertResultIsBOOL(CloudKit.CKNotification.isPruned)

        self.assertResultIsBOOL(CloudKit.CKQueryNotification.isPublicDatabase)
