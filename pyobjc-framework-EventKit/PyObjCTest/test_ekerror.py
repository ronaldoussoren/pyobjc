import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKAlarm (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertIsInstance(EventKit.EKErrorDomain, unicode)

            self.assertEqual(EventKit.EKErrorEventNotMutable, 0)
            self.assertEqual(EventKit.EKErrorNoCalendar, 1)
            self.assertEqual(EventKit.EKErrorNoStartDate, 2)
            self.assertEqual(EventKit.EKErrorNoEndDate, 3)
            self.assertEqual(EventKit.EKErrorDatesInverted, 4)
            self.assertEqual(EventKit.EKErrorInternalFailure, 5)
            self.assertEqual(EventKit.EKErrorCalendarReadOnly, 6)
            self.assertEqual(EventKit.EKErrorDurationGreaterThanRecurrence, 7)
            self.assertEqual(EventKit.EKErrorAlarmGreaterThanRecurrence, 8)
            self.assertEqual(EventKit.EKErrorStartDateTooFarInFuture, 9)
            self.assertEqual(EventKit.EKErrorStartDateCollidesWithOtherOccurrence, 10)
            self.assertEqual(EventKit.EKErrorObjectBelongsToDifferentStore, 11)
            self.assertEqual(EventKit.EKErrorInvitesCannotBeMoved, 12)
            self.assertEqual(EventKit.EKErrorInvalidSpan, 13)
            self.assertEqual(EventKit.EKErrorCalendarHasNoSource, 14)
            self.assertEqual(EventKit.EKErrorCalendarSourceCannotBeModified, 15)
            self.assertEqual(EventKit.EKErrorCalendarIsImmutable, 16)
            self.assertEqual(EventKit.EKErrorSourceDoesNotAllowCalendarAddDelete, 17)
            self.assertEqual(EventKit.EKErrorRecurringReminderRequiresDueDate, 18)
            self.assertEqual(EventKit.EKErrorStructuredLocationsNotSupported, 19)
            self.assertEqual(EventKit.EKErrorReminderLocationsNotSupported, 20)
            self.assertEqual(EventKit.EKErrorAlarmProximityNotSupported, 21)
            self.assertEqual(EventKit.EKErrorCalendarDoesNotAllowEvents, 22)
            self.assertEqual(EventKit.EKErrorCalendarDoesNotAllowReminders, 23)
            self.assertEqual(EventKit.EKErrorSourceDoesNotAllowReminders, 24)
            self.assertEqual(EventKit.EKErrorSourceDoesNotAllowEvents, 25)
            self.assertEqual(EventKit.EKErrorPriorityIsInvalid, 26)
            self.assertEqual(EventKit.EKErrorInvalidEntityType, 27)
            self.assertEqual(EventKit.EKErrorProcedureAlarmsNotMutable, 28)
            self.assertEqual(EventKit.EKErrorEventStoreNotAuthorized, 29)
            self.assertEqual(EventKit.EKErrorOSNotSupported, 30)
            self.assertEqual(EventKit.EKErrorLast, 31)

if __name__ == '__main__':
    main()
