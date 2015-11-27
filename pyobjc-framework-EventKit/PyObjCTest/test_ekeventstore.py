import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKEventStore (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKEventStore"))

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(EventKit.EKEventStore.commit_)
            self.assertArgIsOut(EventKit.EKEventStore.commit_, 0)

            self.assertArgIsBlock(EventKit.EKEventStore.enumerateEventsMatchingPredicate_usingBlock_, 1, b'v@o^B')
            self.assertArgIsBlock(EventKit.EKEventStore.fetchRemindersMatchingPredicate_completion_, 1, b'v@')

            self.assertResultIsBOOL(EventKit.EKEventStore.removeCalendar_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.removeCalendar_commit_error_, 1)
            self.assertArgIsOut(EventKit.EKEventStore.removeCalendar_commit_error_, 2)

            self.assertResultIsBOOL(EventKit.EKEventStore.removeEvent_span_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.removeEvent_span_commit_error_, 2)
            self.assertArgIsOut(EventKit.EKEventStore.removeEvent_span_commit_error_, 3)


            self.assertResultIsBOOL(EventKit.EKEventStore.removeReminder_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.removeReminder_commit_error_, 1)
            self.assertArgIsOut(EventKit.EKEventStore.removeReminder_commit_error_, 2)

            self.assertResultIsBOOL(EventKit.EKEventStore.saveCalendar_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.saveCalendar_commit_error_, 1)
            self.assertArgIsOut(EventKit.EKEventStore.saveCalendar_commit_error_, 2)

            self.assertResultIsBOOL(EventKit.EKEventStore.saveEvent_span_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.saveEvent_span_commit_error_, 2)
            self.assertArgIsOut(EventKit.EKEventStore.saveEvent_span_commit_error_, 3)


            self.assertResultIsBOOL(EventKit.EKEventStore.saveReminder_commit_error_)
            self.assertArgIsBOOL(EventKit.EKEventStore.saveReminder_commit_error_, 1)
            self.assertArgIsOut(EventKit.EKEventStore.saveReminder_commit_error_, 2)

        @min_os_level('10.9')
        def testMethods10_9(self):
            self.assertArgIsBlock(EventKit.EKEventStore.requestAccessToEntityType_completion_, 1, b"vZ@")

        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(EventKit.EKSpanThisEvent, 0)
            self.assertEqual(EventKit.EKSpanFutureEvents, 1)

            self.assertIsInstance(EventKit.EKEventStoreChangedNotification, unicode)

            self.assertEqual(EventKit.EKAuthorizationStatusNotDetermined, 0)
            self.assertEqual(EventKit.EKAuthorizationStatusRestricted, 1)
            self.assertEqual(EventKit.EKAuthorizationStatusDenied, 2)
            self.assertEqual(EventKit.EKAuthorizationStatusAuthorized, 3)

if __name__ == '__main__':
    main()
