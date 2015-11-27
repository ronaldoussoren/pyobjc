import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKSubscription (TestCase):
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

            self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordCreation, 1)
            self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordUpdate, 2)
            self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnRecordDeletion, 4)
            self.assertEqual(CloudKit.CKSubscriptionOptionsFiresOnce, 8)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBOOL(CloudKit.CKNotificationInfo.shouldBadge)
            self.assertArgIsBOOL(CloudKit.CKNotificationInfo.setShouldBadge_, 0)

            self.assertResultIsBOOL(CloudKit.CKNotificationInfo.shouldSendContentAvailable)
            self.assertArgIsBOOL(CloudKit.CKNotificationInfo.setShouldSendContentAvailable_, 0)

if __name__ == "__main__":
    main()
