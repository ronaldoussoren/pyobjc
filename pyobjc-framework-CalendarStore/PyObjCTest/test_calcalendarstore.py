
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendarStore (TestCase):
    def testConstants(self):
        self.assertEqual(CalSpanThisEvent, 0)
        self.assertEqual(CalSpanFutureEvents, 1)
        self.assertEqual(CalSpanAllEvents, 2)

        self.assertIsInstance(CalCalendarsChangedNotification, unicode)
        self.assertIsInstance(CalEventsChangedNotification, unicode)
        self.assertIsInstance(CalTasksChangedNotification, unicode)
        self.assertIsInstance(CalCalendarsChangedExternallyNotification, unicode)
        self.assertIsInstance(CalEventsChangedExternallyNotification, unicode)
        self.assertIsInstance(CalTasksChangedExternallyNotification, unicode)
        self.assertIsInstance(CalInsertedRecordsKey, unicode)
        self.assertIsInstance(CalUpdatedRecordsKey, unicode)
        self.assertIsInstance(CalDeletedRecordsKey, unicode)
        self.assertIsInstance(CalSenderProcessIDKey, unicode)
        self.assertIsInstance(CalUserUIDKey, unicode)

    def testMethods(self):
        self.assertArgIsOut(CalCalendarStore.saveCalendar_error_, 1)
        self.assertArgIsOut(CalCalendarStore.removeCalendar_error_, 1)

        self.assertArgIsOut(CalCalendarStore.saveEvent_span_error_, 2)
        self.assertResultIsBOOL(CalCalendarStore.saveEvent_span_error_)

        self.assertArgIsOut(CalCalendarStore.removeEvent_span_error_, 2)
        self.assertResultIsBOOL(CalCalendarStore.removeEvent_span_error_)

        self.assertArgIsOut(CalCalendarStore.saveTask_error_, 1)
        self.assertResultIsBOOL(CalCalendarStore.saveTask_error_)

        self.assertArgIsOut(CalCalendarStore.removeTask_error_, 1)
        self.assertResultIsBOOL(CalCalendarStore.removeTask_error_)

if __name__ == "__main__":
    main()
