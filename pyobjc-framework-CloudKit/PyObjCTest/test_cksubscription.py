from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKSubscription(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKQuerySubscriptionOptions)
        self.assertIsEnumType(CloudKit.CKSubscriptionType)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKSubscription")
        self.assertIsInstance(CloudKit.CKSubscription, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKNotificationInfo")
        self.assertIsInstance(CloudKit.CKNotificationInfo, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(CloudKit.CKSubscriptionTypeQuery, 1)
        self.assertEqual(CloudKit.CKSubscriptionTypeRecordZone, 2)
        self.assertEqual(CloudKit.CKSubscriptionTypeDatabase, 3)

        self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordCreation, 1)
        self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordUpdate, 2)
        self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordDeletion, 4)
        self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnce, 8)

        self.assertEqual(
            CloudKit.CKQuerySubscriptionOptionsFiresOnRecordCreation, 1 << 0
        )
        self.assertEqual(CloudKit.CKQuerySubscriptionOptionsFiresOnRecordUpdate, 1 << 1)
        self.assertEqual(
            CloudKit.CKQuerySubscriptionOptionsFiresOnRecordDeletion, 1 << 2
        )
        self.assertEqual(CloudKit.CKQuerySubscriptionOptionsFiresOnce, 1 << 3)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(CloudKit.CKNotificationInfo.shouldBadge)
        self.assertArgIsBOOL(CloudKit.CKNotificationInfo.setShouldBadge_, 0)

        self.assertResultIsBOOL(CloudKit.CKNotificationInfo.shouldSendContentAvailable)
        self.assertArgIsBOOL(
            CloudKit.CKNotificationInfo.setShouldSendContentAvailable_, 0
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CloudKit.CKNotificationInfo.shouldSendMutableContent)
        self.assertArgIsBOOL(
            CloudKit.CKNotificationInfo.setShouldSendMutableContent_, 0
        )
